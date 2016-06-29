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
