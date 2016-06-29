ALL_COMMONRULES += src_HLTrigger_HLTanalyzers_test
src_HLTrigger_HLTanalyzers_test_parent := HLTrigger/HLTanalyzers
src_HLTrigger_HLTanalyzers_test_INIT_FUNC += $$(eval $$(call CommonProductRules,src_HLTrigger_HLTanalyzers_test,src/HLTrigger/HLTanalyzers/test,TEST))
