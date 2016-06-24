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
