# !/usr/bin/env python
#
# Primitive tool to get the count of an unprescaled trigger
# 
# Input:
#	List of trigger names for which to get the counts, list of the directory where root files ("hltbits*.root", by default) reside.
# 	CalculateRates -- boolean variable specifying whether to compute the rates from counts,
# 	L1 rate corresponding to the run from which the events come
#
# Output:
#	A dictionary containing trigger names as values and respective counts as keys, and a csv file
# 	A dictionary containing trigger names as values and respective counts as rates, and a csv file
#
# Description:
# 	Count for a trigger is calculated as (N accepted events / N total events)
# 	Each hltbits*.root file contains one tree, "HltTree". In each tree, there is some number of entries (events) N 
# 	Branches of the tree are the triggers from the trigger menu
# 	For a given event, a trigger either accepts the event (attribute = 1) or rejects it (attribute = 0)
# 	To get the count of a given trigger, we need to consider all hltbits*.root files
# 	To get the total number of events, we need to sum the number of entries across all the files
# 	To get the total number of events accepted by the trigger, we need to sum the number of entries across all the files such that their attribute for the given trigger's name is 1

from __future__ import division
from decimal import Decimal 
#import csv 
import ROOT 
import os, fnmatch 
from tabulate import tabulate

#findFiles will return a list of all the subdirectories and filepaths in your target directory
def findFiles (path, filter):
	for root, dirs, files in os.walk(path):
		for file in fnmatch.filter(files, filter):
			yield os.path.join(root, file)

#Specify all relevant triggers in any subdirectory of the path
trigger_list = ["HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v2",
	"HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v2",
	"HLT_PFJet80_v5",
	"HLT_DiPFJetAve80_v3"
	]

#Specify the directory where the histrograms (*.root reside)
dataset_directory = "/afs/cern.ch/user/l/lkang/diphoton/rate_tests/CMSSW_8_0_11/src/crabjobs/HLTPhysics_Run274998/HLTPhysics/HLTPhysics/160628_100015/0000/" 

#Specify a filter for finding *.root files in the directory (and subdirectories)
events_file_filter = "hltbits*.root"

#Calculate rates from counts? Need l1 Rate corresponding to the run from which the events come 
calculate_rates = True

#L1 rate corresponding to the run from which the events come, in Hz
l1_rate = 78406.969

#Create a dictionary of all accepted events, events_accepted
events_accepted = dict.fromkeys(trigger_list, 0)

#Create a dictionary of all counts, counts
counts = dict.fromkeys(trigger_list, None)

#Declare a variable for a total number of events, events_total = 0
events_total = 0
  
try:			
	for events_file in findFiles(dataset_directory, events_file_filter):
		print ("Going through the file " + events_file)
		events_file_ROOT = ROOT.TFile(events_file)
		trigger_tree = ROOT.gDirectory.Get("HltTree")
                events_in_file = trigger_tree.GetEntries()
                print ("Number of events in the file is " + str(events_in_file))
                events_total += events_in_file
		for trigger_name in trigger_list:
			print ("Working with the trigger " + trigger_name) 
			accepted_by_trigger_in_file = 0 
			for event in trigger_tree:
				try:
					if getattr(event,trigger_name) == 1:
						accepted_by_trigger_in_file += 1
				except:
					err_notrigger = "Couldn't find the trigger " + trigger_name + " in the file " + str(events_file) 
					print err_notrigger
			print ("Number of events accepted by the trigger in the file is "+ str(accepted_by_trigger_in_file))
			events_accepted[trigger_name] += accepted_by_trigger_in_file
	
	counts_table = []
	rates_table = []

	print ("Total number of events is " + str(events_total))
	if events_total != 0:
		counts_writeout = open('counts.txt', 'wb') #csv.writer(open('counts.txt', 'wb'))	
		print "Writing the counts in a file counts.txt..."
		for trigger_name in trigger_list:
                	counts[trigger_name] = events_accepted[trigger_name]/events_total
                	count_display = '%.2E' % Decimal(str(counts[trigger_name])) + " count"
			counts_table.append([trigger_name, count_display])
			#counts_writeout.writerow([trigger_name, " | ", count_display])
		counts_print = tabulate(counts_table, headers=["Trigger Name","Trigger Count"])
		print "\n" + counts_print + "\n"
		counts_writeout.write(counts_print)
		counts_writeout.close()
	
	elif events_total == 0:
        	err_noevents = "Couldn't find any events" 
        	print err_noevents

	if calculate_rates:
		rates = dict.fromkeys(trigger_list, None)
		print rates
		print ("Calculating the corresponding rates. Using the formula rate = l1_rate * count. \nFor this run, l1_rate is " + str(l1_rate) + " Hz")
		rates_writeout = open('rates.txt', 'wb') #csv.writer(open('rates.txt','wb'))
		print "Writing the rates in a file rates.txt..."
		for trigger_name in trigger_list:
			rates[trigger_name] = counts[trigger_name] * l1_rate
			rate_display = '%.3E' % Decimal(str(rates[trigger_name])) + " Hz"
			rates_table.append([trigger_name, rate_display])
			#rates_writeout.writerow([trigger_name, " | ", rate_display])
		rates_print = tabulate(rates_table, headers=["Trigger Name","Trigger Rate"])
		print "\n" + rates_print + "\n"
		rates_writeout.write(rates_print)
		counts_writeout.close()
except:
	print "Something went wrong when going through *.root files"
