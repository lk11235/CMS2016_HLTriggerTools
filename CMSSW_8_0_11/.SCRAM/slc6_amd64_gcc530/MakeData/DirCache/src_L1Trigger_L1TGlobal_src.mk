ifeq ($(strip $(L1Trigger/L1TGlobal)),)
ALL_COMMONRULES += src_L1Trigger_L1TGlobal_src
src_L1Trigger_L1TGlobal_src_parent := L1Trigger/L1TGlobal
src_L1Trigger_L1TGlobal_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_L1Trigger_L1TGlobal_src,src/L1Trigger/L1TGlobal/src,LIBRARY))
L1TriggerL1TGlobal := self/L1Trigger/L1TGlobal
L1Trigger/L1TGlobal := L1TriggerL1TGlobal
L1TriggerL1TGlobal_files := $(patsubst src/L1Trigger/L1TGlobal/src/%,%,$(wildcard $(foreach dir,src/L1Trigger/L1TGlobal/src src/L1Trigger/L1TGlobal/src/L1TMenuEditor src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/compilers src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/compilers/vc-7 src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/compilers/vc-8 src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/parser src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/parser/expat src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/parser/non-validating src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/parser/validating src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/parser/xerces src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/tree src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/tree/bits src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/tree/parsing src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/tree/serialization src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/xml src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/xml/bits src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/xml/dom src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/xml/dom/bits src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/xml/sax src/L1Trigger/L1TGlobal/src/L1TMenuEditor/xsd/cxx/xml/sax/bits,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
L1TriggerL1TGlobal_BuildFile    := $(WORKINGDIR)/cache/bf/src/L1Trigger/L1TGlobal/src/BuildFile
L1TriggerL1TGlobal_LOC_USE := self  FWCore/Framework FWCore/PluginManager FWCore/ParameterSet DataFormats/L1TCalorimeter DataFormats/L1TGlobal CondFormats/L1TObjects CondFormats/DataRecord xerces-c
L1TriggerL1TGlobal_LCGDICTS  := x 
L1TriggerL1TGlobal_PRE_INIT_FUNC += $$(eval $$(call LCGDict,L1TriggerL1TGlobal,src/L1Trigger/L1TGlobal/src/classes.h,src/L1Trigger/L1TGlobal/src/classes_def.xml,$(SCRAMSTORENAME_LIB),$(GENREFLEX_ARGS) --fail_on_warnings,))
L1TriggerL1TGlobal_EX_LIB   := L1TriggerL1TGlobal
L1TriggerL1TGlobal_EX_USE   := $(foreach d,$(L1TriggerL1TGlobal_LOC_USE),$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
L1TriggerL1TGlobal_PACKAGE := self/src/L1Trigger/L1TGlobal/src
ALL_PRODS += L1TriggerL1TGlobal
L1TriggerL1TGlobal_CLASS := LIBRARY
L1Trigger/L1TGlobal_forbigobj+=L1TriggerL1TGlobal
L1TriggerL1TGlobal_INIT_FUNC        += $$(eval $$(call Library,L1TriggerL1TGlobal,src/L1Trigger/L1TGlobal/src,src_L1Trigger_L1TGlobal_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
