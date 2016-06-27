# -*- coding: iso-8859-15 -*-#master:                                        ±  Hz STEAM rates evaluated on the Spring'15 samples, corresponding to a luminoity of 5e33 cm⁻²s⁻¹ with the menu
#same as: /frozen/2015/50ns_5e33/v2.2/HLT/V2                                         

triggerList = []
triggerName = "_frozen_2015_50ns_5e33_v2p2_HLT_V2"

triggersGroupMap = {
	'HLT_PFHT400_SixJet30_BTagCSV0p55_2PFBTagCSV0p72_v2': ['NoGroup'],
	'HLT_L1SingleMu16_v1': ['SMP', 'Muons'],
	'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v1': ['EXO'],
	'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v2': ['EXO'],
	'HLT_HcalCalibration_v1': ['HCAL'],
	'HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v1': ['TAU', 'HIG'],
	'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40_v2': ['HIG'],
	'HLT_DoublePhoton85_v2': ['EXO'],
	'HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing_v1': ['BPH'],
	'HLT_IsoMu20_eta2p1_TriCentralPFJet50_40_30_v2': ['TOP'],
	'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v2': ['EXO'],
	'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v2': ['EXO'],
	'HLT_Photon30_v2': ['SMP', 'EXO'],
	'HLT_DiPFJetAve60_v1': ['JME'],
	'HLT_Mu55_v1': ['EXO'],
	'HLT_Ele15_IsoVVVL_BTagCSV0p72_PFHT400_v2': ['SUSY'],
	'HLT_HT500_DisplacedDijet40_Inclusive_v2': ['EXO'],
	'HLT_Mu20_Mu10_v1': ['HIG'],
	'HLT_Mu16_eta2p1_CaloMET30_v2': ['TAU', 'HIG'],
	'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80_v2': ['HIG'],
	'HLT_Mu10_CentralPFJet30_BTagCSV0p54PF_v2': ['SUSY'],
	'HLT_Mu17_v1': ['SUSY', 'Muons'],
	'HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v2': ['EXO'],
	'HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v2': ['EXO'],
	'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_VBF_v2': ['HIG'],
	'HLT_Mu3er_PFHT140_PFMET125_NoiseCleaned_v2': ['SUSY'],
	'HLT_Ele32_eta2p1_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v1': ['TOP'],
	'HLT_Ele27_eta2p1_WPLoose_Gsf_TriCentralPFJet30_v1': ['TOP'],
	'HLT_Ele115_CaloIdVT_GsfTrkIdT_v1': ['EXO'],
	'HLT_PFJet400_v2': ['SMP', 'B2G'],
	'HLT_Photon36_R9Id90_HE10_IsoM_v2': ['SMP', 'SUSY'],
	'HLT_AK4PFJet100_v2': ['HIN'],
	'HLT_Mu17_TkMu8_DZ_v2': ['TOP', 'HIG', 'SMP'],
	'HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV0p54PF_v2': ['SUSY'],
	'HLT_QuadPFJet_VBF_v2': ['HIG'],
	'HLT_L1Tech_HBHEHO_totalOR_v1': ['FSQ'],
	'HLT_Ele27_eta2p1_WPLoose_Gsf_v1': ['Egamma', 'HIG', 'SMP'],
	'HLT_Photon50_R9Id90_HE10_IsoM_v2': ['SMP', 'SUSY'],
	'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1': ['HIG'],
	'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v2': ['EXO'],
	'HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v2': ['EXO'],
	'HLT_Mu7p5_Track3p5_Jpsi_v2': ['BPH'],
	'HLT_PFHT800_v1': ['SUSY'],
	'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v2': ['SUSY'],
	'HLT_QuadPFJet_DoubleBTagCSV_VBF_Mqq240_v2': ['HIG'],
	'HLT_Rsq0p30_v1': ['SUSY'],
	'HLT_DiPFJetAve320_v1': ['JME'],
	'HLT_IsoMu16_eta2p1_CaloMET30_LooseIsoPFTau50_Trk30_eta2p1_v2': ['TAU', 'HIG'],
	'HLT_DiPFJetAve80_HFJEC_v2': ['JME'],
	'HLT_PixelTracks_Multiplicity135ForEndOfFill_v1': ['FSQ', 'HIN'],
#	'HLT_PixelTracks_Multiplicity135_v1': ['FSQ', 'HIN'],
	'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v2': ['HIG', 'SMP'],
	'HLT_IsoMu24_eta2p1_TriCentralPFJet30_v2': ['TOP'],
	'HLT_Dimuon6_Jpsi_NoVertexing_v1': ['BPH'],
	'HLT_MonoCentralPFJet80_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v2': ['EXO'],
	'HLT_IsoMu24_eta2p1_LooseIsoPFTau20_v2': ['TAU', 'HIG'],
	'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40_v2': ['HIG'],
	'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52_v1': ['SUSY'],
	'HLT_TkMu20_v2': ['SMP'],
	'HLT_IsoMu20_v2': ['SMP', 'TOP', 'Muons'],
	'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v2': ['EXO', 'SUSY'],
	'HLT_TripleMu_12_10_5_v1': ['HIG'],
	'HLT_Photon90_CaloIdL_PFHT500_v2': ['SUSY', 'EXO'],
	'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v2': ['TAU', 'HIG'],
	'HLT_Physics_v1': ['TSG', 'Alca', 'Tracker'],
	'HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL_v2': ['EXO'],
	'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF_v2': ['HIG'],
	'HLT_PFJet450_v2': ['SMP', 'B2G'],
	'HLT_Photon90_CaloIdL_PFHT600_v1': ['EXO'],
	'HLT_MET60_IsoTrk35_Loose_v1': ['EXO'],
	'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v1': ['SUSY'],
	'HLT_Rsq0p25_v1': ['SUSY'],
	'HLT_Mu12_Photon25_CaloIdL_v2': ['HIG'],
	'HLT_DiPFJetAve140_v1': ['JME'],
	'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v2': ['EXO'],
	'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v2': ['TAU', 'HIG'],
	'HLT_CaloJet500_NoJetID_v2': ['EXO'],
	'HLT_Dimuon10_Jpsi_Barrel_v1': ['BPH'],
	'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v2': ['HIG', 'SMP'],
	'HLT_IsoMu17_eta2p1_MediumIsoPFTau40_Trk1_eta2p1_Reg_v2': ['TAU', 'HIG'],
	'HLT_PixelTracks_Multiplicity110ForEndOfFill_v1': ['FSQ', 'HIN'],
#	'HLT_PixelTracks_Multiplicity110_v1': ['FSQ', 'HIN'],
	'HLT_JetE70_NoBPTX3BX_NoHalo_v2': ['EXO'],
	'HLT_RsqMR270_Rsq0p09_MR200_v1': ['SUSY'],
	'HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v2': ['EXO'],
	'HLT_ZeroBias_v1': ['TSG', 'L1', 'AlCa', 'Tracker', 'Lumi'],
	'HLT_Photon75_R9Id90_HE10_IsoM_v2': ['SMP', 'SUSY'],
	'HLT_Photon120_R9Id90_HE10_IsoM_v2': ['SMP', 'SUSY'],
	'HLT_Ele22_eta2p1_WPTight_Gsf_v1': ['TAU', 'HIG'],
	'HLT_PFJet80_v2': ['SMP'],
	'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v1': ['SUSY'],
	'HLT_HT2500_v1': ['Hotline'],
	'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v2': ['EXO', 'SUSY'],
	'HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight_v2': ['EXO'],
	'HLT_PFHT400_v1': ['SUSY'],
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v2': ['HIG', 'TOP', 'SMP', 'B2G'],
	'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v2': ['TAU', 'HIG'],
	'HLT_DiPFJetAve100_HFJEC_v2': ['JME'],
	'HLT_QuadPFJet_DoubleBTagCSV_VBF_Mqq200_v2': ['HIG'],
	'HLT_DoubleMu4_JpsiTrk_Displaced_v2': ['BPH'],
	'HLT_HT350_DisplacedDijet80_DisplacedTrack_v2': ['EXO'],
	'HLT_FullTrack50_v2': ['HIN'],
	'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v2': ['SUSY'],
	'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v1': ['TAU', 'HIG'],
	'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF_v2': ['HIG'],
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v2': ['TOP', 'HIG', 'SMP', 'B2G'],
	'HLT_Mu24_eta2p1_v1': ['SMP'],
	'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v2': ['HIG'],
	'HLT_Ele33_CaloIdM_TrackIdM_PFJet30_v2': ['SUSY'],
	'HLT_Mu12_Photon25_CaloIdL_L1ISO_v2': ['HIG'],
	'HLT_RsqMR270_Rsq0p09_MR200_4jet_v1': ['SUSY'],
	'HLT_Mu17_Photon30_CaloIdL_L1ISO_v2': ['HIG'],
	'HLT_JetE50_NoBPTX3BX_NoHalo_v2': ['EXO'],
	'HLT_QuadMuon0_Dimuon0_Jpsi_v1': ['BPH'],
	'HLT_Mu17_Mu8_SameSign_DZ_v1': ['HIG', 'B2G'],
	'HLT_Ele15_PFHT300_v2': ['SUSY'],
	'HLT_VBF_DisplacedJet40_TightID_DisplacedTrack_v2': ['EXO'],
	'HLT_AK4CaloJet40ForEndOfFill_v1': ['HIN'],
	'HLT_HISinglePhoton15_v2': ['HIN'],
	'HLT_Photon120_v2': ['SMP', 'EXO'],
	'HLT_DoubleMu38NoFiltersNoVtx_v1': ['EXO'],
	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v2': ['HIG', 'TOP', 'SMP'],
	'HLT_BTagMu_Jet300_Mu5_v2': ['BTV'],
	'HLT_JetE30_NoBPTX_v2': ['EXO'],
	'HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v1': ['TAU', 'HIG'],
	'HLT_Mu300_v1': ['Hotline'],
	'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v1': ['HIG'],
	'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v1': ['EXO'],
	'HLT_HcalUTCA_v1': ['HCAL'],
	'HLT_Ele27_eta2p1_WPTight_Gsf_v1': ['Egamma'],
	'HLT_Mu25_TkMu0_dEta18_Onia_v2': ['BPH', 'SMP'],
	'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v1': ['HIG'],
	'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v2': ['B2G'],
	'HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v2': ['EXO'],
#	'HLT_PixelTracks_Multiplicity85ForEndOfFill_v1': ['FSQ', 'HIN'],
	'HLT_PixelTracks_Multiplicity85_v2': ['FSQ', 'HIN'],
	'HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v2': ['EXO'],
	'HLT_L2Mu10_NoVertex_NoBPTX_v1': ['EXO'],
	'HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet50_40_30_v1': ['TOP'],
	'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p45_v2': ['B2G'],
	'HLT_PFJet320_v2': ['SMP'],
	'HLT_DiSC30_18_EIso_AND_HE_Mass70_v1': ['ECAL'],
	'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v2': ['BPH'],
	'HLT_Mu16_TkMu0_dEta18_Onia_v2': ['BPH', 'SMP'],
	'HLT_PFHT450_SixJet40_v2': ['HIG'],
	'HLT_DiPFJetAve200_v1': ['JME'],
	'HLT_BTagMu_DiJet40_Mu5_v2': ['BTV'],
	'HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq500_v2': ['HIG'],
	'HLT_PFHT250_v1': ['SUSY'],
	'HLT_Dimuon8_PsiPrime_Barrel_v1': ['BPH'],
	'HLT_Mu7p5_Track7_Jpsi_v2': ['BPH'],
	'HLT_Photon500_v1': ['Hotline'],
	'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v1': ['HIG', 'SMP'],
	'HLT_HIL1DoubleMu0_v1': ['HIN'],
	'HLT_PFJet260_v2': ['JME', 'SMP'],
	'HLT_PFHT600_v2': ['SUSY', 'EXO'],
	'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v2': ['Muons'],
	'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55_v1': ['SUSY'],
	'HLT_Mu16_TkMu0_dEta18_Phi_v2': ['BPH'],
	'HLT_Mu50_eta2p1_v1': ['EXO'],
	'HLT_PFMET120_NoiseCleaned_Mu5_v2': ['SUSY'],
	'HLT_IsoMu20_eta2p1_TriCentralPFJet30_v2': ['TOP'],
	'HLT_IsoMu16_eta2p1_CaloMET30_v2': ['TAU', 'HIG'],
	'HLT_Mu15_IsoVVVL_PFHT350_PFMET70_v1': ['SUSY'],
	'HLT_Ele18_CaloIdM_TrackIdM_PFJet30_v2': ['SUSY'],
	'HLT_Mu50_v1': ['EXO', 'B2G'],
	'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40_v2': ['HIG'],
	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v2': ['HIG', 'TOP', 'SMP'],
	'HLT_VBF_DisplacedJet40_TightID_Hadronic_v2': ['EXO'],
	'HLT_Photon50_v2': ['SMP', 'EXO'],
	'HLT_IsoTrackHE_v1': ['HCAL'],
	'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v2': ['HIG', 'SMP'],
	'HLT_Photon175_v2': ['SMP', 'EXO'],
	'HLT_FullTrack12ForEndOfFill_v1': ['HIN'],
	'HLT_PFMET90_PFMHT90_IDTight_v1': ['HIG'],
	'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v2': ['HIG'],
	'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v2': ['EXO', 'B2G'],
	'HLT_Dimuon13_PsiPrime_v1': ['BPH'],
	'HLT_Mu7p5_Track2_Upsilon_v2': ['BPH'],
	'HLT_QuadJet45_TripleBTagCSV0p67_v2': ['HIG'],
	'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v2': ['SUSY'],
	'HLT_HISinglePhoton60_v2': ['HIN', 'Egamma'],
	'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v1': ['EXO'],
	'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v2': ['EXO'],
	'HLT_IsoMu17_eta2p1_v2': ['TAU', 'HIG', 'Muons'],
	'HLT_DiCentralPFJet55_PFMET110_NoiseCleaned_v1': ['SUSY'],
	'HLT_IsoTkMu20_eta2p1_v2': ['SMP', 'TOP'],
	'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_PFMET40_v2': ['HIG'],
	'HLT_PFHT650_4Jet_v2': ['EXO'],
	'HLT_DoubleJet90_Double30_TripleBTagCSV0p67_v2': ['HIG'],
	'HLT_DiPFJetAve260_v1': ['JME'],
	'HLT_DoubleJet90_Double30_DoubleBTagCSV0p67_v2': ['HIG'],
	'HLT_PFJet60_v2': ['SMP'],
	'HLT_Mu7p5_Track2_Jpsi_v2': ['BPH'],
	'HLT_L1_TripleJet_VBF_v1': ['HIG'],
	'HLT_Photon165_R9Id90_HE10_IsoM_v2': ['HIG', 'SUSY', 'SMP'],
	'HLT_PFJet500_v2': ['SMP', 'B2G'],
	'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF_v2': ['HIG'],
	'HLT_IsoTkMu27_v2': ['SMP', 'HIG'],
	'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40_v2': ['HIG'],
	'HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v2': ['EXO'],
	'HLT_Photon90_R9Id90_HE10_IsoM_v2': ['SMP', 'SUSY'],
	'HLT_Ele105_CaloIdVT_GsfTrkIdT_v2': ['EXO', 'B2G'],
	'HLT_QuadJet45_DoubleBTagCSV0p67_v2': ['HIG'],
	'HLT_Diphoton30_18_Solid_R9Id_AND_IsoCaloId_AND_HE_R9Id_Mass55_v1': ['HIG', 'SMP'],
	'HLT_IsoMu20_eta2p1_v2': ['TOP', 'TAU'],
	'HLT_DoubleMu4_3_Jpsi_Displaced_v1': ['BPH'],
	'HLT_Ele27_eta2p1_WPLoose_Gsf_TriCentralPFJet50_40_30_v1': ['TOP'],
	'HLT_IsoTkMu20_v2': ['SMP', 'TOP'],
	'HLT_AK4PFJet80_v2': ['HIN'],
	'HLT_PFHT550_4Jet_v2': ['EXO'],
	'HLT_Mu15_IsoVVVL_PFHT600_v2': ['SUSY'],
	'HLT_Photon22_v2': ['SMP', 'EXO'],
	'HLT_Ele32_eta2p1_WPLoose_Gsf_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1': ['TAU', 'HIG', 'EXO'],
	'HLT_HT350_DisplacedDijet40_DisplacedTrack_v2': ['EXO'],
	'HLT_AK4CaloJet100_v2': ['HIN'],
	'HLT_HISinglePhoton10_v2': ['HIN'],
	'HLT_CaloMET200_NoiseCleaned_v2': ['EXO'],
	'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v2': ['SUSY'],
	'HLT_BTagMu_DiJet20_Mu5_v2': ['BTV'],
	'HLT_AK8PFJet360_TrimMass30_v2': ['B2G'],
	'HLT_HT750_DisplacedDijet80_Inclusive_v2': ['EXO'],
	'HLT_DiPFJetAve300_HFJEC_v2': ['JME'],
	'HLT_Ele15_IsoVVVL_PFHT600_v2': ['SUSY'],
	'HLT_Dimuon0er16_Jpsi_NoVertexing_v1': ['BPH'],
	'HLT_Mu8_v1': ['SUSY'],
	'HLT_IsoTrackHB_v1': ['HCAL'],
	'HLT_JetE30_NoBPTX3BX_NoHalo_v2': ['EXO'],
	'HLT_DiPFJetAve80_v1': ['JME'],
	'HLT_PFMET100_PFMHT100_IDTight_v1': ['HIG'],
	'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v1': ['HIG'],
	'HLT_HIL2Mu3_v2': ['HIN'],
	'HLT_Mu40_TkMu11_v2': ['EXO'],
	'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v2': ['HIG'],
	'HLT_BTagMu_DiJet70_Mu5_v2': ['BTV'],
	'HLT_Mu20_v1': ['SMP', 'Muons'],
	'HLT_AK4CaloJet30ForEndOfFill_v1': ['HIN'],
	'HLT_Photon75_v2': ['SMP', 'EXO'],
	'HLT_Mu24_TrkIsoVVL_v2': ['SUSY'],
	'HLT_PFMET120_NoiseCleaned_BTagCSV0p72_v2': ['SUSY'],
	'HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL_v2': ['EXO'],
	'HLT_HIL2DoubleMu0_v2': ['HIN'],
	'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_NoHalo_v1': ['EXO'],
	'HLT_Mu7p5_L2Mu2_Upsilon_v1': ['BPH'],
	'HLT_Mu7p5_Track7_Upsilon_v2': ['BPH'],
	'HLT_L1SingleMuOpen_v1': ['Muons'],
	'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v1': ['SUSY'],
	'HLT_RsqMR240_Rsq0p09_MR200_v1': ['SUSY'],
	'HLT_Ele32_eta2p1_WPLoose_Gsf_v1': ['HIG', 'Egamma', 'SMP'],
	'HLT_Ele25WP60_SC4_Mass55_v2': ['Egamma'],
	'HLT_DiPFJetAve160_HFJEC_v2': ['JME'],
	'HLT_Mu34_v1': ['SUSY'],
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v2': ['Muons', 'SMP'],
	'HLT_Ele23_WPLoose_Gsf_v1': ['SMP'],
	'HLT_Activity_Ecal_SC7_v1': ['ECAL'],
	'HLT_Random_v1': ['AlCa', 'Tracker'],
	'HLT_PFJet140_v2': ['SMP'],
	'HLT_Dimuon8_Upsilon_Barrel_v1': ['BPH'],
	'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET80_v2': ['TAU', 'HIG'],
	'HLT_Mu27_TkMu8_v2': ['EXO', 'B2G'],
	'HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq460_v2': ['HIG'],
	'HLT_L1Tech_DT_GlobalOR_v1': ['DT'],
	'HLT_DiPFJetAve220_HFJEC_v2': ['JME'],
	'HLT_Mu6_PFHT200_PFMET80_NoiseCleaned_BTagCSV0p72_v1': ['SUSY'],
	'HLT_DoubleMu4_3_Bs_v1': ['BPH'],
	'HLT_PFHT350_v2': ['SUSY', 'EXO'],
	'HLT_PFMET170_v1': ['SUSY', 'EXO', 'B2G'],
	'HLT_DiPFJetAve60_HFJEC_v2': ['JME'],
	'HLT_QuadMuon0_Dimuon0_Upsilon_v1': ['BPH'],
	'HLT_L2Mu10_v1': ['Muons'],
	'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF_v2': ['HIG'],
	'HLT_Photon135_PFMET100_NoiseCleaned_v2': ['EXO'],
	'HLT_VBF_DisplacedJet40_DisplacedTrack_v2': ['EXO'],
	'HLT_MET90_IsoTrk50_v2': ['EXO'],
	'HLT_Ele18_CaloIdL_TrackIdL_IsoVL_PFJet30_v2': ['SUSY'],
	'HLT_HISinglePhoton20_v2': ['HIN'],
	'HLT_ECALHT800_v1': ['EXO'],
	'HLT_TkMu27_v2': ['SMP'],
	'HLT_PFMET110_PFMHT110_IDTight_v1': ['HIG'],
	'HLT_Mu17_Photon35_CaloIdL_L1ISO_v2': ['HIG'],
	'HLT_BTagMu_DiJet110_Mu5_v2': ['BTV'],
	'HLT_DoubleMu33NoFiltersNoVtx_v1': ['EXO'],
	'HLT_Mu45_eta2p1_v1': ['EXO', 'B2G'],
	'HLT_Mu34_TrkIsoVVL_v2': ['SUSY'],
	'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v2': ['SUSY'],
	'HLT_Ele22_eta2p1_WPLoose_Gsf_v1': ['Egamma'],
	'HLT_Mu14er_PFMET100_NoiseCleaned_v1': ['SUSY', 'JME'],
	'HLT_VBF_DisplacedJet40_Hadronic_v2': ['EXO'],
	'HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v1': ['EXO'],
	'HLT_PFHT650_v2': ['SUSY', 'EXO'],
	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v2': ['HIG', 'SMP', 'TOP'],
	'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v2': ['TOP', 'HIG', 'SMP', 'B2G'],
	'HLT_Mu17_Mu8_DZ_v1': ['TOP', 'HIG', 'SMP'],
	'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53_v1': ['SUSY'],
	'HLT_Photon90_v2': ['SMP', 'EXO'],
	'HLT_PFMET120_PFMHT120_IDTight_v1': ['HIG'],
	'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40_v2': ['HIG'],
	'HLT_HcalPhiSym_v1': ['HCAL'],
	'HLT_PFMET170_NoiseCleaned_v2': ['SUSY', 'EXO', 'B2G'],
	'HLT_Ele33_CaloIdL_TrackIdL_IsoVL_PFJet30_v2': ['SUSY'],
	'HLT_MET75_IsoTrk50_v2': ['EXO'],
	'HLT_Ele12_CaloIdM_TrackIdM_PFJet30_v2': ['SUSY'],
	'HLT_MET250_v1': ['Hotline'],
	'HLT_PFMET300_NoiseCleaned_v1': ['Hotline'],
	'HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v2': ['EXO'],
	'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v1': ['HIG'],
	'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v2': ['EXO'],
	'HLT_AK4CaloJet50ForEndOfFill_v1': ['HIN'],
	'HLT_Mu20_Mu10_DZ_v1': ['HIG'],
	'HLT_DiPFJetAve500_v1': ['JME'],
	'HLT_Mu20_Mu10_SameSign_DZ_v1': ['HIG'],
	'HLT_Mu17_TrkIsoVVL_v2': ['SUSY', 'HIG', 'Muons'],
	'HLT_HIL3Mu3_v2': ['HIN'],
	'HLT_MonoCentralPFJet80_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v2': ['EXO'],
	'HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15_v1': ['EXO'],
	'HLT_Ele25WP60_Ele8_Mass55_v2': ['HIG'],
	'HLT_Dimuon0_Phi_Barrel_v1': ['BPH'],
	'HLT_PFMET400_NoiseCleaned_v1': ['Hotline'],
	'HLT_Mu12_Photon25_CaloIdL_L1OR_v2': ['HIG'],
	'HLT_PFHT475_v1': ['SUSY'],
	'HLT_Dimuon20_Jpsi_v1': ['BPH'],
	'HLT_DoubleMu18NoFiltersNoVtx_v1': ['EXO'],
	'HLT_Photon165_HE10_v2': ['SMP', 'SUSY'],
	'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v1': ['SUSY'],
	'HLT_Dimuon0_Jpsi_Muon_v1': ['BPH'],
	'HLT_TkMu24_eta2p1_v2': ['SMP'],
	'HLT_Dimuon13_Upsilon_v1': ['BPH'],
	'HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelSeedMatch_Mass70_v1': ['HIG'],
	'HLT_L1SingleMuOpen_DT_v1': ['DT'],
	'HLT_PFJet40_v2': ['SMP'],
	'HLT_PFHT350_PFMET100_NoiseCleaned_v1': ['SUSY'],
	'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v2': ['EXO'],
	'HLT_DiPFJetAve40_v1': ['JME'],
	'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v2': ['HIG'],
	'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57_v1': ['SUSY'],
	'HLT_IsoMu20_eta2p1_CentralPFJet30_BTagCSV07_v2': ['TOP'],
	'HLT_DoubleIsoMu17_eta2p1_v2': ['HIG', 'TAU'],
	'HLT_AK4CaloJet80_v2': ['HIN'],
	'HLT_L2DoubleMu23_NoVertex_v1': ['EXO'],
	'HLT_IsoMu24_eta2p1_TriCentralPFJet50_40_30_v2': ['TOP'],
	'HLT_HT550_DisplacedDijet40_Inclusive_v2': ['EXO'],
	'HLT_Photon36_v2': ['SMP', 'EXO'],
	'HLT_HISinglePhoton40_v2': ['HIN'],
	'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51_v1': ['SUSY'],
	'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v2': ['HIG'],
	'HLT_Photon30_R9Id90_HE10_IsoM_v2': ['SMP', 'SUSY'],
	'HLT_GlobalRunHPDNoise_v1': ['HCAL'],
	'HLT_PFJet200_v2': ['SMP'],
	'HLT_MET300_v1': ['Hotline'],
	'HLT_Mu8_TrkIsoVVL_v2': ['SUSY', 'HIG', 'SMP'],
	'HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15_v2': ['EXO'],
	'HLT_Photon250_NoHE_v2': ['HIG'],
	'HLT_Ele15_IsoVVVL_PFHT350_PFMET70_v1': ['SUSY'],
	'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v2': ['SUSY'],
#	'HLT_PixelTracks_Multiplicity60ForEndOfFill_v1': ['FSQ', 'HIN'],
	'HLT_PixelTracks_Multiplicity60_v2': ['FSQ', 'HIN'],
	'HLT_Ele27_eta2p1_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v1': ['TOP'],
	'HLT_IsoMu24_eta2p1_v2': ['TOP', 'SMP', 'HIG', 'TAU', 'B2G'],
	'HLT_EcalCalibration_v1': ['ECAL'],
	'HLT_PFHT750_4JetPt50_v1': ['SUSY'],
	'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v2': ['HIG'],
	'HLT_PixelTracks_Multiplicity160ForEndOfFill_v1': ['FSQ', 'HIN'],
#	'HLT_PixelTracks_Multiplicity160_v1': ['FSQ', 'HIN'],
	'HLT_HT2000_v1': ['Hotline'],
	'HLT_PFHT450_SixJet40_PFBTagCSV0p72_v2': ['HIG'],
	'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v1': ['TAU', 'HIG'],
	'HLT_Ele32_eta2p1_WPTight_Gsf_v1': ['HIG', 'Egamma'],
	'HLT_HcalNZS_v1': ['HCAL'],
	'HLT_IsoMu27_v2': ['SMP', 'HIG'],
	'HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet30_v1': ['TOP'],
	'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v2': ['BPH'],
	'HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v1': ['HIG'],
	'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v2': ['HIG', 'SMP'],
	'HLT_PFHT400_SixJet30_v2': ['HIG'],
	'HLT_Mu350_v1': ['Hotline'],
	'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v2': ['EXO', 'B2G'],
	'HLT_Photon300_NoHE_v2': ['HIG'],
	'HLT_Mu15_PFHT300_v2': ['SUSY'],
	'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v2': ['SUSY'],
	'HLT_Photon22_R9Id90_HE10_IsoM_v2': ['SMP', 'SUSY'],
	'HLT_Mu27_v1': ['SMP'],
	'HLT_HT650_DisplacedDijet80_Inclusive_v2': ['EXO'],
	'HLT_Dimuon0_Upsilon_Muon_v1': ['BPH'],
	'HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v1': ['EXO'],
	'HLT_Ele27_eta2p1_WPLoose_Gsf_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1': ['TAU', 'HIG', 'EXO'],
	'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v1': ['SUSY'],
	'HLT_Mu30_TkMu11_v2': ['EXO', 'B2G'],
	'HLT_Mu15_IsoVVVL_BTagCSV0p72_PFHT400_v2': ['SUSY'],
	'HLT_DiPFJetAve400_v1': ['JME'],
	'HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v1': ['HIG', 'SMP'],
	'HLT_IsoTkMu24_eta2p1_v2': ['SMP', 'HIG', 'TOP'],
	'HLT_RsqMR240_Rsq0p09_MR200_4jet_v1': ['SUSY'],
	'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF_v2': ['HIG'],
	'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10_v1': ['EXO'],
	'HLT_Photon600_v1': ['Hotline'],
	'HLT_L1Tech_HCAL_HF_single_channel_v1': ['FSQ'],
	'HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v2': ['EXO'],
	'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v2': ['EXO'],
	'HLT_Mu24_v1': ['EXO'],
	'HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60_v2': ['EXO'],
	'HLT_Dimuon16_Jpsi_v1': ['BPH'],
	'HLT_AK4PFJet30ForEndOfFill_v1': ['HIN'],
	'HLT_Mu17_Mu8_v1': ['HIG'],
	'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v2': ['TAU', 'HIG'],
	'HLT_IsoMu24_eta2p1_CentralPFJet30_BTagCSV07_v2': ['TOP'],
	'HLT_Mu6_PFHT200_PFMET100_NoiseCleaned_v1': ['SUSY', 'JME'],
	'HLT_LooseIsoPFTau50_Trk30_eta2p1_v2': ['TAU', 'HIG'],
	'HLT_PFHT300_v1': ['SUSY'],
	'HLT_Mu7p5_Track3p5_Upsilon_v2': ['BPH'],
	'HLT_DoubleMu8_Mass8_PFHT300_v2': ['SUSY'],
	'HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL_v2': ['EXO'],
	'HLT_AK4PFJet50ForEndOfFill_v1': ['HIN'],
	'HLT_PFHT200_v1': ['SUSY'],
	'HLT_Mu7p5_L2Mu2_Jpsi_v1': ['BPH']
}

#L1Menu_Collisions2015_50nsGct_v3 
triggersL1GroupMap = {
    'L1_ZeroBias' : ['L1'],
    'L1_AlwaysTrue' : ['Masked'],
    'L1_SingleEG2_BptxAND' : ['L1'],
    'L1_SingleJet16' : ['L1'],
    'L1_Mu16er_TauJet40erORCenJet72er' : ['L1'],
    'L1_Mu12_EG10' : ['L1'],
    'L1_Mu5_EG15' : ['L1'],
    'L1_DoubleTauJet40er' : ['L1'],
    'L1_IsoEG20er_TauJet20er_NotWdEta0' : ['L1'],
    'L1_Mu16er_TauJet20er' : ['L1'],
    'L1_QuadJetC84' : ['L1'],
    'L1_DoubleJetC72' : ['L1'],
    'L1_DoubleJetC120' : ['L1'],
    'L1_SingleJet52' : ['L1'],
    'L1_SingleJet68' : ['L1'],
    'L1_SingleJet92' : ['L1'],
    'L1_SingleJet128' : ['L1'],
    'L1_SingleJet176' : ['L1'],
    'L1_SingleJet200' : ['L1'],
    'L1_SingleJet36' : ['L1'],
    'L1_DoubleTauJet36er' : ['L1'],
    'L1_DoubleTauJet44er' : ['L1'],
    'L1_DoubleMu0' : ['L1'],
    'L1_SingleMu30er' : ['L1'],
    'L1_ETT15' : ['Masked'],
    'L1_Mu3_JetC16_WdEtaPhi2' : ['L1'],
    'L1_Mu3_JetC52_WdEtaPhi2' : ['L1'],
    'L1_EG25er_HTT125' : ['L1'],
    'L1_SingleEG35er' : ['L1'],
    'L1_SingleIsoEG25er' : ['L1'],
    'L1_SingleIsoEG25' : ['L1'],
    'L1_SingleIsoEG28er' : ['L1'],
    'L1_SingleIsoEG30er' : ['L1'],
    'L1_SingleEG10' : ['L1'],
    'L1_SingleIsoEG22er' : ['L1'],
    'L1_SingleJet240' : ['L1'],
    'L1_DoubleJetC52' : ['L1'],
    'L1_DoubleJetC84' : ['L1'],
    'L1_SingleMu14er' : ['L1'],
    'L1_DoubleJetC112' : ['L1'],
    'L1_DoubleMu_10_Open' : ['L1'],
    'L1_DoubleMu_10_3p5' : ['L1'],
    'L1_QuadJetC40' : ['L1'],
    'L1_SingleEG5' : ['L1'],
    'L1_SingleEG25' : ['L1'],
    'L1_SingleEG40' : ['L1'],
    'L1_SingleIsoEG18' : ['L1'],
    'L1_SingleIsoEG20er' : ['L1'],
    'L1_SingleEG20' : ['L1'],
    'L1_SingleEG30' : ['L1'],
    'L1_SingleEG35' : ['L1'],
    'L1_SingleMuOpen' : ['L1'],
    'L1_SingleMu16' : ['L1'],
    'L1_SingleEG15' : ['L1'],
    'L1_SingleMu5' : ['L1'],
    'L1_ETT40' : ['Masked'],
    'L1_SingleMu20er' : ['L1'],
    'L1_SingleMu12' : ['L1'],
    'L1_SingleMu20' : ['L1'],
    'L1_SingleMu25er' : ['L1'],
    'L1_SingleMu25' : ['L1'],
    'L1_SingleMu30' : ['L1'],
    'L1_ETM30' : ['L1'],
    'L1_ETM50' : ['L1'],
    'L1_ETM70' : ['L1'],
    'L1_ETM100' : ['L1'],
    'L1_HTT125' : ['L1'],
    'L1_HTT150' : ['L1'],
    'L1_HTT175' : ['L1'],
    'L1_HTT200' : ['L1'],
    'L1_Mu20_EG10' : ['L1'],
    'L1_Mu5_EG20' : ['L1'],
    'L1_Mu5_IsoEG18' : ['L1'],
    'L1_Mu6_DoubleEG10' : ['L1'],
    'L1_SingleJetC32_NotBptxOR' : ['L1'],
    'L1_ETM40' : ['L1'],
    'L1_HTT250' : ['L1'],
    'L1_Mu20_EG8' : ['L1'],
    'L1_Mu6_HTT150' : ['L1'],
    'L1_Mu10er_ETM50' : ['L1'],
    'L1_Mu14er_ETM30' : ['L1'],
    'L1_DoubleMu7_EG7' : ['L1'],
    'L1_SingleMu16er' : ['L1'],
    'L1_Mu8_HTT125' : ['L1'],
    'L1_Mu4_EG18' : ['L1'],
    'L1_SingleMuOpen_NotBptxOR' : ['L1'],
    'L1_DoubleMu6_EG6' : ['L1'],
    'L1_Mu5_DoubleEG5' : ['L1'],
    'L1_DoubleEG6_HTT150' : ['L1'],
    'L1_QuadJetC36_TauJet52' : ['L1'],
    'L1_ETT60' : ['Masked'],
    'L1_ETT90' : ['Masked'],
    'L1_DoubleMuOpen' : ['L1'],
    'L1_TripleMu0' : ['L1'],
    'L1_TripleMu_5_5_3' : ['L1'],
    'L1_SingleJet12_BptxAND' : ['L1'],
    'L1_TripleEG_14_10_8' : ['L1'],
    'L1_DoubleEG_15_10' : ['L1'],
    'L1_DoubleEG_22_10' : ['L1'],
    'L1_DoubleEG_20_10_1LegIso' : ['L1'],
    'L1_Mu0er_ETM55' : ['L1'],
    'L1_DoubleJetC60_ETM60' : ['L1'],
    'L1_DoubleJetC32_WdPhi7_HTT125' : ['L1'],
    'L1_Jet32_DoubleMu_Open_10_MuMuNotWdPhi23_JetMuWdPhi1' : ['L1'],
    'L1_Jet32_MuOpen_EG10_MuEGNotWdPhi3_JetMuWdPhi1' : ['L1'],
    'L1_ETM60' : ['L1'],
    'L1_DoubleJetC100' : ['L1'],
    'L1_QuadJetC60' : ['L1'],
    'L1_SingleJetC20_NotBptxOR' : ['L1'],
    'L1_DoubleJetC56_ETM60' : ['L1'],
    'L1_DoubleMu0_Eta1p6_WdEta18' : ['L1'],
    'L1_ETM60_NotJet52WdPhi2' : ['L1'],
    'L1_ETM70_NotJet52WdPhi2' : ['L1'],
    'L1_ETT130' : ['Masked'],
    'L1_RomanPotsAND' : ['Masked'],
    'L1_TripleJet_92_76_64' : ['L1'],
    'L1_TripleJet_92_76_64_NoFFF' : ['L1'],
    'L1_QuadMu0' : ['L1'],
    'L1_SingleMu18er' : ['L1'],
    'L1_DoubleMu0_Eta1p6_WdEta18_OS' : ['L1'],
    'L1_DoubleMu_12_5' : ['L1'],
    'L1_DoubleMu_10_0_WdEta18' : ['L1'],
    'L1_SingleMuBeamHalo' : ['Masked'],
}
triggersToRemove = [
    # not in stream A
    'HLT_EcalCalibration_v',
    
    # use UTCA (not simulated in MC)
    'HLT_HcalUTCA_v',
    
    # use NZS (not simulated in MC)
    'HLT_HcalPhiSym_v',
    'HLT_HcalNZS_v',
    
    # fake triggers
    'HLT_BCToEFilter_v',
    'HLT_RemovePileUpDominatedEventsGen_v',
    'HLT_RemovePileUpDominatedEvents_v',
    'HLT_EmFilter_v',
    'HLT_EmGlobalFilter_v',
    'HLT_MuFilter_v',
    'HLT_MuFilterTP_v',

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
        if not (group in groupList) : groupList.append(group)

## Fill HLTList and L1List
for trigger in triggerList:
    if "HLT_" in trigger: HLTList.append(trigger)
    elif "L1_" in trigger: L1List.append(trigger)

## Fill getTriggerString get a map from trigger and group names to strings
for trigger in triggerList:
    getTriggerString[trigger]=trigger
    for group in triggersGroupMap[trigger]:
        if group in getTriggerString.keys(): getTriggerString[group]+='||'+trigger
        else: getTriggerString[group]=trigger

## Fill twoGroupsList and getTriggerString
for group1 in groupList:
    for group2 in groupList:
        twoGroups = group1 + "-" + group2
        if not (twoGroups in twoGroupsList):
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
