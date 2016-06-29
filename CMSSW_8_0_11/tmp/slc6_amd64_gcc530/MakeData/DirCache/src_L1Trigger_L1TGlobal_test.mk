ALL_COMMONRULES += src_L1Trigger_L1TGlobal_test
src_L1Trigger_L1TGlobal_test_parent := L1Trigger/L1TGlobal
src_L1Trigger_L1TGlobal_test_INIT_FUNC += $$(eval $$(call CommonProductRules,src_L1Trigger_L1TGlobal_test,src/L1Trigger/L1TGlobal/test,TEST))
