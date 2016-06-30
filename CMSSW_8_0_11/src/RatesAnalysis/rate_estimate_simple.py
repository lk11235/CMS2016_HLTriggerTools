#!/usr/bin/env python

# Primitive tool to get the count of an unprescaled trigger
# 
# Input: list of trigger names for which to get the counts, list of the directory where root files ("hltbits*.root", by default) reside.
# 	 calculateRates -- boolean variable specifying whether to compute the rates from counts,
# 	 L1 rate corresponding to the run from which the events come
# Output: a dictionary containing trigger names as values and respective counts as keys, and a csv file
# 	  a dictionary containing trigger names as values and respective counts as rates, and a csv file
# Description:
## Count for a trigger is calculated as (N accepted events / N total events). 
##
## Each hltbits*.root file contains one tree, "HltTree". In each tree, there is some number of entries (events) N. 
## Branches of the tree are the triggers from the trigger menu. 
## For a given event, a trigger either accepts the event (attribute = 1) or rejects it (attribute = 0).  
##
## To get the count of a given trigger, we need to consider all hltbits*.root files. 
## To get the total number of events, we need to sum the number of entries across all the files. 
## To get the total number of events accepted by the trigger, we need to sum the number of entries across all the files such that their attribute for the given trigger's name is 1.
#

# force non-truncating division to avoid converting ints to floats
from __future__ import division
# importing decimal for a neater work with decimal numbers (instead of floats)
from decimal import Decimal
# importing csv to write the counts in the file
import csv

import ROOT

# import libraries to parse through directories and find the required files
import os, fnmatch

# define a function that will find all the required files given the directory where thery reside
# input: 
#	string path, the absolute path to the directory where all files reside, possibly in subdirectories
#	string filter, a regexp to find all *.root files of interest
# output:
#	a list of absolute paths to the *.root files
def findFiles (path, filter):
	for root, dirs, files in os.walk(path):
		for file in fnmatch.filter(files, filter):
			yield os.path.join(root, file)

## Specify the list of trigger names for which to get the counts.
# edit these names as necessary; the names should coincide with those in trigger menus on ConfDB
trigger_list = ["HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v2",
	"HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v2",
	"HLT_PFJet80_v5",
	"HLT_DiPFJetAve80_v3"
	]

## Specify the directory where the histrograms (*.root reside)
dataset_directory = "/afs/cern.ch/user/a/aavkhadi/commissioning_trigger_bjet/rate_studies/CMSSW_8_0_11/src/tests/crabjobs" 
## Specify a filter for finding *.root files in the directory (and subdirectories)
events_file_filter = "hltbits*.root"

# Calculate rates from counts? Need l1 Rate corresponding to the run from which the events come 
calculate_rates = True

# L1 rate corresponding to the run from which the events come, in Hz
l1_rate = 78406.969

## Create a dictionary of all accepted events, events_accepted
### trigger names from the list as keys, and 0 as values. 
events_accepted = dict.fromkeys(trigger_list, 0)

## Create a dictionary of all counts, counts
### trigger names from the list as keys, and NaN as values.
counts = dict.fromkeys(trigger_list, None)

## Declare a variable for a total number of events, events_total = 0
events_total = 0
  
## Loop over all directories
try:			
	for events_file in findFiles(dataset_directory, events_file_filter):
		print ("Going through the file " + events_file)
		#### Open the file in ROOT: event_file = ROOT.
		events_file_ROOT = ROOT.TFile(events_file)
		#### Copy the tree from the file: trigger_tree = ROOT.gDirectory.Get("HltTree")
		trigger_tree = ROOT.gDirectory.Get("HltTree") # relies on the fact that all trees in files are named "HltTree"
		#### Copy the total number of events in the file:
                events_in_file = trigger_tree.GetEntries()
                print ("Number of events in the file is " + str(events_in_file))
                #### Increment events_total by events_in_file
                events_total += events_in_file
		#### Loop over the trigger names in accepted_events
		for trigger_name in trigger_list:
			##### Try to get the number of events in the file accepted by a given trigger: 
			print ("Working with the trigger " + trigger_name) 
			accepted_by_trigger_in_file = 0
			##### Loop over all events in the file: 
			for event in trigger_tree:
			###### If event was accepted by the trigger, increment the counter: 
				try:	
					if getattr(event,trigger_name) == 1:
						accepted_by_trigger_in_file += 1
				except:
					##### Exception: If couldn't find the trigger_name in the tree,
					##### print out that trigger was not found in the menu
				 	err_notrigger = "Couldn't find the trigger " + trigger_name + " in the file " + str(events_file) 
					print err_notrigger
			print ("Number of events accepted by the trigger in the file is "+ str(accepted_by_trigger_in_file))
			events_accepted[trigger_name] += accepted_by_trigger_in_file
	
	print ("Total number of events is " + str(events_total))
	## Loop over the counts dictionary. Compute the count for a given trigger as the respective value from events_accepted divided by event_total. 
	if events_total != 0:
		counts_writeout = csv.writer(open('counts.csv', 'wb'))	
		print "Writing the counts in a file counts.csv..."
		for trigger_name in trigger_list:
                	counts[trigger_name] = events_accepted[trigger_name]/events_total
                	# Print out the counts dictionary, display in scientific notation
			# see http://stackoverflow.com/questions/6913532/display-a-decimal-in-scientific-notation
                	count_display = '%.2E' % Decimal(str(counts[trigger_name]))
			counts_writeout.writerow([trigger_name, count_display])	
	elif events_total == 0:
        	err_noevents = "Couldn't find any events" 
        	print err_noevents

	if calculate_rates:
		rates = dict.fromkeys(trigger_list, None)
		print rates
		print ("Calculating the corresponding rates. Using the formula rate = l1_rate * count. \nFor this run, l1_rate is " + str(l1_rate) + " Hz")
		rates_writeout = csv.writer(open('rates.csv','wb'))
		print "Writing the rates in a file rates.csv..."
		for trigger_name in trigger_list:
			rates[trigger_name] = counts[trigger_name] * l1_rate
			rate_display = '%.3E' % Decimal(str(rates[trigger_name])) + " Hz"
			rates_writeout.writerow([trigger_name, rate_display])
except:
	print "Something went wrong when going through *.root files"
