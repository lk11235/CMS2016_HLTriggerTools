src_L1Trigger_L1TGlobal_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/L1Trigger/L1TGlobal/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_L1Trigger_L1TGlobal_scripts,src/L1Trigger/L1TGlobal/scripts,$(SCRAMSTORENAME_BIN),*))
