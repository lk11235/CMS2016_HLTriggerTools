ifeq ($(strip $(GeneratorInterface/GenFilters)),)
ALL_COMMONRULES += src_GeneratorInterface_GenFilters_src
src_GeneratorInterface_GenFilters_src_parent := GeneratorInterface/GenFilters
src_GeneratorInterface_GenFilters_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_GeneratorInterface_GenFilters_src,src/GeneratorInterface/GenFilters/src,LIBRARY))
GeneratorInterfaceGenFilters := self/GeneratorInterface/GenFilters
GeneratorInterface/GenFilters := GeneratorInterfaceGenFilters
GeneratorInterfaceGenFilters_files := $(patsubst src/GeneratorInterface/GenFilters/src/%,%,$(wildcard $(foreach dir,src/GeneratorInterface/GenFilters/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
GeneratorInterfaceGenFilters_BuildFile    := $(WORKINGDIR)/cache/bf/src/GeneratorInterface/GenFilters/BuildFile
GeneratorInterfaceGenFilters_LOC_USE := self  boost FWCore/PluginManager FWCore/ParameterSet FWCore/Framework FWCore/Utilities SimDataFormats/GeneratorProducts heppdt clhep root GeneratorInterface/Pythia6Interface GeneratorInterface/Core SimGeneral/HepPDTRecord DataFormats/GeometryVector DataFormats/GeometrySurface TrackPropagation/SteppingHelixPropagator MagneticField/Records TrackingTools/TrajectoryState TrackingTools/TrajectoryParametrization TrackingTools/Records CommonTools/UtilAlgos FWCore/ServiceRegistry FastSimulation/Particle FastSimulation/BaseParticlePropagator TrackingTools/GeomPropagators DataFormats/HepMCCandidate DataFormats/JetReco DataFormats/EgammaReco
GeneratorInterfaceGenFilters_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,GeneratorInterfaceGenFilters,GeneratorInterfaceGenFilters,$(SCRAMSTORENAME_LIB),src/GeneratorInterface/GenFilters/src))
GeneratorInterfaceGenFilters_PACKAGE := self/src/GeneratorInterface/GenFilters/src
ALL_PRODS += GeneratorInterfaceGenFilters
GeneratorInterfaceGenFilters_CLASS := LIBRARY
GeneratorInterface/GenFilters_forbigobj+=GeneratorInterfaceGenFilters
GeneratorInterfaceGenFilters_INIT_FUNC        += $$(eval $$(call Library,GeneratorInterfaceGenFilters,src/GeneratorInterface/GenFilters/src,src_GeneratorInterface_GenFilters_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
