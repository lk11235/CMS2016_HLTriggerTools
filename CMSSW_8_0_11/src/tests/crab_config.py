###########################
##
# HLTPhysics Run 2016B #
# #
###########################

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

name = 'HLTPhysics' # will be part of the work area name and the storage subdir name
runNom = 274998     # the only run number I am getting the files from

# For information on config parameters, see
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile

# section General
config.General.requestName = name
config.General.workArea = 'crab_test_' + name + '_Run' + str( runNom )
config.General.transferOutputs = True
config.General.transferLogs = True

# section JobType
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'hlt.py'
config.JobType.outputFiles = ['hltbits.root']

# section Data
config.Data.inputDataset = '/HLTPhysics/Run2016B-v2/RAW'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.lumiMask = 'lumimask_Run274998.txt' # specifes good lumi sections to be used
config.Data.totalUnits = -1 # analyze all events after applying the lumi mask
config.Data.runRange = str( runNom )
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB()) + '/' + name + '_Run' + str( runNom )
config.Data.outputDatasetTag = name
config.Data.ignoreLocality = True

# section Site
config.Site.storageSite = 'T3_US_FNALLPC'
