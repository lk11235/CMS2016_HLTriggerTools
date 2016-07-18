ALL_COMMONRULES += src_Configuration_Skimming_test
src_Configuration_Skimming_test_parent := Configuration/Skimming
src_Configuration_Skimming_test_INIT_FUNC += $$(eval $$(call CommonProductRules,src_Configuration_Skimming_test,src/Configuration/Skimming/test,TEST))
