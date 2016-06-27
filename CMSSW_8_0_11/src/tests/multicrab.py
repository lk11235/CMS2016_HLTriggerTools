###########################
##
# HLTPhysics Run 2016C #
# #
###########################
dataset = {
'HLTPhysics' : '/HLTPhysics/Run2016B-v1/RAW'
}

nfiles = {
'HLTPhysics' : -1
}

filesPerJob = {
'HLTPhysics' : 3
}

if __name__ == '__main__':
	from CRABAPI.RawCommand import crabCommand

def submit(config):
	res = crabCommand('submit', config = config)

from CRABClient.UserUtilities import config
config = config()

name = 'test_HLTPhysicsB_unpre'
config.General.workArea = 'crab_'+name
config.General.transferLogs = True
# config.General.transferOutputs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'hlt.py'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased' 
config.Data.ignoreLocality = True
# config.Data.publication = True
config.Data.publication = False
config.JobType.outputFiles = ['hltbits.root'] #,'DQMIO.root']
config.Site.storageSite = 'T2_US_MIT'

listOfSamples = ['HLTPhysics']
# listOfSamples = ['QCDEM15','QCDEM20','QCDEM30','QCDEM50','QCDEM80','QCDEM120','QCDMu15','QCDMu20','QCDMu30','QCDMu50','QCDMu80','QCDMu120','QCD15','QCD30','QCD50','QCD80','QCD120','QCD170','QCD300','QCD470','DYToLL','WJets']
listOfSamples.reverse()

for sample in listOfSamples:
	config.General.requestName = sample
	config.Data.inputDataset = dataset[sample]
	config.Data.unitsPerJob = filesPerJob[sample]
	config.Data.totalUnits = nfiles[sample]
	config.Data.outputDatasetTag = sample
# Commenting out a lumiMask -- it may cause the crab job to fail
#	config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt' 
	config.Data.outLFNDirBase = '/store/user/aavkhadi/' + name
	submit(config)
