ifeq ($(strip $(PyConfigurationAlCa)),)
PyConfigurationAlCa := self/src/Configuration/AlCa/python
src_Configuration_AlCa_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/Configuration/AlCa/python)
PyConfigurationAlCa_files := $(patsubst src/Configuration/AlCa/python/%,%,$(wildcard $(foreach dir,src/Configuration/AlCa/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyConfigurationAlCa_LOC_USE := self  
PyConfigurationAlCa_PACKAGE := self/src/Configuration/AlCa/python
ALL_PRODS += PyConfigurationAlCa
PyConfigurationAlCa_INIT_FUNC        += $$(eval $$(call PythonProduct,PyConfigurationAlCa,src/Configuration/AlCa/python,src_Configuration_AlCa_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyConfigurationAlCa,src/Configuration/AlCa/python))
endif
ALL_COMMONRULES += src_Configuration_AlCa_python
src_Configuration_AlCa_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_Configuration_AlCa_python,src/Configuration/AlCa/python,PYTHON))
