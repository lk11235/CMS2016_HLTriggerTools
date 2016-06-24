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
