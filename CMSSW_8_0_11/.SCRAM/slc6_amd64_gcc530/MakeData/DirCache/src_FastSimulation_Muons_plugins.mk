ifeq ($(strip $(FastSimulationMuonsPlugins)),)
FastSimulationMuonsPlugins := self/src/FastSimulation/Muons/plugins
PLUGINS:=yes
FastSimulationMuonsPlugins_files := $(patsubst src/FastSimulation/Muons/plugins/%,%,$(foreach file,*.cc,$(eval xfile:=$(wildcard src/FastSimulation/Muons/plugins/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/FastSimulation/Muons/plugins/$(file). Please fix src/FastSimulation/Muons/plugins/BuildFile.))))
FastSimulationMuonsPlugins_BuildFile    := $(WORKINGDIR)/cache/bf/src/FastSimulation/Muons/plugins/BuildFile
FastSimulationMuonsPlugins_LOC_USE := self  CondFormats/DataRecord CondFormats/L1TObjects DataFormats/L1GlobalMuonTrigger DataFormats/L1Trigger DataFormats/Math DataFormats/MuonSeed DataFormats/TrackReco DataFormats/TrackerRecHit2D DataFormats/TrajectorySeed FWCore/Framework FWCore/MessageLogger FWCore/ParameterSet FWCore/PluginManager FWCore/ServiceRegistry FWCore/Utilities FastSimDataFormats/L1GlobalMuonTrigger FastSimulation/Tracking FastSimulation/Utilities Geometry/RPCGeometry RecoMuon/GlobalTrackingTools RecoMuon/L3TrackFinder RecoMuon/TrackerSeedGenerator RecoMuon/TrackingTools RecoTracker/TkTrackingRegions SimDataFormats/Track TrackingTools/DetLayers TrackingTools/PatternTools Utilities/General
FastSimulationMuonsPlugins_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,FastSimulationMuonsPlugins,FastSimulationMuonsPlugins,$(SCRAMSTORENAME_LIB),src/FastSimulation/Muons/plugins))
FastSimulationMuonsPlugins_PACKAGE := self/src/FastSimulation/Muons/plugins
ALL_PRODS += FastSimulationMuonsPlugins
FastSimulation/Muons_forbigobj+=FastSimulationMuonsPlugins
FastSimulationMuonsPlugins_INIT_FUNC        += $$(eval $$(call Library,FastSimulationMuonsPlugins,src/FastSimulation/Muons/plugins,src_FastSimulation_Muons_plugins,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
FastSimulationMuonsPlugins_CLASS := LIBRARY
else
$(eval $(call MultipleWarningMsg,FastSimulationMuonsPlugins,src/FastSimulation/Muons/plugins))
endif
ALL_COMMONRULES += src_FastSimulation_Muons_plugins
src_FastSimulation_Muons_plugins_parent := FastSimulation/Muons
src_FastSimulation_Muons_plugins_INIT_FUNC += $$(eval $$(call CommonProductRules,src_FastSimulation_Muons_plugins,src/FastSimulation/Muons/plugins,PLUGINS))
