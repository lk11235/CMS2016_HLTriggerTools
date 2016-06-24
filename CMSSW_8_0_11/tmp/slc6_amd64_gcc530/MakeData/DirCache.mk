ALL_SUBSYSTEMS+=Configuration
subdirs_src_Configuration = src_Configuration_HLT src_Configuration_AlCa src_Configuration_Skimming
ALL_PACKAGES += Configuration/AlCa
subdirs_src_Configuration_AlCa := src_Configuration_AlCa_doc src_Configuration_AlCa_python
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
ALL_PACKAGES += Configuration/HLT
subdirs_src_Configuration_HLT := src_Configuration_HLT_python
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
ALL_PACKAGES += Configuration/Skimming
subdirs_src_Configuration_Skimming := src_Configuration_Skimming_python src_Configuration_Skimming_src src_Configuration_Skimming_test
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
ALL_COMMONRULES += src_Configuration_Skimming_test
src_Configuration_Skimming_test_parent := Configuration/Skimming
src_Configuration_Skimming_test_INIT_FUNC += $$(eval $$(call CommonProductRules,src_Configuration_Skimming_test,src/Configuration/Skimming/test,TEST))
ALL_SUBSYSTEMS+=FastSimulation
subdirs_src_FastSimulation = src_FastSimulation_Muons
ALL_PACKAGES += FastSimulation/Muons
subdirs_src_FastSimulation_Muons := src_FastSimulation_Muons_data src_FastSimulation_Muons_plugins src_FastSimulation_Muons_python
ifeq ($(strip $(PyFastSimulationMuons)),)
PyFastSimulationMuons := self/src/FastSimulation/Muons/python
src_FastSimulation_Muons_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/FastSimulation/Muons/python)
PyFastSimulationMuons_files := $(patsubst src/FastSimulation/Muons/python/%,%,$(wildcard $(foreach dir,src/FastSimulation/Muons/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyFastSimulationMuons_LOC_USE := self  
PyFastSimulationMuons_PACKAGE := self/src/FastSimulation/Muons/python
ALL_PRODS += PyFastSimulationMuons
PyFastSimulationMuons_INIT_FUNC        += $$(eval $$(call PythonProduct,PyFastSimulationMuons,src/FastSimulation/Muons/python,src_FastSimulation_Muons_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyFastSimulationMuons,src/FastSimulation/Muons/python))
endif
ALL_COMMONRULES += src_FastSimulation_Muons_python
src_FastSimulation_Muons_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_FastSimulation_Muons_python,src/FastSimulation/Muons/python,PYTHON))
ALL_SUBSYSTEMS+=HLTrigger
subdirs_src_HLTrigger = src_HLTrigger_Configuration src_HLTrigger_HLTanalyzers
ALL_PACKAGES += HLTrigger/Configuration
subdirs_src_HLTrigger_Configuration := src_HLTrigger_Configuration_doc src_HLTrigger_Configuration_python src_HLTrigger_Configuration_scripts src_HLTrigger_Configuration_tables src_HLTrigger_Configuration_test
ifeq ($(strip $(PyHLTriggerConfiguration)),)
PyHLTriggerConfiguration := self/src/HLTrigger/Configuration/python
src_HLTrigger_Configuration_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/HLTrigger/Configuration/python)
PyHLTriggerConfiguration_files := $(patsubst src/HLTrigger/Configuration/python/%,%,$(wildcard $(foreach dir,src/HLTrigger/Configuration/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyHLTriggerConfiguration_LOC_USE := self  
PyHLTriggerConfiguration_PACKAGE := self/src/HLTrigger/Configuration/python
ALL_PRODS += PyHLTriggerConfiguration
PyHLTriggerConfiguration_INIT_FUNC        += $$(eval $$(call PythonProduct,PyHLTriggerConfiguration,src/HLTrigger/Configuration/python,src_HLTrigger_Configuration_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyHLTriggerConfiguration,src/HLTrigger/Configuration/python))
endif
ALL_COMMONRULES += src_HLTrigger_Configuration_python
src_HLTrigger_Configuration_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_HLTrigger_Configuration_python,src/HLTrigger/Configuration/python,PYTHON))
src_HLTrigger_Configuration_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/HLTrigger/Configuration/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_HLTrigger_Configuration_scripts,src/HLTrigger/Configuration/scripts,$(SCRAMSTORENAME_BIN),*))
ALL_COMMONRULES += src_HLTrigger_Configuration_test
src_HLTrigger_Configuration_test_parent := HLTrigger/Configuration
src_HLTrigger_Configuration_test_INIT_FUNC += $$(eval $$(call CommonProductRules,src_HLTrigger_Configuration_test,src/HLTrigger/Configuration/test,TEST))
ALL_PACKAGES += HLTrigger/HLTanalyzers
subdirs_src_HLTrigger_HLTanalyzers := src_HLTrigger_HLTanalyzers_python src_HLTrigger_HLTanalyzers_src src_HLTrigger_HLTanalyzers_test
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
ALL_COMMONRULES += src_HLTrigger_HLTanalyzers_test
src_HLTrigger_HLTanalyzers_test_parent := HLTrigger/HLTanalyzers
src_HLTrigger_HLTanalyzers_test_INIT_FUNC += $$(eval $$(call CommonProductRules,src_HLTrigger_HLTanalyzers_test,src/HLTrigger/HLTanalyzers/test,TEST))
ALL_SUBSYSTEMS+=L1Trigger
subdirs_src_L1Trigger = src_L1Trigger_L1TGlobal
ALL_PACKAGES += L1Trigger/L1TGlobal
subdirs_src_L1Trigger_L1TGlobal := src_L1Trigger_L1TGlobal_data src_L1Trigger_L1TGlobal_interface src_L1Trigger_L1TGlobal_plugins src_L1Trigger_L1TGlobal_python src_L1Trigger_L1TGlobal_scripts src_L1Trigger_L1TGlobal_src src_L1Trigger_L1TGlobal_test
ifeq ($(strip $(PyL1TriggerL1TGlobal)),)
PyL1TriggerL1TGlobal := self/src/L1Trigger/L1TGlobal/python
src_L1Trigger_L1TGlobal_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/L1Trigger/L1TGlobal/python)
PyL1TriggerL1TGlobal_files := $(patsubst src/L1Trigger/L1TGlobal/python/%,%,$(wildcard $(foreach dir,src/L1Trigger/L1TGlobal/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyL1TriggerL1TGlobal_LOC_USE := self  
PyL1TriggerL1TGlobal_PACKAGE := self/src/L1Trigger/L1TGlobal/python
ALL_PRODS += PyL1TriggerL1TGlobal
PyL1TriggerL1TGlobal_INIT_FUNC        += $$(eval $$(call PythonProduct,PyL1TriggerL1TGlobal,src/L1Trigger/L1TGlobal/python,src_L1Trigger_L1TGlobal_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyL1TriggerL1TGlobal,src/L1Trigger/L1TGlobal/python))
endif
ALL_COMMONRULES += src_L1Trigger_L1TGlobal_python
src_L1Trigger_L1TGlobal_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_L1Trigger_L1TGlobal_python,src/L1Trigger/L1TGlobal/python,PYTHON))
src_L1Trigger_L1TGlobal_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/L1Trigger/L1TGlobal/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_L1Trigger_L1TGlobal_scripts,src/L1Trigger/L1TGlobal/scripts,$(SCRAMSTORENAME_BIN),*))
ALL_COMMONRULES += src_L1Trigger_L1TGlobal_test
src_L1Trigger_L1TGlobal_test_parent := L1Trigger/L1TGlobal
src_L1Trigger_L1TGlobal_test_INIT_FUNC += $$(eval $$(call CommonProductRules,src_L1Trigger_L1TGlobal_test,src/L1Trigger/L1TGlobal/test,TEST))
