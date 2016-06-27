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
ifeq ($(strip $(A/TriggerRatesAnalyzer)),)
ALL_COMMONRULES += src_A_TriggerRatesAnalyzer_src
src_A_TriggerRatesAnalyzer_src_parent := A/TriggerRatesAnalyzer
src_A_TriggerRatesAnalyzer_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_A_TriggerRatesAnalyzer_src,src/A/TriggerRatesAnalyzer/src,LIBRARY))
ATriggerRatesAnalyzer := self/A/TriggerRatesAnalyzer
A/TriggerRatesAnalyzer := ATriggerRatesAnalyzer
ATriggerRatesAnalyzer_files := $(patsubst src/A/TriggerRatesAnalyzer/src/%,%,$(wildcard $(foreach dir,src/A/TriggerRatesAnalyzer/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
ATriggerRatesAnalyzer_BuildFile    := $(WORKINGDIR)/cache/bf/src/A/TriggerRatesAnalyzer/BuildFile
ATriggerRatesAnalyzer_LOC_USE := self  DataFormats/Candidate DataFormats/Common DataFormats/EgammaCandidates DataFormats/HepMCCandidate DataFormats/HLTReco DataFormats/JetReco DataFormats/L1GlobalTrigger DataFormats/L1Trigger DataFormats/METReco DataFormats/MuonReco DQMServices/Core FWCore/Framework FWCore/MessageLogger FWCore/ParameterSet FWCore/ServiceRegistry HLTrigger/HLTcore rootgraphics
ATriggerRatesAnalyzer_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,ATriggerRatesAnalyzer,ATriggerRatesAnalyzer,$(SCRAMSTORENAME_LIB),src/A/TriggerRatesAnalyzer/src))
ATriggerRatesAnalyzer_PACKAGE := self/src/A/TriggerRatesAnalyzer/src
ALL_PRODS += ATriggerRatesAnalyzer
ATriggerRatesAnalyzer_CLASS := LIBRARY
A/TriggerRatesAnalyzer_forbigobj+=ATriggerRatesAnalyzer
ATriggerRatesAnalyzer_INIT_FUNC        += $$(eval $$(call Library,ATriggerRatesAnalyzer,src/A/TriggerRatesAnalyzer/src,src_A_TriggerRatesAnalyzer_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
ifeq ($(strip $(GeneratorInterface/GenFilters)),)
ALL_COMMONRULES += src_GeneratorInterface_GenFilters_src
src_GeneratorInterface_GenFilters_src_parent := GeneratorInterface/GenFilters
src_GeneratorInterface_GenFilters_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_GeneratorInterface_GenFilters_src,src/GeneratorInterface/GenFilters/src,LIBRARY))
GeneratorInterfaceGenFilters := self/GeneratorInterface/GenFilters
GeneratorInterface/GenFilters := GeneratorInterfaceGenFilters
GeneratorInterfaceGenFilters_files := $(patsubst src/GeneratorInterface/GenFilters/src/%,%,$(wildcard $(foreach dir,src/GeneratorInterface/GenFilters/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
GeneratorInterfaceGenFilters_BuildFile    := $(WORKINGDIR)/cache/bf/src/GeneratorInterface/GenFilters/BuildFile
GeneratorInterfaceGenFilters_LOC_USE := self  boost FWCore/PluginManager FWCore/ParameterSet FWCore/Framework FWCore/Utilities SimDataFormats/GeneratorProducts heppdt clhep root GeneratorInterface/Pythia6Interface GeneratorInterface/Core SimGeneral/HepPDTRecord DataFormats/GeometryVector DataFormats/GeometrySurface TrackPropagation/SteppingHelixPropagator MagneticField/Records TrackingTools/TrajectoryState TrackingTools/TrajectoryParametrization TrackingTools/Records CommonTools/UtilAlgos FWCore/ServiceRegistry FastSimulation/Particle FastSimulation/BaseParticlePropagator TrackingTools/GeomPropagators DataFormats/HepMCCandidate DataFormats/JetReco DataFormats/EgammaReco
GeneratorInterfaceGenFilters_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,GeneratorInterfaceGenFilters,GeneratorInterfaceGenFilters,$(SCRAMSTORENAME_LIB),src/GeneratorInterface/GenFilters/src))
GeneratorInterfaceGenFilters_PACKAGE := self/src/GeneratorInterface/GenFilters/src
ALL_PRODS += GeneratorInterfaceGenFilters
GeneratorInterfaceGenFilters_CLASS := LIBRARY
GeneratorInterface/GenFilters_forbigobj+=GeneratorInterfaceGenFilters
GeneratorInterfaceGenFilters_INIT_FUNC        += $$(eval $$(call Library,GeneratorInterfaceGenFilters,src/GeneratorInterface/GenFilters/src,src_GeneratorInterface_GenFilters_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
ifeq ($(strip $(SimGeneralMixingModulePlugins)),)
SimGeneralMixingModulePlugins := self/src/SimGeneral/MixingModule/plugins
PLUGINS:=yes
SimGeneralMixingModulePlugins_files := $(patsubst src/SimGeneral/MixingModule/plugins/%,%,$(foreach file,*.cc,$(eval xfile:=$(wildcard src/SimGeneral/MixingModule/plugins/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/SimGeneral/MixingModule/plugins/$(file). Please fix src/SimGeneral/MixingModule/plugins/BuildFile.))))
SimGeneralMixingModulePlugins_BuildFile    := $(WORKINGDIR)/cache/bf/src/SimGeneral/MixingModule/plugins/BuildFile
SimGeneralMixingModulePlugins_LOC_USE := self  DataFormats/Common DataFormats/Provenance FWCore/Framework FWCore/MessageLogger FWCore/ParameterSet FWCore/ServiceRegistry FWCore/Utilities FWCore/PluginManager Mixing/Base SimDataFormats/CaloHit SimDataFormats/CrossingFrame SimDataFormats/Track SimDataFormats/TrackingHit SimDataFormats/Vertex SimDataFormats/GeneratorProducts SimCalorimetry/HcalSimProducers SimGeneral/MixingModule clhep CondFormats/DataRecord CondFormats/RunInfo CondCore/DBOutputService DataFormats/TrackerRecHit2D
SimGeneralMixingModulePlugins_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,SimGeneralMixingModulePlugins,SimGeneralMixingModulePlugins,$(SCRAMSTORENAME_LIB),src/SimGeneral/MixingModule/plugins))
SimGeneralMixingModulePlugins_PACKAGE := self/src/SimGeneral/MixingModule/plugins
ALL_PRODS += SimGeneralMixingModulePlugins
SimGeneral/MixingModule_forbigobj+=SimGeneralMixingModulePlugins
SimGeneralMixingModulePlugins_INIT_FUNC        += $$(eval $$(call Library,SimGeneralMixingModulePlugins,src/SimGeneral/MixingModule/plugins,src_SimGeneral_MixingModule_plugins,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
SimGeneralMixingModulePlugins_CLASS := LIBRARY
else
$(eval $(call MultipleWarningMsg,SimGeneralMixingModulePlugins,src/SimGeneral/MixingModule/plugins))
endif
ALL_COMMONRULES += src_SimGeneral_MixingModule_plugins
src_SimGeneral_MixingModule_plugins_parent := SimGeneral/MixingModule
src_SimGeneral_MixingModule_plugins_INIT_FUNC += $$(eval $$(call CommonProductRules,src_SimGeneral_MixingModule_plugins,src/SimGeneral/MixingModule/plugins,PLUGINS))
ifeq ($(strip $(SimGeneral/MixingModule)),)
ALL_COMMONRULES += src_SimGeneral_MixingModule_src
src_SimGeneral_MixingModule_src_parent := SimGeneral/MixingModule
src_SimGeneral_MixingModule_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_SimGeneral_MixingModule_src,src/SimGeneral/MixingModule/src,LIBRARY))
SimGeneralMixingModule := self/SimGeneral/MixingModule
SimGeneral/MixingModule := SimGeneralMixingModule
SimGeneralMixingModule_files := $(patsubst src/SimGeneral/MixingModule/src/%,%,$(wildcard $(foreach dir,src/SimGeneral/MixingModule/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
SimGeneralMixingModule_BuildFile    := $(WORKINGDIR)/cache/bf/src/SimGeneral/MixingModule/BuildFile
SimGeneralMixingModule_LOC_USE := self  FWCore/PluginManager FWCore/ParameterSet
SimGeneralMixingModule_EX_LIB   := SimGeneralMixingModule
SimGeneralMixingModule_EX_USE   := $(foreach d,$(SimGeneralMixingModule_LOC_USE),$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
SimGeneralMixingModule_PACKAGE := self/src/SimGeneral/MixingModule/src
ALL_PRODS += SimGeneralMixingModule
SimGeneralMixingModule_CLASS := LIBRARY
SimGeneral/MixingModule_forbigobj+=SimGeneralMixingModule
SimGeneralMixingModule_INIT_FUNC        += $$(eval $$(call Library,SimGeneralMixingModule,src/SimGeneral/MixingModule/src,src_SimGeneral_MixingModule_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
