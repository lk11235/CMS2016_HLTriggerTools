ifeq ($(strip $(PyConfigurationHLT)),)
PyConfigurationHLT := self/src/Configuration/HLT/python
src_Configuration_HLT_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/Configuration/HLT/python)
PyConfigurationHLT_files := $(patsubst src/Configuration/HLT/python/%,%,$(wildcard $(foreach dir,src/Configuration/HLT/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyConfigurationHLT_LOC_USE := self  
PyConfigurationHLT_PACKAGE := self/src/Configuration/HLT/python
ALL_PRODS += PyConfigurationHLT
PyConfigurationHLT_INIT_FUNC        += $$(eval $$(call PythonProduct,PyConfigurationHLT,src/Configuration/HLT/python,src_Configuration_HLT_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyConfigurationHLT,src/Configuration/HLT/python))
endif
ALL_COMMONRULES += src_Configuration_HLT_python
src_Configuration_HLT_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_Configuration_HLT_python,src/Configuration/HLT/python,PYTHON))
