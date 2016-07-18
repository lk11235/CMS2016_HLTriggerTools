src_RatesAnalysis_RateEstimate_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/RatesAnalysis/RateEstimate/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_RatesAnalysis_RateEstimate_scripts,src/RatesAnalysis/RateEstimate/scripts,$(SCRAMSTORENAME_BIN),*))
