ifeq ($(strip $(Configuration/Skimming)),)
ALL_COMMONRULES += src_Configuration_Skimming_src
src_Configuration_Skimming_src_parent := Configuration/Skimming
src_Configuration_Skimming_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_Configuration_Skimming_src,src/Configuration/Skimming/src,LIBRARY))
ConfigurationSkimming := self/Configuration/Skimming
Configuration/Skimming := ConfigurationSkimming
ConfigurationSkimming_files := $(patsubst src/Configuration/Skimming/src/%,%,$(wildcard $(foreach dir,src/Configuration/Skimming/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
ConfigurationSkimming_BuildFile    := $(WORKINGDIR)/cache/bf/src/Configuration/Skimming/BuildFile
ConfigurationSkimming_LOC_USE := self  FWCore/Framework FWCore/PluginManager FWCore/ParameterSet FWCore/Common DataFormats/EgammaCandidates DataFormats/MuonReco DataFormats/JetReco DataFormats/Common Geometry/CaloTopology Geometry/Records RecoEcal/EgammaCoreTools RecoJets/JetAlgorithms HLTrigger/HLTcore
ConfigurationSkimming_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,ConfigurationSkimming,ConfigurationSkimming,$(SCRAMSTORENAME_LIB),src/Configuration/Skimming/src))
ConfigurationSkimming_PACKAGE := self/src/Configuration/Skimming/src
ALL_PRODS += ConfigurationSkimming
ConfigurationSkimming_CLASS := LIBRARY
Configuration/Skimming_forbigobj+=ConfigurationSkimming
ConfigurationSkimming_INIT_FUNC        += $$(eval $$(call Library,ConfigurationSkimming,src/Configuration/Skimming/src,src_Configuration_Skimming_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
ifeq ($(strip $(FastSimulationMuonsPlugins)),)
FastSimulationMuonsPlugins := self/src/FastSimulation/Muons/plugins
PLUGINS:=yes
FastSimulationMuonsPlugins_files := $(patsubst src/FastSimulation/Muons/plugins/%,%,$(foreach file,*.cc,$(eval xfile:=$(wildcard src/FastSimulation/Muons/plugins/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/FastSimulation/Muons/plugins/$(file). Please fix src/FastSimulation/Muons/plugins/BuildFile.))))
FastSimulationMuonsPlugins_BuildFile    := $(WORKINGDIR)/cache/bf/src/FastSimulation/Muons/plugins/BuildFile
FastSimulationMuonsPlugins_LOC_USE := self  CondFormats/DataRecord CondFormats/L1TObjects DataFormats/L1GlobalMuonTrigger DataFormats/L1Trigger DataFormats/Math DataFormats/MuonSeed DataFormats/TrackReco DataFormats/TrackerRecHit2D DataFormats/TrajectorySeed FWCore/Framework FWCore/MessageLogger FWCore/ParameterSet FWCore/PluginManager FWCore/ServiceRegistry FWCore/Utilities FastSimDataFormats/L1GlobalMuonTrigger FastSimulation/Tracking FastSimulation/Utilities Geometry/RPCGeometry RecoMuon/GlobalTrackingTools RecoMuon/L3TrackFinder RecoMuon/TrackerSeedGenerator RecoMuon/TrackingTools RecoTracker/TkTrackingRegions SimDataFormats/Track TrackingTools/DetLayers TrackingTools/PatternTools Utilities/General
FastSimulationMuonsPlugins_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,FastSimulationMuonsPlugins,FastSimulationMuonsPlugins,$(SCRAMSTORENAME_LIB),src/FastSimulation/Muons/plugins))
FastSimulationMuonsPlugins_PACKAGE := self/src/FastSimulation/Muons/plugins
ALL_PRODS += FastSimulationMuonsPlugins
FastSimulation/Muons_forbigobj+=FastSimulationMuonsPlugins
FastSimulationMuonsPlugins_INIT_FUNC        += $$(eval $$(call Library,FastSimulationMuonsPlugins,src/FastSimulation/Muons/plugins,src_FastSimulation_Muons_plugins,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
FastSimulationMuonsPlugins_CLASS := LIBRARY
else
$(eval $(call MultipleWarningMsg,FastSimulationMuonsPlugins,src/FastSimulation/Muons/plugins))
endif
ALL_COMMONRULES += src_FastSimulation_Muons_plugins
src_FastSimulation_Muons_plugins_parent := FastSimulation/Muons
src_FastSimulation_Muons_plugins_INIT_FUNC += $$(eval $$(call CommonProductRules,src_FastSimulation_Muons_plugins,src/FastSimulation/Muons/plugins,PLUGINS))
ifeq ($(strip $(HLTrigger/HLTanalyzers)),)
ALL_COMMONRULES += src_HLTrigger_HLTanalyzers_src
src_HLTrigger_HLTanalyzers_src_parent := HLTrigger/HLTanalyzers
src_HLTrigger_HLTanalyzers_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_HLTrigger_HLTanalyzers_src,src/HLTrigger/HLTanalyzers/src,LIBRARY))
HLTriggerHLTanalyzers := self/HLTrigger/HLTanalyzers
HLTrigger/HLTanalyzers := HLTriggerHLTanalyzers
HLTriggerHLTanalyzers_files := $(patsubst src/HLTrigger/HLTanalyzers/src/%,%,$(wildcard $(foreach dir,src/HLTrigger/HLTanalyzers/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
HLTriggerHLTanalyzers_BuildFile    := $(WORKINGDIR)/cache/bf/src/HLTrigger/HLTanalyzers/BuildFile
HLTriggerHLTanalyzers_LOC_USE := self  CondFormats/DataRecord CondFormats/L1TObjects DataFormats/L1TGlobal DataFormats/BTauReco DataFormats/CSCDigi DataFormats/CaloTowers DataFormats/Candidate DataFormats/Common DataFormats/DTDigi DataFormats/EcalDigi DataFormats/EgammaCandidates DataFormats/EgammaReco DataFormats/FEDRawData DataFormats/GeometryVector DataFormats/HcalDigi DataFormats/JetReco DataFormats/L1CaloTrigger DataFormats/L1GlobalCaloTrigger DataFormats/L1GlobalMuonTrigger DataFormats/L1GlobalTrigger DataFormats/L1Trigger DataFormats/METReco DataFormats/MuonData DataFormats/MuonReco DataFormats/RPCDigi DataFormats/RecoCandidate DataFormats/SiPixelDigi DataFormats/SiStripDigi DataFormats/TauReco DataFormats/TrackReco DataFormats/TrajectorySeed DataFormats/HeavyIonEvent DataFormats/Luminosity SimDataFormats/HiGenData FWCore/Framework FWCore/MessageLogger FWCore/ParameterSet FWCore/PluginManager Geometry/CaloGeometry Geometry/CommonDetUnit Geometry/Records Geometry/EcalMapping HLTrigger/HLTcore L1Trigger/RegionalCaloTrigger MagneticField/Engine MagneticField/Records SimDataFormats/GeneratorProducts SimDataFormats/Track SimDataFormats/Vertex TrackingTools/TrajectoryState RecoEcal/EgammaCoreTools RecoEgamma/EgammaTools RecoHI/HiEgammaAlgos RecoJets/JetProducers RecoLuminosity/LumiProducer TrackingTools/TransientTrack DQMServices/Core rootcore
HLTriggerHLTanalyzers_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,HLTriggerHLTanalyzers,HLTriggerHLTanalyzers,$(SCRAMSTORENAME_LIB),src/HLTrigger/HLTanalyzers/src))
HLTriggerHLTanalyzers_PACKAGE := self/src/HLTrigger/HLTanalyzers/src
ALL_PRODS += HLTriggerHLTanalyzers
HLTriggerHLTanalyzers_CLASS := LIBRARY
HLTrigger/HLTanalyzers_forbigobj+=HLTriggerHLTanalyzers
HLTriggerHLTanalyzers_INIT_FUNC        += $$(eval $$(call Library,HLTriggerHLTanalyzers,src/HLTrigger/HLTanalyzers/src,src_HLTrigger_HLTanalyzers_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
ifeq ($(strip $(L1TriggerL1TGlobalPlugins)),)
L1TriggerL1TGlobalPlugins := self/src/L1Trigger/L1TGlobal/plugins
PLUGINS:=yes
L1TriggerL1TGlobalPlugins_files := $(patsubst src/L1Trigger/L1TGlobal/plugins/%,%,$(foreach file,*.cc,$(eval xfile:=$(wildcard src/L1Trigger/L1TGlobal/plugins/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/L1Trigger/L1TGlobal/plugins/$(file). Please fix src/L1Trigger/L1TGlobal/plugins/BuildFile.))))
L1TriggerL1TGlobalPlugins_BuildFile    := $(WORKINGDIR)/cache/bf/src/L1Trigger/L1TGlobal/plugins/BuildFile
L1TriggerL1TGlobalPlugins_LOC_USE := self  FWCore/Framework FWCore/PluginManager FWCore/ParameterSet DataFormats/L1Trigger CondFormats/L1TObjects CondFormats/DataRecord CondTools/L1Trigger xerces-c utm L1TriggerConfig/L1GtConfigProducers L1Trigger/L1TGlobal L1Trigger/GlobalTrigger
L1TriggerL1TGlobalPlugins_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,L1TriggerL1TGlobalPlugins,L1TriggerL1TGlobalPlugins,$(SCRAMSTORENAME_LIB),src/L1Trigger/L1TGlobal/plugins))
L1TriggerL1TGlobalPlugins_PACKAGE := self/src/L1Trigger/L1TGlobal/plugins
ALL_PRODS += L1TriggerL1TGlobalPlugins
L1Trigger/L1TGlobal_forbigobj+=L1TriggerL1TGlobalPlugins
L1TriggerL1TGlobalPlugins_INIT_FUNC        += $$(eval $$(call Library,L1TriggerL1TGlobalPlugins,src/L1Trigger/L1TGlobal/plugins,src_L1Trigger_L1TGlobal_plugins,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
L1TriggerL1TGlobalPlugins_CLASS := LIBRARY
else
$(eval $(call MultipleWarningMsg,L1TriggerL1TGlobalPlugins,src/L1Trigger/L1TGlobal/plugins))
endif
ALL_COMMONRULES += src_L1Trigger_L1TGlobal_plugins
src_L1Trigger_L1TGlobal_plugins_parent := L1Trigger/L1TGlobal
src_L1Trigger_L1TGlobal_plugins_INIT_FUNC += $$(eval $$(call CommonProductRules,src_L1Trigger_L1TGlobal_plugins,src/L1Trigger/L1TGlobal/plugins,PLUGINS))
ifeq ($(strip $(L1Trigger/L1TGlobal)),)
ALL_COMMONRULES += src_L1Trigger_L1TGlobal_src
src_L1Trigger_L1TGlobal_src_parent := L1Trigger/L1TGlobal
src_L1Trigger_L1TGlobal_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_L1Trigger_L1TGlobal_src,src/L1Trigger/L1TGlobal/src,LIBRARY))
L1TriggerL1TGlobal := self/L1Trigger/L1TGlobal
L1Trigger/L1TGlobal := L1TriggerL1TGlobal
L1TriggerL1TGlobal_files := $(patsubst src/L1Trigger/L1TGlobal/src/%,%,$(wildcard $(foreach dir,src/L1Trigger/L1TGlobal/src src/L1Trigger/L1TGlobal/src/L1TMenuEditor src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/compilers src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/compilers/vc-7 src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/compilers/vc-8 src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/parser src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/parser/expat src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/parser/non-validating src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/parser/validating src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/parser/xerces src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/tree src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/tree/bits src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/tree/parsing src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/tree/serialization src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/xml src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/xml/bits src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/xml/dom src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/xml/dom/bits src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/xml/sax src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/xml/sax/bits,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
L1TriggerL1TGlobal_BuildFile    := $(WORKINGDIR)/cache/bf/src/L1Trigger/L1TGlobal/src/BuildFile
L1TriggerL1TGlobal_LOC_USE := self  FWCore/Framework FWCore/PluginManager FWCore/ParameterSet DataFormats/L1TCalorimeter DataFormats/L1TGlobal CondFormats/L1TObjects CondFormats/DataRecord xerces-c
L1TriggerL1TGlobal_LCGDICTS  := x 
L1TriggerL1TGlobal_PRE_INIT_FUNC += $$(eval $$(call LCGDict,L1TriggerL1TGlobal,src/L1Trigger/L1TGlobal/src/classes.h,src/L1Trigger/L1TGlobal/src/classes_def.xml,$(SCRAMSTORENAME_LIB),$(GENREFLEX_ARGS) --fail_on_warnings,))
L1TriggerL1TGlobal_EX_LIB   := L1TriggerL1TGlobal
L1TriggerL1TGlobal_EX_USE   := $(foreach d,$(L1TriggerL1TGlobal_LOC_USE),$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
L1TriggerL1TGlobal_PACKAGE := self/src/L1Trigger/L1TGlobal/src
ALL_PRODS += L1TriggerL1TGlobal
L1TriggerL1TGlobal_CLASS := LIBRARY
L1Trigger/L1TGlobal_forbigobj+=L1TriggerL1TGlobal
L1TriggerL1TGlobal_INIT_FUNC        += $$(eval $$(call Library,L1TriggerL1TGlobal,src/L1Trigger/L1TGlobal/src,src_L1Trigger_L1TGlobal_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
