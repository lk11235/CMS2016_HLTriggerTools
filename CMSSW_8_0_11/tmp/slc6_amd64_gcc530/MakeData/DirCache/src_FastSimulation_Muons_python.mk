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
