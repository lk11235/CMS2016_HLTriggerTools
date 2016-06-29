ifeq ($(strip $(PyConfigurationSkimming)),)
PyConfigurationSkimming := self/src/Configuration/Skimming/python
src_Configuration_Skimming_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/Configuration/Skimming/python)
PyConfigurationSkimming_files := $(patsubst src/Configuration/Skimming/python/%,%,$(wildcard $(foreach dir,src/Configuration/Skimming/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyConfigurationSkimming_LOC_USE := self  
PyConfigurationSkimming_PACKAGE := self/src/Configuration/Skimming/python
ALL_PRODS += PyConfigurationSkimming
PyConfigurationSkimming_INIT_FUNC        += $$(eval $$(call PythonProduct,PyConfigurationSkimming,src/Configuration/Skimming/python,src_Configuration_Skimming_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyConfigurationSkimming,src/Configuration/Skimming/python))
endif
ALL_COMMONRULES += src_Configuration_Skimming_python
src_Configuration_Skimming_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_Configuration_Skimming_python,src/Configuration/Skimming/python,PYTHON))
