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
