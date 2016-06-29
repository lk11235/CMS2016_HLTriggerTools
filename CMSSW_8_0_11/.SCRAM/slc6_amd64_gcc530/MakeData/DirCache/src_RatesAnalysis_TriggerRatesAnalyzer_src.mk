ifeq ($(strip $(RatesAnalysis/TriggerRatesAnalyzer)),)
ALL_COMMONRULES += src_RatesAnalysis_TriggerRatesAnalyzer_src
src_RatesAnalysis_TriggerRatesAnalyzer_src_parent := RatesAnalysis/TriggerRatesAnalyzer
src_RatesAnalysis_TriggerRatesAnalyzer_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_RatesAnalysis_TriggerRatesAnalyzer_src,src/RatesAnalysis/TriggerRatesAnalyzer/src,LIBRARY))
RatesAnalysisTriggerRatesAnalyzer := self/RatesAnalysis/TriggerRatesAnalyzer
RatesAnalysis/TriggerRatesAnalyzer := RatesAnalysisTriggerRatesAnalyzer
RatesAnalysisTriggerRatesAnalyzer_files := $(patsubst src/RatesAnalysis/TriggerRatesAnalyzer/src/%,%,$(wildcard $(foreach dir,src/RatesAnalysis/TriggerRatesAnalyzer/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
RatesAnalysisTriggerRatesAnalyzer_BuildFile    := $(WORKINGDIR)/cache/bf/src/RatesAnalysis/TriggerRatesAnalyzer/BuildFile
RatesAnalysisTriggerRatesAnalyzer_LOC_USE := self  DataFormats/Candidate DataFormats/Common DataFormats/EgammaCandidates DataFormats/HepMCCandidate DataFormats/HLTReco DataFormats/JetReco DataFormats/L1GlobalTrigger DataFormats/L1Trigger DataFormats/METReco DataFormats/MuonReco DQMServices/Core FWCore/Framework FWCore/MessageLogger FWCore/ParameterSet FWCore/ServiceRegistry HLTrigger/HLTcore rootgraphics
RatesAnalysisTriggerRatesAnalyzer_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,RatesAnalysisTriggerRatesAnalyzer,RatesAnalysisTriggerRatesAnalyzer,$(SCRAMSTORENAME_LIB),src/RatesAnalysis/TriggerRatesAnalyzer/src))
RatesAnalysisTriggerRatesAnalyzer_PACKAGE := self/src/RatesAnalysis/TriggerRatesAnalyzer/src
ALL_PRODS += RatesAnalysisTriggerRatesAnalyzer
RatesAnalysisTriggerRatesAnalyzer_CLASS := LIBRARY
RatesAnalysis/TriggerRatesAnalyzer_forbigobj+=RatesAnalysisTriggerRatesAnalyzer
RatesAnalysisTriggerRatesAnalyzer_INIT_FUNC        += $$(eval $$(call Library,RatesAnalysisTriggerRatesAnalyzer,src/RatesAnalysis/TriggerRatesAnalyzer/src,src_RatesAnalysis_TriggerRatesAnalyzer_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
