ifeq ($(strip $(PyHLTriggerHLTanalyzers)),)
PyHLTriggerHLTanalyzers := self/src/HLTrigger/HLTanalyzers/python
src_HLTrigger_HLTanalyzers_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/HLTrigger/HLTanalyzers/python)
PyHLTriggerHLTanalyzers_files := $(patsubst src/HLTrigger/HLTanalyzers/python/%,%,$(wildcard $(foreach dir,src/HLTrigger/HLTanalyzers/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyHLTriggerHLTanalyzers_LOC_USE := self  
PyHLTriggerHLTanalyzers_PACKAGE := self/src/HLTrigger/HLTanalyzers/python
ALL_PRODS += PyHLTriggerHLTanalyzers
PyHLTriggerHLTanalyzers_INIT_FUNC        += $$(eval $$(call PythonProduct,PyHLTriggerHLTanalyzers,src/HLTrigger/HLTanalyzers/python,src_HLTrigger_HLTanalyzers_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyHLTriggerHLTanalyzers,src/HLTrigger/HLTanalyzers/python))
endif
ALL_COMMONRULES += src_HLTrigger_HLTanalyzers_python
src_HLTrigger_HLTanalyzers_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_HLTrigger_HLTanalyzers_python,src/HLTrigger/HLTanalyzers/python,PYTHON))
