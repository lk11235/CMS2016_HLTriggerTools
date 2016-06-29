# Primitive tool to get the count of an unprescaled trigger
# 
# Input: list of trigger names for which to get the counts, list of all directories where histograms ("hltbits*.root", by default) reside.
# Output: a dictionary containing trigger names as values and respective counts as keys.
#
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
# Pseudocode:
## import ROOT
## Specify the list of trigger names for which to get the counts.
## Specify the list of all directories where histrograms ("hltbits*.root" reside)
## 
## Create a dictionary of all accepted events, events_accepted
### trigger names from the list as keys, and 0 as values. 
## Create a dictionary of all rates, rates
### trigger names from the list as keys, and NaN as values.
## Declare a variable for a total number of events, events_total = 0
##  
## Loop over all directories
##
### Loop over all hltbits*.root fles (or abstract to a general name)
###
#### Open the file in ROOT: event_file = ROOT.TFile("hltbits*.root")
####
#### Copy the total number of events in the file: events_in_file = event_file.GetEntries()
#### Increment events_total by events_in_file
####
#### Copy the tree from the file: trigger_tree = ROOT.gDirectory.Get("HltTree")
#### Loop over the trigger names in accepted_events
####
##### Try to get the number of events in the file accepted by a given trigger: 
##### accepted_by_trigger_in_file = 0
####
##### Loop over all events in the file: for event in trigger_tree:
####
###### If event was accepted by the trigger, increment the counter: if getattr(event,trigger_name) == 1: accepted_by_trigger_in_file += 1
#####
##### Increment the value for the trigger in events_accepted by accepted_by_trigger_in_file
#####
##### Exception: If couldn't find the trigger_name in the tree, print out that trigger was not found in the menu
## 
## Loop over the rates dictionary. Compute the rate for a given trigger as the respective value from events_accepted divided by event_total. 
## Print out the rates dictionary.
#   

