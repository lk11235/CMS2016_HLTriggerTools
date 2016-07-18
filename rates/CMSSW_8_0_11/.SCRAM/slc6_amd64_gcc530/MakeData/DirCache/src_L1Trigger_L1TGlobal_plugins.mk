ifeq ($(strip $(L1TriggerL1TGlobalPlugins)),)
L1TriggerL1TGlobalPlugins := self/src/L1Trigger/L1TGlobal/plugins
PLUGINS:=yes
L1TriggerL1TGlobalPlugins_files := $(patsubst src/L1Trigger/L1TGlobal/plugins/%,%,$(foreach file,*.cc,$(eval xfile:=$(wildcard src/L1Trigger/L1TGlobal/plugins/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/L1Trigger/L1TGlobal/plugins/$(file). Please fix src/L1Trigger/L1TGlobal/plugins/BuildFile.))))
L1TriggerL1TGlobalPlugins_BuildFile    := $(WORKINGDIR)/cache/bf/src/L1Trigger/L1TGlobal/plugins/BuildFile
L1TriggerL1TGlobalPlugins_LOC_USE := self  FWCore/Framework FWCore/PluginManager FWCore/ParameterSet DataFormats/L1Trigger CondFormats/L1TObjects CondFormats/DataRecord CondTools/L1Trigger xerces-c utm L1TriggerConfig/L1GtConfigProducers L1Trigger/L1TGlobal L1Trigger/GlobalTrigger
L1TriggerL1TGlobalPlugins_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,L1TriggerL1TGlobalPlugins,L1TriggerL1TGlobalPlugins,$(SCRAMSTORENAME_LIB),src/L1Trigger/L1TGlobal/plugins))
L1TriggerL1TGlobalPlugins_PACKAGE := self/src/L1Trigger/L1TGlobal/plugins
ALL_PRODS += L1TriggerL1TGlobalPlugins
L1Trigger/L1TGlobal_forbigobj+=L1TriggerL1TGlobalPlugins
L1TriggerL1TGlobalPlugins_INIT_FUNC        += $$(eval $$(call Library,L1TriggerL1TGlobalPlugins,src/L1Trigger/L1TGlobal/plugins,src_L1Trigger_L1TGlobal_plugins,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
L1TriggerL1TGlobalPlugins_CLASS := LIBRARY
else
$(eval $(call MultipleWarningMsg,L1TriggerL1TGlobalPlugins,src/L1Trigger/L1TGlobal/plugins))
endif
ALL_COMMONRULES += src_L1Trigger_L1TGlobal_plugins
src_L1Trigger_L1TGlobal_plugins_parent := L1Trigger/L1TGlobal
src_L1Trigger_L1TGlobal_plugins_INIT_FUNC += $$(eval $$(call CommonProductRules,src_L1Trigger_L1TGlobal_plugins,src/L1Trigger/L1TGlobal/plugins,PLUGINS))
