# -*- coding: iso-8859-15 -*-#  25ns master table: /dev/CMSSW_7_4_0/HLT/V560                                             Lien Steam Gdoc      Lien Steam Gdoc    
#  same as /dev/CMSSW_7_4_0/GRun/V173      L1 prescales            HLT prescales            Total prescale               /frozen/2015/25ns14e33/v3.0/HLT/V1       /dev/CMSSW_7_4_0/GRun/V106    

triggerList = []
triggerName = "_frozen_2015_25ns14e33_v4p4_HLT_V1"

triggersGroupMap = {
	'HLT_QuadPFJet_DoubleBTagCSV_VBF_Mqq240_v4': ['HIG'],
	'HLT_PFHT400_SixJet30_BTagCSV0p55_2PFBTagCSV0p72_v3': ['HIG'],
	'HLT_L1SingleMu16_v1': ['Muons'],
	'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v2': ['EXO'],
	'HLT_HcalCalibration_v1': ['HCAL'],
	'HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v3': ['HIG', 'TAU'],
	'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40_v3': ['HIG'],
	'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v2': ['TAU', 'HIG'],
	'HLT_DoublePhoton85_v2': ['EXO'],
	'HLT_HIL1DoubleMu0BPTX_v1': ['HIN'],
	'HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing_v2': ['BPH'],
	'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v3': ['EXO'],
	'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v2': ['EXO'],
	'HLT_HISinglePhoton20ForEndOfFill_v1': ['HIN'],
	'HLT_Mu55_v1': ['EXO'],
	'HLT_HIL2Mu3BPTX_v1': ['HIN'],
	'HLT_Ele15_IsoVVVL_BTagCSV0p72_PFHT400_v3': ['SUSY'],
	'HLT_Photon50_R9Id90_HE10_IsoM_v3': ['SMP', 'SUSY'],
	'HLT_HT500_DisplacedDijet40_Inclusive_v2': ['EXO'],
	'HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v3': ['EXO'],
	'HLT_Mu20_Mu10_v1': ['HIG'],
	'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80_v1': ['HIG'],
	'HLT_Mu10_CentralPFJet30_BTagCSV0p54PF_v3': ['SUSY'],
	'HLT_Mu17_v2': ['Muons'],
	'HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v2': ['EXO'],
	'HLT_HT425_v1': ['EXO'],
	'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_VBF_v2': ['HIG'],
	'HLT_TkMu24_eta2p1_v2': ['SMP'],
	'HLT_PFJet400_v4': ['SMP', 'B2G', 'BTV'],
	'HLT_Ele115_CaloIdVT_GsfTrkIdT_v2': ['EXO'],
	'HLT_PFJet260_v4': ['JME', 'SMP', 'BTV'],
	'HLT_Photon36_R9Id90_HE10_IsoM_v3': ['SMP', 'SUSY'],
	'HLT_AK4PFJet100_v3': ['HIN'],
	'HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV0p54PF_v3': ['SUSY'],
	'HLT_PFMET300_v1': ['Hotline'],
	'HLT_Ele27_eta2p1_WPLoose_Gsf_v2': ['Egamma', 'HIG', 'SMP'],
	'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v2': ['HIG'],
	'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v2': ['EXO'],
	'HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v2': ['EXO'],
	'HLT_Mu7p5_Track3p5_Jpsi_v2': ['BPH'],
	'HLT_PFHT800_v2': ['SUSY'],
	'HLT_DiCentralPFJet55_PFMET110_v1': ['SUSY'],
	'HLT_DiPFJetAve320_v2': ['JME'],
	'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v3': ['SUSY'],
	'HLT_IsoMu22_v2': ['TOP'],
	'HLT_Rsq0p30_v2': ['SUSY'],
	'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF_v2': ['HIG'],
	'HLT_Mu17_Photon35_CaloIdL_L1ISO_v3': ['HIG'],
	'HLT_DiPFJetAve80_HFJEC_v3': ['JME'],
	'HLT_PixelTracks_Multiplicity135ForEndOfFill_v1': ['HIN'],
	'HLT_MonoCentralPFJet80_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v2': ['EXO'],
	'HLT_Dimuon6_Jpsi_NoVertexing_v2': ['BPH'],
	'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF_v2': ['HIG'],
	'HLT_PFHT650_4JetPt50_v1': ['EXO'],
	'HLT_Photon30_v3': ['SMP', 'EXO'],
	'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40_v3': ['HIG'],
	'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52_v2': ['SUSY'],
	'HLT_TkMu20_v2': ['SMP'],
	'HLT_PFMET110_PFMHT110_IDTight_v2': ['HIG'],
	'HLT_IsoMu20_v3': ['SMP', 'TOP', 'Muons'],
	'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v2': ['EXO', 'SUSY'],
	'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT250_v1': ['SUSY'],
	'HLT_Rsq0p02_MR300_TriPFJet80_60_40_DoublePFBTagCSV0p7_0p4_Mbb60_200_v1': ['SUSY'],
	'HLT_DoubleJetsC100_DoubleBTagCSV0p9_DoublePFJetsC100MaxDeta1p6_v2': ['SUSY'],
	'HLT_Photon90_CaloIdL_PFHT500_v3': ['SUSY', 'EXO'],
	'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v1': ['TAU', 'HIG'],
	'HLT_Physics_v2': ['TSG'],
	'HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL_v2': ['EXO'],
	'HLT_AK4CaloJet30_v3': ['HIN'],
	'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF_v2': ['HIG'],
	'HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV0p45_v2': ['B2G'],
	'HLT_Photon90_CaloIdL_PFHT600_v2': ['SUSY', 'EXO'],
	'HLT_MET60_IsoTrk35_Loose_v1': ['EXO'],
	#'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v2': ['SUSY'],
	'HLT_HT500to550_v1': ['EXO', 'PPD'],
	'HLT_Rsq0p25_v2': ['SUSY'],
	'HLT_DoubleJetsC100_DoubleBTagCSV0p85_DoublePFJetsC160_v2': ['SUSY'],
	'HLT_DiPFJetAve60_v2': ['JME'],
	'HLT_Mu12_Photon25_CaloIdL_v3': ['HIG'],
	'HLT_Mu17_Photon22_CaloIdL_L1ISO_v1': ['HIG'],
	'HLT_DiPFJetAve140_v2': ['JME'],
	'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v2': ['EXO'],
	'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v4': ['TAU', 'HIG'],
	'HLT_HT450to470_v1': ['EXO', 'PPD'],
	'HLT_CaloJet500_NoJetID_v2': ['EXO'],
	'HLT_PFMET400_v1': ['Hotline'],
	'HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v2': ['EXO'],
	'HLT_Dimuon10_Jpsi_Barrel_v2': ['BPH'],
	'HLT_Rsq0p02_MR300_TriPFJet80_60_40_DoublePFBTagCSV0p7_Mbb60_200_v1': ['SUSY'],
	'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v3': ['HIG', 'SMP'],
	'HLT_IsoMu17_eta2p1_MediumIsoPFTau40_Trk1_eta2p1_Reg_v5': ['TAU', 'HIG'],
	'HLT_ZeroBias_v2': ['TSG'],
	'HLT_PixelTracks_Multiplicity110ForEndOfFill_v1': ['HIN'],
	'HLT_JetE70_NoBPTX3BX_NoHalo_v2': ['EXO'],
	'HLT_Mu40_eta2p1_PFJet200_PFJet50_v3': ['B2G'],
	'HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v2': ['EXO'],
	'HLT_RsqMR270_Rsq0p09_MR200_v2': ['SUSY'],
	'HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v2': ['EXO'],
	'HLT_HT275_v1': ['EXO'],
	'HLT_Photon75_R9Id90_HE10_IsoM_v3': ['SMP', 'SUSY'],
	'HLT_Photon120_R9Id90_HE10_IsoM_v3': ['SMP', 'SUSY'],
	'HLT_Ele22_eta2p1_WPTight_Gsf_v3': ['HIG', 'TAU'],
	'HLT_PFJet80_v4': ['SMP', 'BTV'],
	'HLT_Ele27_eta2p1_WPLoose_Gsf_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v2': ['HIG', 'TAU', 'EXO'],
	'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v2': ['SUSY'],
	'HLT_HT2500_v1': ['Hotline'],
	'HLT_DoubleMu3_Mass10_v1': ['PPD', 'EXO'],
	'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v2': ['EXO', 'SUSY'],
	'HLT_QuadPFJet_VBF_v4': ['HIG'],
	'HLT_PFHT400_v2': ['SUSY'],
	'HLT_Mu7p5_L2Mu2_Jpsi_v2': ['BPH'],
	'HLT_DiPFJetAve100_HFJEC_v3': ['JME'],
	'HLT_DoubleMu4_JpsiTrk_Displaced_v2': ['BPH'],
	'HLT_PFMET170_JetIdCleaned_v2': ['SUSY', 'EXO', 'B2G'],
	'HLT_HT350_DisplacedDijet80_DisplacedTrack_v2': ['EXO'],
	'HLT_Mu12_Photon25_CaloIdL_L1ISO_v3': ['HIG'],
	'HLT_FullTrack50_v2': ['HIN'],
	'HLT_PFMET120_BTagCSV0p72_v1': ['SUSY'],
	'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v4': ['SUSY'],
	'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v2': ['TAU', 'HIG'],
	'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v2': ['HIG', 'TAU'],
	'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v2': ['TOP', 'HIG', 'SMP', 'B2G'],
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v2': ['TOP', 'HIG', 'SMP', 'B2G'],
	'HLT_PFHT350_v3': ['SUSY', 'EXO'],
	'HLT_Mu24_eta2p1_v2': ['SMP', 'EXO'],
	'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v3': ['HIG'],
	'HLT_Mu6_PFHT200_PFMET80_BTagCSV0p72_v1': ['SUSY'],
	'HLT_Ele33_CaloIdM_TrackIdM_PFJet30_v3': ['SUSY'],
	'HLT_Ele23_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v2': ['TOP'],
	'HLT_RsqMR270_Rsq0p09_MR200_4jet_v2': ['SUSY'],
	'HLT_Mu17_Photon30_CaloIdL_L1ISO_v3': ['HIG'],
	'HLT_JetE50_NoBPTX3BX_NoHalo_v2': ['EXO'],
	'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT250_v1': ['SUSY'],
	'HLT_IsoMu18_CentralPFJet30_BTagCSV07_v2': ['TOP'],
	'HLT_IsoMu22_TriCentralPFJet50_40_30_v2': ['TOP'],
	'HLT_Mu17_Mu8_SameSign_DZ_v1': ['HIG', 'B2G'],
	'HLT_Photon135_PFMET100_v1': ['EXO'],
	'HLT_DoubleJetsC112_DoubleBTagCSV0p9_DoublePFJetsC112MaxDeta1p6_v2': ['SUSY'],
	'HLT_VBF_DisplacedJet40_TightID_DisplacedTrack_v2': ['EXO'],
	'HLT_Photon120_v3': ['SMP', 'EXO'],
	'HLT_DoubleMu38NoFiltersNoVtx_v2': ['EXO'],
	'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v3': ['SUSY'],
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v3': ['HIG', 'TOP', 'SMP'],
	'HLT_BTagMu_Jet300_Mu5_v2': ['BTV'],
	'HLT_JetE30_NoBPTX_v2': ['EXO'],
	'HLT_Mu300_v1': ['Hotline'],
	'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v2': ['HIG'],
	'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v2': ['EXO'],
	'HLT_HcalUTCA_v2': ['HCAL'],
	'HLT_Ele27_eta2p1_WPTight_Gsf_v2': ['Egamma'],
	'HLT_Mu25_TkMu0_dEta18_Onia_v2': ['BPH', 'SMP'],
	'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v2': ['HIG'],
	'HLT_Ele27_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v1': ['TOP'],
	'HLT_PFJet450_v4': ['SMP', 'B2G', 'BTV'],
	'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v3': ['B2G'],
	'HLT_PixelTracks_Multiplicity85ForEndOfFill_v1': ['HIN'],
	'HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v2': ['EXO'],
	'HLT_IsoMu16_eta2p1_MET30_LooseIsoPFTau50_Trk30_eta2p1_v1': ['TAU', 'HIG'],
	'HLT_L2Mu10_NoVertex_NoBPTX_v2': ['EXO'],
	'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p45_v3': ['B2G'],
	'HLT_IsoMu18_TriCentralPFJet50_40_30_v2': ['TOP'],
	'HLT_IsoMu17_eta2p1_MediumIsoPFTau35_Trk1_eta2p1_Reg_v3': ['TAU', 'HIG'],
	'HLT_HIL3Mu3BPTX_v1': ['HIN'],
	'HLT_PFJet320_v4': ['SMP', 'BTV'],
	'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v2': ['EXO'],
	'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v2': ['BPH'],
	'HLT_Mu16_TkMu0_dEta18_Onia_v2': ['BPH', 'SMP'],
	'HLT_PFHT450_SixJet40_v3': ['HIG'],
	'HLT_DiPFJetAve200_v2': ['JME'],
	'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v1': ['EXO'],
	'HLT_IsoMu16_eta2p1_MET30_v1': ['TAU', 'HIG'],
	'HLT_HcalNZS_v2': ['HCAL'],
	'HLT_BTagMu_DiJet40_Mu5_v2': ['BTV'],
	'HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq500_v4': ['HIG'],
	'HLT_PFHT250_v2': ['SUSY'],
	'HLT_Dimuon8_PsiPrime_Barrel_v2': ['BPH'],
	'HLT_Mu7p5_Track7_Jpsi_v2': ['BPH'],
	'HLT_Photon500_v1': ['Hotline'],
	'HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v1': ['EXO'],
	'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v1': ['HIG', 'SMP'],
	'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v2': ['Muons', 'SMP'],
	'HLT_PFHT550_4JetPt50_v1': ['EXO'],
	'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v3': ['B2G'],
	'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55_v2': ['SUSY'],
	'HLT_Mu16_TkMu0_dEta18_Phi_v2': ['BPH'],
	'HLT_VBF_DisplacedJet40_Hadronic_2PromptTrack_v2': ['EXO'],
	'HLT_Mu17_TkMu8_DZ_v2': ['TOP', 'HIG', 'SMP'],
	'HLT_AK4PFJet50_v3': ['HIN'],
	'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40_v3': ['HIG'],
	'HLT_BTagMu_DiJet70_Mu5_v2': ['BTV'],
	'HLT_IsoMu20_eta2p1_LooseIsoPFTau20_v3': ['TAU', 'HIG'],
	'HLT_IsoTrackHE_v1': ['HCAL'],
	'HLT_PFHT600_v3': ['SUSY', 'EXO'],
	'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v3': ['HIG', 'SMP'],
	'HLT_Ele30WP60_Ele8_Mass55_v2': ['HIG'],
	'HLT_Photon175_v3': ['SMP', 'EXO'],
	'HLT_PFMET90_PFMHT90_IDTight_v2': ['HIG'],
	'HLT_FullTrack12ForEndOfFill_v1': ['HIN'],
	'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v3': ['EXO', 'B2G'],
	'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v3': ['HIG'],
	'HLT_PFHT400_SixJet30_v3': ['HIG'],
	'HLT_OldIsoMu18_v1': ['SMP', 'TOP'],
	'HLT_Mu7p5_Track2_Upsilon_v2': ['BPH'],
	'HLT_QuadJet45_TripleBTagCSV0p67_v3': ['HIG'],
	'HLT_Mu14er_PFMET100_v1': ['SUSY'],
	'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v3': ['EXO'],
	'HLT_HISinglePhoton60_v2': ['HIN'],
	'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v1': ['SUSY'],
	'HLT_Mu16_eta2p1_MET30_v1': ['TAU', 'HIG'],
	'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v2': ['EXO'],
	'HLT_IsoMu17_eta2p1_v3': ['TAU', 'HIG'],
	'HLT_PFHT200_PFAlphaT0p51_v2': ['SUSY'],
	'HLT_Ele30WP60_SC4_Mass55_v3': ['Egamma'],
	'HLT_Mu6_PFHT200_PFMET100_v1': ['SUSY'],
	'HLT_Mu15_IsoVVVL_PFHT350_PFMET50_v2': ['SUSY'],
	'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_PFMET40_v3': ['HIG'],
	'HLT_OldIsoTkMu18_v2': ['SMP', 'TOP'],
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v3': ['HIG', 'TOP', 'SMP', 'B2G'],
	'HLT_DoubleJet90_Double30_TripleBTagCSV0p67_v3': ['HIG'],
	'HLT_Ele15_IsoVVVL_PFHT350_v2': ['SUSY'],
	'HLT_DiPFJetAve260_v2': ['JME'],
	'HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV0p45_v2': ['B2G'],
	'HLT_DoubleJet90_Double30_DoubleBTagCSV0p67_v3': ['HIG'],
	'HLT_PFJet60_v4': ['SMP', 'BTV'],
	'HLT_Photon165_R9Id90_HE10_IsoM_v3': ['HIG', 'SUSY', 'SMP'],
	'HLT_L1_TripleJet_VBF_v4': ['HIG'],
	'HLT_PFJet500_v4': ['SMP', 'B2G', 'BTV'],
	'HLT_PFHT350_PFMET100_v1': ['SUSY', 'EXO'],
	'HLT_IsoTkMu27_v3': ['SMP', 'HIG'],
	'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40_v3': ['HIG'],
	'HLT_Photon90_R9Id90_HE10_IsoM_v3': ['SMP', 'SUSY'],
	'HLT_Ele105_CaloIdVT_GsfTrkIdT_v3': ['EXO', 'B2G'],
	'HLT_HT550to650_v1': ['EXO', 'PPD'],
	'HLT_QuadJet45_DoubleBTagCSV0p67_v3': ['HIG'],
	'HLT_Diphoton30_18_Solid_R9Id_AND_IsoCaloId_AND_HE_R9Id_Mass55_v1': ['HIG', 'SMP'],
	'HLT_DoubleMu4_3_Jpsi_Displaced_v2': ['BPH'],
	'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v4': ['TAU', 'HIG'],
	'HLT_AK4PFJet30_v3': ['HIN'],
	'HLT_IsoTkMu20_v4': ['SMP', 'TOP'],
	'HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight_v2': ['EXO'],
	'HLT_DoublePhoton60_v1': ['EXO', 'EGM'],
	'HLT_AK4PFJet80_v3': ['HIN'],
	'HLT_HT470to500_v1': ['EXO', 'PPD'],
	'HLT_HISinglePhoton15ForEndOfFill_v1': ['HIN'],
	'HLT_Mu15_IsoVVVL_PFHT600_v3': ['SUSY'],
	'HLT_Ele23_WPLoose_Gsf_TriCentralPFJet50_40_30_v2': ['TOP'],
	'HLT_Ele35_CaloIdVT_GsfTrkIdT_PFJet150_PFJet50_v1': ['B2G'],
	'HLT_HT350_DisplacedDijet40_DisplacedTrack_v2': ['EXO'],
	'HLT_AK4CaloJet100_v2': ['HIN'],
	'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v3': ['SUSY'],
	'HLT_BTagMu_DiJet20_Mu5_v2': ['BTV'],
	'HLT_AK8PFJet360_TrimMass30_v3': ['B2G'],
	'HLT_HT650_v2': ['EXO', 'PPD'],
	'HLT_HT750_DisplacedDijet80_Inclusive_v2': ['EXO'],
	'HLT_MET200_v1': ['EXO'],
	'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v2': ['EXO'],
	'HLT_DiPFJetAve300_HFJEC_v3': ['JME'],
	'HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90_IDTight_v1': ['EXO'],
	'HLT_Ele15_IsoVVVL_PFHT600_v3': ['SUSY'],
	'HLT_Mu7p5_Track2_Jpsi_v2': ['BPH'],
	'HLT_Dimuon0er16_Jpsi_NoVertexing_v2': ['BPH'],
	'HLT_ZeroBias_IsolatedBunches_v1': ['TSG'],
	'HLT_HT400_DisplacedDijet40_Inclusive_v2': ['EXO'],
	'HLT_Mu8_v3': ['Muon', 'SUSY'],
	'HLT_PFMET170_HBHECleaned_v2': ['SUSY', 'EXO', 'B2G'],
	'HLT_IsoTrackHB_v1': ['HCAL'],
	'HLT_JetE30_NoBPTX3BX_NoHalo_v2': ['EXO'],
	'HLT_PFMET100_PFMHT100_IDTight_v2': ['HIG'],
	'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v2': ['HIG'],
	'HLT_Mu40_TkMu11_v2': ['EXO'],
	'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v1': ['HIG'],
	'HLT_DiPFJetAve80_v2': ['JME'],
	'HLT_Mu20_v2': ['SMP', 'Muons'],
	'HLT_Photon75_v3': ['SMP', 'EXO'],
	'HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL_v2': ['EXO'],
	'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_NoHalo_v2': ['EXO'],
	'HLT_Mu7p5_L2Mu2_Upsilon_v2': ['BPH'],
	'HLT_Mu7p5_Track7_Upsilon_v2': ['BPH'],
	'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v2': ['SUSY'],
	'HLT_L1SingleMuOpen_v2': ['0'],
	'HLT_Ele27_WPLoose_Gsf_TriCentralPFJet50_40_30_v1': ['TOP'],
	'HLT_IsoTkMu22_v2': ['SMP', 'Muons'],
	'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v3': ['HIG'],
	'HLT_QuadPFJet_DoubleBTagCSV_VBF_Mqq200_v4': ['HIG'],
	'HLT_DiPFJetAve160_HFJEC_v3': ['JME'],
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v3': ['HIG', 'TOP', 'SMP'],
	'HLT_Ele23_WPLoose_Gsf_v3': ['SMP', 'TOP'],
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v2': ['Muons', 'SMP'],
	'HLT_Activity_Ecal_SC7_v2': ['ECAL'],
	'HLT_HT200_v1': ['EXO'],
	'HLT_PFJet140_v4': ['SMP', 'BTV'],
	'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET80_v1': ['TAU', 'HIG'],
	'HLT_Dimuon8_Upsilon_Barrel_v2': ['BPH'],
	'HLT_Mu27_TkMu8_v2': ['EXO', 'B2G'],
	'HLT_L1Tech_DT_GlobalOR_v2': ['DT'],
	'HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq460_v4': ['HIG'],
	'HLT_DiPFJetAve220_HFJEC_v3': ['JME'],
	'HLT_DoubleMu4_3_Bs_v2': ['BPH'],
	'HLT_PFMET120_Mu5_v1': ['SUSY'],
	'HLT_DiPFJetAve60_HFJEC_v3': ['JME'],
	'HLT_QuadMuon0_Dimuon0_Upsilon_v2': ['BPH'],
	'HLT_L2Mu10_v1': ['Muons'],
	'HLT_Mu50_v2': ['EXO', 'B2G'],
	'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF_v2': ['HIG'],
	'HLT_VBF_DisplacedJet40_DisplacedTrack_v2': ['EXO'],
	'HLT_Mu3er_PFHT140_PFMET125_v1': ['SUSY'],
	'HLT_MET90_IsoTrk50_v2': ['EXO'],
	'HLT_ECALHT800_v2': ['EXO'],
	'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v3': ['HIG', 'SMP'],
	'HLT_BTagMu_DiJet110_Mu5_v2': ['BTV'],
	'HLT_DoubleMu33NoFiltersNoVtx_v2': ['EXO'],
	'HLT_Mu45_eta2p1_v2': ['EXO', 'B2G'],
	'HLT_Ele23_WPLoose_Gsf_WHbbBoost_v2': ['HIG'],
	'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v3': ['SUSY'],
	'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v1': ['EXO'],
	'HLT_Ele22_eta2p1_WPLoose_Gsf_v3': ['Egamma'],
	'HLT_VBF_DisplacedJet40_Hadronic_v2': ['EXO'],
	'HLT_Mu30_eta2p1_PFJet150_PFJet50_v1': ['B2G'],
	'HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v2': ['EXO'],
	'HLT_PFHT650_v3': ['SUSY', 'EXO'],
	'HLT_DoubleMu8_Mass8_PFHT250_v1': ['SUSY'],
	'HLT_HT250_DisplacedDijet40_DisplacedTrack_v2': ['EXO'],
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v3': ['HIG', 'SMP', 'TOP'],
	'HLT_Mu17_Mu8_DZ_v2': ['TOP', 'HIG', 'SMP'],
	'HLT_Ele27_WPLoose_Gsf_v1': ['TOP'],
	'HLT_Photon600_v1': ['Hotline'],
	'HLT_TkMu27_v2': ['SMP'],
	'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53_v2': ['SUSY'],
	'HLT_Photon90_v3': ['SMP', 'EXO'],
	'HLT_PFMET120_PFMHT120_IDTight_v2': ['HIG'],
	'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40_v3': ['HIG'],
	'HLT_HcalPhiSym_v2': ['HCAL'],
	'HLT_PFMET170_NoiseCleaned_v3': ['SUSY', 'EXO', 'B2G'],
	'HLT_Ele33_CaloIdL_TrackIdL_IsoVL_PFJet30_v3': ['SUSY'],
	'HLT_MET75_IsoTrk50_v2': ['EXO'],
	'HLT_HISinglePhoton10ForEndOfFill_v1': ['HIN'],
	'HLT_Ele12_CaloIdM_TrackIdM_PFJet30_v3': ['SUSY'],
	'HLT_IsoMu22_CentralPFJet30_BTagCSV07_v2': ['TOP'],
	'HLT_MET250_v1': ['Hotline'],
	'HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v2': ['EXO'],
	'HLT_VBF_DisplacedJet40_TightID_Hadronic_v2': ['EXO'],
	'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v2': ['HIG'],
	'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v3': ['EXO'],
	'HLT_Mu20_Mu10_DZ_v1': ['HIG'],
	'HLT_DiPFJetAve500_v2': ['JME'],
	'HLT_Mu20_Mu10_SameSign_DZ_v1': ['HIG'],
	'HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15_v2': ['EXO'],
	'HLT_Dimuon0_Phi_Barrel_v2': ['BPH'],
	'HLT_PFHT475_v2': ['SUSY', 'EXO'],
	'HLT_Dimuon13_PsiPrime_v2': ['BPH'],
	'HLT_Mu12_Photon25_CaloIdL_L1OR_v3': ['HIG'],
	'HLT_Dimuon20_Jpsi_v2': ['BPH'],
	'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v2': ['SUSY'],
	'HLT_Photon165_HE10_v3': ['SMP', 'SUSY'],
	'HLT_Dimuon0_Jpsi_Muon_v2': ['BPH'],
	'HLT_Dimuon13_Upsilon_v2': ['BPH'],
	'HLT_QuadMuon0_Dimuon0_Jpsi_v2': ['BPH'],
	'HLT_AK4CaloJet40_v2': ['HIN'],
	'HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelSeedMatch_Mass70_v1': ['HIG'],
	'HLT_L1SingleMuOpen_DT_v2': ['0'],
	'HLT_PFJet40_v4': ['SMP', 'BTV'],
	'HLT_L2DoubleMu23_NoVertex_v2': ['EXO'],
	'HLT_DiPFJetAve40_v2': ['JME'],
	'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57_v2': ['SUSY'],
	'HLT_DoubleIsoMu17_eta2p1_v3': ['HIG', 'TAU'],
	'HLT_AK4CaloJet80_v2': ['HIN'],
	'HLT_HIL2DoubleMu0BPTX_v1': ['HIN'],
	'HLT_HT550_DisplacedDijet40_Inclusive_v2': ['EXO'],
	'HLT_Photon36_v3': ['SMP', 'EXO'],
	'HLT_HISinglePhoton40_v2': ['HIN'],
	'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51_v2': ['SUSY'],
	'HLT_RsqMR240_Rsq0p09_MR200_v2': ['SUSY'],
	'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v3': ['HIG'],
	'HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v2': ['B2G'],
	'HLT_Photon30_R9Id90_HE10_IsoM_v3': ['SMP', 'SUSY'],
	'HLT_GlobalRunHPDNoise_v2': ['HCAL'],
	'HLT_TripleMu_12_10_5_v2': ['HIG'],
	'HLT_PFJet200_v4': ['SMP', 'BTV'],
	'HLT_MET300_v1': ['Hotline'],
	'HLT_Mu8_TrkIsoVVL_v3': ['Muon', 'SUSY', 'HIG'],
	'HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15_v2': ['EXO'],
	'HLT_AK4CaloJet50_v2': ['HIN'],
	'HLT_PixelTracks_Multiplicity60ForEndOfFill_v1': ['HIN'],
	'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v4': ['SUSY'],
	'HLT_EcalCalibration_v1': ['ECAL'],
	'HLT_PFHT750_4JetPt50_v3': ['SUSY'],
	'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v3': ['HIG'],
	'HLT_PixelTracks_Multiplicity160ForEndOfFill_v1': ['HIN'],
	'HLT_HT2000_v1': ['Hotline'],
	'HLT_DoubleJetsC112_DoubleBTagCSV0p85_DoublePFJetsC172_v2': ['SUSY'],
	'HLT_Random_v1': ['AlCa', 'Tracker'],
	'HLT_PFHT450_SixJet40_PFBTagCSV0p72_v3': ['HIG'],
	'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v3': ['HIG', 'TAU'],
	'HLT_Photon50_v3': ['SMP', 'EXO'],
	'HLT_Ele32_eta2p1_WPTight_Gsf_v2': ['HIG', 'Egamma'],
	'HLT_IsoMu27_v3': ['SMP', 'HIG'],
	'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v2': ['BPH'],
	'HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v1': ['HIG'],
	'HLT_Ele15_IsoVVVL_PFHT350_PFMET50_v2': ['SUSY'],
	'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v3': ['HIG', 'SMP'],
	'HLT_LooseIsoPFTau50_Trk30_eta2p1_v3': ['TAU', 'HIG'],
	'HLT_Mu350_v1': ['Hotline'],
	'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v3': ['EXO', 'B2G'],
	'HLT_Photon300_NoHE_v2': ['HIG'],
	'HLT_Photon22_R9Id90_HE10_IsoM_v2': ['SMP', 'SUSY'],
	'HLT_Mu27_v2': ['SMP'],
	'HLT_IsoTkMu18_v2': ['SMP', 'Muons'],
	'HLT_Dimuon0_Upsilon_Muon_v2': ['BPH'],
	'HLT_HT650_DisplacedDijet80_Inclusive_v2': ['EXO'],
	'HLT_Photon22_v2': ['SMP', 'EXO'],
	'HLT_Ele27_eta2p1_WPLoose_Gsf_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v3': ['HIG', 'TAU', 'EXO'],
	'HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v2': ['EXO'],
	'HLT_HT575_v1': ['EXO'],
	'HLT_Mu30_TkMu11_v2': ['EXO', 'B2G'],
	'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v2': ['SUSY'],
	'HLT_Mu15_IsoVVVL_BTagCSV0p72_PFHT400_v3': ['SUSY'],
	'HLT_DiPFJetAve400_v2': ['JME'],
	'HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v1': ['HIG', 'SMP'],
	'HLT_RsqMR240_Rsq0p09_MR200_4jet_v2': ['SUSY'],
	'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF_v2': ['HIG'],
	'HLT_HT325_v1': ['EXO'],
	'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10_v2': ['EXO'],
	'HLT_Mu15_IsoVVVL_PFHT350_v2': ['SUSY'],
	'HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v2': ['EXO'],
	'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v2': ['EXO'],
	'HLT_Mu17_TrkIsoVVL_v2': ['SUSY', 'HIG', 'Muons'],
	'HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60_v2': ['EXO'],
	'HLT_Dimuon16_Jpsi_v2': ['BPH'],
	'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v4': ['TAU', 'HIG'],
	'HLT_DoubleMu18NoFiltersNoVtx_v2': ['EXO'],
	'HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v2': ['EXO'],
	'HLT_MonoCentralPFJet80_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v3': ['EXO'],
	'HLT_Photon250_NoHE_v2': ['HIG'],
	'HLT_IsoMu18_v2': ['SMP', 'TOP', 'Muons'],
	'HLT_PFHT300_v2': ['SUSY'],
	'HLT_PFMET170_v2': ['SUSY', 'EXO', 'B2G'],
	'HLT_Mu7p5_Track3p5_Upsilon_v2': ['BPH'],
	'HLT_DoubleMu8_Mass8_PFHT300_v4': ['SUSY'],
	'HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL_v2': ['EXO'],
	'HLT_Mu17_Mu8_v1': ['HIG'],
	'HLT_PFHT200_v2': ['SUSY'],
        'HLT_RemovePileUpDominatedEventsGenV2_v1' : ['EXO'],
        'HLT_BCToEFilter_v1' : ['EXO'],
        'HLT_EmFilter_v1' : ['EXO'],
        'HLT_EmGlobalFilter_v1' : ['EXO'],
        'HLT_MuFilter_v1' : ['EXO'],
        'HLT_MuFilterTP_v1' : ['EXO']
}

#L1Menu_Collisions2015_25nsStage1_v5

triggersL1GroupMap = {
	'L1_ETM100': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleJet36': ['L1', '262139', '262139', '262139', '7000', '5000', '3000', '1500'],
	'L1_HTT200': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_Mu8_HTT50': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleMuOpen': ['L1', '262139', '262139', '262139', '262139', '262139', '262139', '262139'],
	'L1_SingleIsoEG22er': ['L1', '2000', '2000', '1', '1', '1', '1', '1'],
	'L1_DoubleJetC112': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_HTT125': ['L1', '300', '300', '1', '1', '1', '1', '1'],
	'L1_AlwaysTrue': ['Masked', '1', '1', '1', '1', '1', '1', '1'],
	'L1_DoubleMu0_Eta1p6_WdEta18': ['L1', '2000', '2000', '1', '1', '1', '1', '1'],
	'L1_ETM40': ['L1', '10000', '10000', '7000', '5000', '3500', '2000', '1000'],
	'L1_DoubleIsoTau36er': ['L1', '1000', '1000', '1', '1', '1', '1', '1'],
	'L1_SingleJetC20_NotBptxOR': ['L1', '10', '10', '10', '10', '10', '10', '10'],
	'L1_QuadJetC60': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_DoubleJetC56_ETM60': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleIsoEG18er': ['L1', '3000', '3000', '2000', '1', '1', '1', '1'],
	'L1_SingleIsoEG20': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleIsoEG25': ['L1', '2000', '2000', '1000', '1000', '700', '400', '200'],
	'L1_DoubleEG6_HTT150': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_EG25er_HTT100': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_Mu12_EG10': ['L1', '262139', '262139', '1', '1', '1', '1', '1'],
	'L1_TripleEG_14_10_8': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_DoubleMu_10_Open': ['L1', '2000', '2000', '500', '500', '250', '150', '100'],
	'L1_SingleMu16': ['L1', '1000', '1000', '1', '1', '1', '1', '1'],
	'L1_SingleMu16er': ['L1', '1000', '1000', '1', '1', '1', '1', '1'],
	'L1_SingleMu12': ['L1', '3000', '3000', '70', '70', '18', '10', '5'],
	'L1_ETM50': ['L1', '1000', '1000', '1', '1', '1', '1', '1'],
	'L1_SingleEG5': ['L1', '262139', '262139', '262139', '262139', '262139', '262139', '262139'],
	'L1_SingleMuBeamHalo': ['Masked', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleMu7': ['L1', '262139', '250', '125', '125', '75', '50', '25'],
	'L1_SingleMu14er': ['L1', '1000', '1000', '200', '200', '100', '75', '50'],
	'L1_TripleMu_5_5_3': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_DoubleEG_15_10': ['L1', '1000', '1000', '1', '1', '1', '1', '1'],
	'L1_Mu0er_ETM40': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_QuadJetC36_TauJet52': ['L1', '20', '20', '10', '7', '5', '3', '2'],
	'L1_HTT100': ['L1', '262139', '262139', '1', '1', '1', '1', '1'],
	'L1_SingleEG10': ['L1', '20000', '15000', '10000', '10000', '5000', '3000', '1500'],
	'L1_SingleIsoEG25er': ['L1', '1000', '1000', '1', '1', '1', '1', '1'],
	'L1_DoubleJetC84': ['L1', '700', '700', '1', '1', '1', '1', '1'],
	'L1_SingleEG15': ['L1', '24000', '24000', '12000', '12000', '7', '4', '2'],
	'L1_Mu5_DoubleEG5': ['L1', '262139', '262139', '262139', '262139', '262139', '262139', '262139'],
	'L1_Mu4_EG18': ['L1', '10000', '10000', '1', '1', '1', '1', '1'],
	'L1_ETT60': ['L1', '262139', '262139', '262139', '262139', '262139', '262139', '262139'],
	'L1_SingleJetC32_NotBptxOR': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleJet128': ['L1', '1000', '1000', '1', '1', '1', '1', '1'],
	'L1_ETM60': ['L1', '900', '900', '1', '1', '1', '1', '1'],
	'L1_DoubleTauJet40er': ['Masked', '1', '1', '1', '1', '1', '1', '1'],
	'L1_QuadMu0': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_Jet32_MuOpen_EG10_MuEGNotWdPhi3_JetMuWdPhi1': ['L1', '150', '150', '80', '60', '40', '20', '10'],
	'L1_DoubleEG_22_10': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_Mu0er_ETM55': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_Jet32_DoubleMu_Open_10_MuMuNotWdPhi23_JetMuWdPhi1': ['L1', '10', '10', '5', '3', '2', '1', '1'],
	'L1_Mu5_EG20': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleEG25': ['L1', '1000', '1000', '1', '1', '1', '1', '1'],
	'L1_SingleEG20': ['L1', '4000', '4000', '2000', '10', '1', '1', '1'],
	'L1_HTT175': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_DoubleIsoTau40er': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_ETM70': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleJet92': ['L1', '3000', '3000', '2000', '2000', '1500', '800', '400'],
	'L1_Mu5_IsoEG18': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_Mu16er_TauJet20er': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_QuadJetC40': ['L1', '1000', '1000', '1', '1', '1', '1', '1'],
	'L1_DoubleIsoTau32er': ['L1', '262139', '262139', '100', '1', '1', '1', '1'],
	'L1_Mu3_JetC52_WdEtaPhi2': ['L1', '15', '15', '10', '7', '5', '3', '1'],
	'L1_Mu6_HTT100': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleEG30': ['L1', '800', '800', '1', '1', '1', '1', '1'],
	'L1_Mu16er_IsoTau32er': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleEG35': ['L1', '500', '500', '1', '1', '1', '1', '1'],
	'L1_ETT40': ['L1', '262139', '262139', '262139', '262139', '262139', '262139', '262139'],
	'L1_ZeroBias': ['L1', '29989', '20000', '15000', '10000', '7500', '5000', '2500'],
	'L1_ETT15_BptxAND': ['L1', '262139', '262139', '262139', '262139', '262139', '262139', '262139'],
	'L1_SingleMu5': ['L1', '262139', '262139', '262139', '262139', '75', '40', '20'],
	'L1_Mu3_JetC16_WdEtaPhi2': ['L1', '400', '400', '200', '150', '100', '50', '25'],
	'L1_TripleJet_92_76_64_VBF': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_DoubleIsoTau28er': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleEG2_BptxAND': ['Masked', '1', '1', '1', '1', '1', '1', '1'],
	'L1_DoubleMu6_EG6': ['L1', '10000', '10000', '1', '1', '1', '1', '1'],
	'L1_DoubleJetC52': ['L1', '10000', '10000', '5000', '5000', '3500', '2000', '1000'],
	'L1_Mu14er_ETM30': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleMuOpen_NotBptxOR': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_HTT150': ['L1', '800', '800', '1', '1', '1', '1', '1'],
	'L1_HTT250': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_Mu10er_ETM50': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_DoubleMu7_EG7': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_DoubleMu_12_5': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_HTT75': ['Masked', '1', '1', '1', '1', '1', '1', '1'],
	'L1_Mu20_EG10': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleEG40': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_DoubleMu_10_3p5': ['L1', '1000', '1000', '1', '1', '1', '1', '1'],
	'L1_Mu16er_IsoTau28er': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_TripleJet_84_68_48_VBF': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_Mu5_EG15': ['L1', '262139', '262139', '1', '1', '1', '1', '1'],
	'L1_SingleIsoEG20er': ['L1', '2000', '2000', '1000', '10', '7', '4', '2'],
	'L1_DoubleMu0_Eta1p6_WdEta18_OS': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleJet200': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleJet68': ['L1', '1500', '1500', '1000', '750', '500', '300', '150'],
	'L1_SingleMu25': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleMu20': ['L1', '700', '700', '1', '1', '1', '1', '1'],
	'L1_DoubleMu_10_0_WdEta18': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleIsoEG30er': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_DoubleMuOpen': ['Masked', '1', '1', '1', '1', '1', '1', '1'],
	#'L1_SingleIsoEG28er': ['Masked', '1000', '1000', '1', '1', '1', '1', '1'],
	'L1_Mu6_DoubleEG10': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_Mu10er_ETM30': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_TripleMu0': ['L1', '100', '100', '1', '1', '1', '1', '1'],
	'L1_SingleMu20er': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_DoubleMu0': ['L1', '300', '300', '150', '150', '105', '60', '30'],
	'L1_DoubleJetC100': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_ETM30': ['L1', '40000', '40000', '20000', '2000', '1500', '800', '400'],
	'L1_SingleJet52': ['L1', '3000', '10000', '6000', '4000', '3000', '1500', '800'],
	'L1_SingleJet176': ['L1', '300', '300', '1', '1', '1', '1', '1'],
	'L1_IsoEG20er_TauJet20er_NotWdEta0': ['L1', '1', '1', '1', '1', '1', '1', '1'],
	'L1_SingleMu30': ['L1', '1', '1', '1', '1', '1', '1', '1']

}

triggersToRemove = [
    ## not in stream A
    'HLT_EcalCalibration_v',
    
    # use UTCA (not simulated in MC)
    'HLT_HcalUTCA_v',
    
    # use NZS (not simulated in MC)
    'HLT_HcalPhiSym_v',
    'HLT_HcalNZS_v',
    
    # fake triggers
    'HLT_BCToEFilter_v',
    'HLT_RemovePileUpDominatedEventsGen_v',
    'HLT_RemovePileUpDominatedEventsGenV2_v',
    'HLT_RemovePileUpDominatedEvents_v',
    'HLT_EmFilter_v',
    'HLT_EmGlobalFilter_v',
    'HLT_MuFilter_v',
    'HLT_MuFilterTP_v',
    'HLT_RemovePileUpDominatedEventsGenV2_v1',
    'HLT_BCToEFilter_v1',
    'HLT_EmFilter_v1',
    'HLT_EmGlobalFilter_v1',
    'HLT_MuFilter_v1',
    'HLT_MuFilterTP_v1',


    # trigger without L1 seeds
    'HLT_Random_v',
    'HLT_Physics_v',
]

triggersGroupMap = dict(triggersGroupMap.items() + triggersL1GroupMap.items())

triggerList = []
L1List = []
HLTList = []
#twoHLTsList = []
groupList = []
twoGroupsList = []
getTriggerString = {}

## Fill triggerList and groupList
for trigger in triggersGroupMap.keys():
    if trigger[:-1] in triggersToRemove: continue
    if not (trigger in triggerList) : triggerList.append(trigger) 
    for group in triggersGroupMap[trigger]:
        if not (group in groupList) and not group.isdigit(): groupList.append(group)

## Fill HLTList and L1List
for trigger in triggerList:
    if "HLT_" in trigger: HLTList.append(trigger)
    elif "L1_" in trigger: L1List.append(trigger)

## Fill getTriggerString get a map from trigger and group names to strings
groupAliasCounter = {}
for trigger in triggerList:
    getTriggerString[trigger]=trigger
#    for group in triggersGroupMap[trigger]:
#        if (group != "L1") and not group.isdigit():
#            if group in getTriggerString.keys(): getTriggerString[group]+='||'+trigger
#            else: getTriggerString[group]=trigger
    for group in triggersGroupMap[trigger]:
        if (group != "L1") and (group != "Masked") and not group.isdigit():
            if group in getTriggerString.keys():
                groupAliasCounter[group] += 1
                getTriggerString[group]+='||'+group+"_"+str(groupAliasCounter[group])
            else:
                groupAliasCounter[group] = 0
                getTriggerString[group]=group+"_0"
        elif (group == "Masked"):
            if group in getTriggerString.keys(): getTriggerString[group]+='||'+trigger
            else: getTriggerString[group]=trigger 
           
## Fill twoGroupsList and getTriggerString
for group1 in groupList:
    for group2 in groupList:
        if (not group1.isdigit()) and (not group2.isdigit()): twoGroups = group1 + "-" + group2
        if not (twoGroups in twoGroupsList) and not ("L1" in twoGroups) and not ("Masked" in twoGroups) and not (group2+"-"+group1 in twoGroupsList):# and (group1 != group2):
            twoGroupsList.append(twoGroups)
            twoGroupsTrigger="("+(getTriggerString[group1])+")&&("+(getTriggerString[group2])+")"
            getTriggerString[twoGroups]=twoGroupsTrigger

### Fill twoHLTsList and getTriggerString
#for trigger1 in HLTList:
#    for trigger2 in HLTList:
#        twoHLTs = trigger1 + "-" + trigger2
#        if not (twoHLTs in twoHLTsList):
#            twoHLTsList.append(twoHLTs)
#            twoHLTsTrigger="("+(getTriggerString[trigger1])+")&&("+(getTriggerString[trigger2])+")"
#            getTriggerString[twoHLTs]=twoHLTsTrigger

## Fill string for All group
groupList.append('All_HLT')
i = 0
for trigger in HLTList:
    if "PPD" not in triggersGroupMap[trigger]: 
        if 'All_HLT' in getTriggerString.keys(): getTriggerString['All_HLT']+='||HLT_'+str(i)
        else: getTriggerString['All_HLT']='HLT_0'
        i += 1

## Creates the global OR string fot all L1 paths 
i = 0
for trigger in L1List:
    if 'L1' in getTriggerString.keys(): getTriggerString['L1']+='||L1_'+str(i)
    else: getTriggerString['L1']='L1_0'
    i += 1

