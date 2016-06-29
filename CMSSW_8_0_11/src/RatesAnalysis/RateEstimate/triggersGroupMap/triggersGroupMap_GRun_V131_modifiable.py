# -*- coding: iso-8859-15 -*-

triggerName = "GRun_V131_modifiable"

triggersDatasetMap = {
	'HLT_DiPFJetAve80_v5': ['JetHT'],
	'HLT_PFJet80_v5': ['JetHT'],
	'HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v2': ['BTagCSV'],
	'HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v2': ['BTagCSV'],
	'HLT_ZeroBias_v4': ['ZeroBias']
}

triggersGroupMap = {
        'HLT_DiPFJetAve80_v5': ['null'],
	'HLT_PFJet80_v5': ['null'],
	'HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v2': ['null'],
	'HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v2': ['null'],
	'HLT_ZeroBias_v4': ['null']
}

datasetStreamMap = {
	'HcalHPDNoise': ['PhysicsEGammaCommissioning'],
	'ScoutingCaloCommissioning': ['ScoutingCalo'],
	'JetHT': ['PhysicsHadronsTaus'],
	'ParkingHT500to550': ['Parking'],
	'ParkingHT470to500': ['Parking'],
	'HTMHT': ['PhysicsHadronsTaus'],
	'NoBPTX': ['PhysicsEGammaCommissioning'],
	'SingleElectron': ['PhysicsEGammaCommissioning'],
	'DoubleMuon': ['PhysicsMuons'],
	'MuOnia': ['PhysicsMuons'],
	'ParkingScoutingMonitor': ['PhysicsParkingScoutingMonitor'],
	'AlCaElectron': ['ALCAELECTRON'],
	'ScoutingPFCommissioning': ['ScoutingPF'],
	'RPCMonitor': ['RPCMON'],
	'FSQJets': ['PhysicsEGammaCommissioning'],
	'BTagCSV': ['PhysicsHadronsTaus'],
	'HcalNZS': ['PhysicsEGammaCommissioning'],
	'BTagMu': ['PhysicsHadronsTaus'],
	'MonteCarlo': ['PhysicsEGammaCommissioning'],
	'HINCaloJets': ['PhysicsEndOfFill'],
	'MuonEG': ['PhysicsMuons'],
	'ParkingHT650': ['Parking'],
	'HighMultiplicity85EOF': ['PhysicsEndOfFill'],
	'HLTPhysics': ['PhysicsEGammaCommissioning'],
	'HighMultiplicityEOF': ['PhysicsEndOfFill'],
	'ParkingHT550to650': ['Parking'],
	'ScoutingCaloHT': ['ScoutingCalo'],
	'DoubleMuonLowMass': ['PhysicsMuons'],
	'SinglePhoton': ['PhysicsEGammaCommissioning'],
	'SingleMuon': ['PhysicsMuons'],
	'DisplacedJet': ['PhysicsHadronsTaus'],
	'ZeroBias': ['PhysicsEGammaCommissioning'],
	'HINPhoton': ['PhysicsEndOfFill'],
	'HINPFJets': ['PhysicsEndOfFill'],
	'ParkingHT450to470': ['Parking'],
	'L1MinimumBias': ['PhysicsEGammaCommissioning'],
	'AlCaPhiSym': ['ALCAPHISYM'],
	'Tau': ['PhysicsHadronsTaus'],
	'AlCaP0': ['ALCAP0'],
	'Charmonium': ['PhysicsMuons'],
	'ParkingHT430to450': ['Parking'],
	'AlCaLumiPixels': ['ALCALUMIPIXELS'],
	'MET': ['PhysicsHadronsTaus'],
	'ParkingHT410to430': ['Parking'],
	'DoubleEG': ['PhysicsEGammaCommissioning'],
	'Commissioning': ['PhysicsEGammaCommissioning'],
	'ScoutingPFMuons': ['ScoutingPF'],
	'ScoutingPFHT': ['ScoutingPF']
}

triggersToRemove = [
    ## not in stream A
    'HLT_EcalCalibration_v',
    
    # use UTCA (not simulated in MC)
    'HLT_HcalUTCA_v',
    
    # use NZS (not simulated in MC)
    'HLT_HcalPhiSym_v',
    'HLT_HcalNZS_v',
    
    # fake triggers
    'HLT_BCToEFilter_v',
    'HLT_RemovePileUpDominatedEventsGen_v',
    'HLT_RemovePileUpDominatedEvents_v',
    'HLT_EmFilter_v',
    'HLT_EmGlobalFilter_v',
    'HLT_MuFilter_v',
    'HLT_MuFilterTP_v',

    # trigger without L1 seeds
    'HLT_Random_v',
    'HLT_Physics_v',
]

#triggersGroupMap = dict(triggersGroupMap.items() + triggersL1GroupMap.items())

triggerList = []
L1List = []
HLTList = []
#twoHLTsList = []
primaryDatasetList = []
groupList = []
twoDatasetsList = []
getTriggerString = {}

## Fill triggerList and groupList and datasetList
for trigger in triggersDatasetMap.keys(): 
    #if trigger[:-1] in triggersToRemove: continue
    if not (trigger in triggerList) : triggerList.append(trigger) 
    for group in triggersGroupMap[trigger]: 
        if not group in groupList: groupList.append(group)
    for dataset in triggersDatasetMap[trigger]:
        if not dataset in primaryDatasetList: primaryDatasetList.append(dataset)

## Fill HLTList and L1List
for trigger in triggerList:
    if "HLT_" in trigger: HLTList.append(trigger)
#    elif "L1_" in trigger: L1List.append(trigger)

## Fill getTriggerString get a map from trigger and group names to strings
#for trigger in triggerList:
#    getTriggerString[trigger]=trigger
#    for dataset in triggersDatasetMap[trigger]:
#        if dataset in getTriggerString.keys(): getTriggerString[dataset]+='||'+trigger
#        else: getTriggerString[dataset]=trigger
#    for group in triggersGroupMap[trigger]:
#        if group in getTriggerString.keys(): getTriggerString[group]+='||'+trigger
#        else: getTriggerString[group]=trigger

## Aliases
groupAliasCounter = {}
datasetAliasCounter = {}
for trigger in triggerList:
    getTriggerString[trigger]=trigger
    for group in triggersGroupMap[trigger]:
        if (group != "L1") and (group != "Masked") and not group.isdigit():
            if group in getTriggerString.keys():
                groupAliasCounter[group] += 1
                getTriggerString[group]+='||'+group+"_"+str(groupAliasCounter[group])
            else:
                groupAliasCounter[group] = 0
                getTriggerString[group]=group+"_0"
        elif (group == "Masked"):
            if group in getTriggerString.keys(): getTriggerString[group]+='||'+trigger
            else: getTriggerString[group]=trigger
    for dataset in triggersDatasetMap[trigger]:
        if dataset in getTriggerString.keys(): 
            datasetAliasCounter[dataset] += 1
            getTriggerString[dataset]+='||'+dataset+"_"+str(datasetAliasCounter[dataset])
        else:
            datasetAliasCounter[dataset] = 0
            getTriggerString[dataset]=dataset+"_0"

## Fill twoGroupsList and getTriggerString
#for group1 in groupList:
#    for group2 in groupList:
#        if (not group1.isdigit()) and (not group2.isdigit()): twoGroups = group1 + "-" + group2
#        if not (twoGroups in twoGroupsList) and ("L1" not in twoGroups):
#            twoGroupsList.append(twoGroups)
#            twoGroupsTrigger="("+(getTriggerString[group1])+")&&("+(getTriggerString[group2])+")"
#            getTriggerString[twoGroups]=twoGroupsTrigger

### Fill twoHLTsList and getTriggerString
#for trigger1 in HLTList:
#    for trigger2 in HLTList:
#        twoHLTs = trigger1 + "-" + trigger2
#        if not (twoHLTs in twoHLTsList):
#            twoHLTsList.append(twoHLTs)
#            twoHLTsTrigger="("+(getTriggerString[trigger1])+")&&("+(getTriggerString[trigger2])+")"
#            getTriggerString[twoHLTs]=twoHLTsTrigger

## Fill string for All group
#primaryDatasetList.append('All_HLT')
groupList.append('All_HLT')
i = 0
for trigger in HLTList:
    if 'All_HLT' in getTriggerString.keys(): getTriggerString['All_HLT']+='||All_HLT_'+str(i)
    else: getTriggerString['All_HLT']='All_HLT_0'
    i += 1

## Creates the global OR string fot all L1 paths 
#i = 0
#for trigger in L1List:
#    if 'L1' in getTriggerString.keys(): getTriggerString['L1']+='||L1_'+str(i)
#    else: getTriggerString['L1']='L1_0'
#    i += 1



