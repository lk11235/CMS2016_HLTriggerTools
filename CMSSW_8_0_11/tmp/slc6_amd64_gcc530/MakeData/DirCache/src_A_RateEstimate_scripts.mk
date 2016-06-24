src_A_RateEstimate_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/A/RateEstimate/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_A_RateEstimate_scripts,src/A/RateEstimate/scripts,$(SCRAMSTORENAME_BIN),*))
