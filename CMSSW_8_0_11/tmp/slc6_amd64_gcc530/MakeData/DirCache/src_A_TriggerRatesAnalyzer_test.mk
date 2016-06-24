ALL_COMMONRULES += src_A_TriggerRatesAnalyzer_test
src_A_TriggerRatesAnalyzer_test_parent := A/TriggerRatesAnalyzer
src_A_TriggerRatesAnalyzer_test_INIT_FUNC += $$(eval $$(call CommonProductRules,src_A_TriggerRatesAnalyzer_test,src/A/TriggerRatesAnalyzer/test,TEST))
