#! /usr/bin/env python

import os, sys, getopt, multiprocessing
import copy, math
from array import array

#mH = [1000,600]
#mS = [150]
#ctaus = [1000, 10000]

DATACARDDIR = 'python/'

def write(mH, mS, ctaus):
    for H in mH:

        for S in mS:

            for c in ctaus:

	        if c==0.05:
	            ci = "0p05"
    	        elif c==0.1:
                    ci = "0p1"
	        else:
	            ci = str(c)


                if c==0:
                    width = 1.9732e-13
                else:
                    width = 1.9732e-13/c #in mm
                #####
                card =   'CROSS_SECTION = 1 # pb \n'
                card +=  'MASS_HIGGS = ' + str(H) + ' # in GeV  \n'
                card +=  'WIDTH_HIGGS   = 0.027*MASS_HIGGS # Same as default for id=35 \n'
                card +=  'MASS_X = ' + str(S) + ' # in GeV  \n'
                card +=  'CTAU_X = ' + str(c) + ' # in mm   \n'
                card +=  'WIDTH_X = ' + str(width) + ' # in mm   \n'
                card +=  '\n'
                card +=  'import FWCore.ParameterSet.Config as cms \n'

                card +=  'from Configuration.Generator.Pythia8CommonSettings_cfi import * \n'
                card +=  '#from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import * #Old Pythia tune \n'
                card +=  'from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import * \n'
                card +=  'from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import * \n'


                card +=  'generator = cms.EDFilter("Pythia8GeneratorFilter", \n'
                card +=  '    pythiaPylistVerbosity = cms.untracked.int32(1), \n'
                card +=  '    filterEfficiency = cms.untracked.double(1), \n'
                card +=  '    pythiaHepMCVerbosity = cms.untracked.bool(False), \n'
                card +=  '    comEnergy = cms.double(13000.), \n'
                card +=  '    crossSection = cms.untracked.double(CROSS_SECTION), \n'
                card +=  '    maxEventsToPrint = cms.untracked.int32(10), \n'
                card +=  '    PythiaParameters = cms.PSet( \n'
 
                card +=  '        pythia8CommonSettingsBlock, \n'
                card +=  '#        pythia8CUEP8M1SettingsBlock, # Old PYTHIA tune \n'
                card +=  '        pythia8CP5SettingsBlock, \n'
                card +=  '        pythia8PSweightsSettingsBlock, \n'
                card +=  '        processParameters = cms.vstring( \n'
                card +=  '            "Higgs:useBSM = on", \n'
                card +=  '            "HiggsBSM:all = off", \n'
                card +=  '# Gluon-fusion production only \n'
                card +=  '#            "HiggsBSM:ffbar2H2 = on", \n'
                card +=  '            "HiggsBSM:gg2H2 = on", \n'
                card +=  '# Long-lived scalar decaying to nunu \n'
                card +=  '            "6000111:new = LL_nunu LLbar_nunu 1 0 0", \n'
                card +=  '            "6000111:m0 = %s" % MASS_X, \n'
                card +=  '            "6000111:mWidth = %s" % WIDTH_X, \n'
                card +=  '            "6000111:tau0 = %s" % CTAU_X, \n'
                card +=  '            "6000111:isResonance = on", \n'
                card +=  '            "6000111:mayDecay = on", \n'
                card +=  '            "6000111:oneChannel = 1  0.333 100 12 -12", \n'
                card +=  '            "6000111:addChannel = 1  0.333 100 14 -14", \n'
                card +=  '            "6000111:addChannel = 1  0.333 100 16 -16", \n'
                card +=  '# Long-lived scalar decaying only to bb \n'
                card +=  '            "6000113:new = LL_b LLbar_b 1 0 0", \n'
                card +=  '            "6000113:m0 = %s" % MASS_X, \n'
                card +=  '            "6000113:mWidth = %s" % WIDTH_X, \n'
                card +=  '            "6000113:tau0 = %s" % CTAU_X, \n'
                card +=  '            "6000113:isResonance = on", \n'
                card +=  '            "6000113:mayDecay = on", \n'
                card +=  '            "6000113:oneChannel = 1 1.0 100 5 -5", \n'
                card +=  '# Shut down H0 decays to ordinary particles and A0 \n'
                card +=  '            "35:m0 = %s" % MASS_HIGGS, \n'
                card +=  '            "35:mWidth = %s" % WIDTH_HIGGS, \n'
                card +=  '            "35:2:bRatio = 0.0", \n'
                card +=  '            "35:3:bRatio = 0.0", \n'
                card +=  '            "35:4:bRatio = 0.0", \n'
                card +=  '            "35:5:bRatio = 0.0", \n'
                card +=  '            "35:7:bRatio = 0.0", \n'
                card +=  '            "35:8:bRatio = 0.0", \n'
                card +=  '# Keep small coupling of H0 to gluons in order to be produced             \n'
                card +=  '#            "35:9:bRatio = 0.0", \n'
                card +=  '            "35:10:bRatio= 0.0", \n'
                card +=  '            "35:12:bRatio= 0.0", \n'
                card +=  '            "35:13:bRatio= 0.0", \n'
                card +=  '            "35:15:bRatio= 0.0", # h0(25)h0(25); would be open at high m(H0) \n'
                card +=  '            "35:18:bRatio= 0.0", # Z0(23)A0(36); would be open at high m(H0) \n'
                card +=  '            "35:36:bRatio= 0.0", # A0(36)A0(36); would be open at high m(H0) \n'
                card +=  '            "35:2:meMode = 100", \n'
                card +=  '            "35:3:meMode = 100", \n'
                card +=  '            "35:4:meMode = 100", \n'
                card +=  '            "35:5:meMode = 100", \n'
                card +=  '            "35:7:meMode = 100", \n'
                card +=  '            "35:8:meMode = 100", \n'
                card +=  '#            "35:9:meMode = 100", \n'
                card +=  '            "35:10:meMode= 100", \n'
                card +=  '            "35:12:meMode= 100", \n'
                card +=  '            "35:13:meMode= 100", \n'
                card +=  '            "35:15:meMode= 100", \n'
                card +=  '            "35:18:meMode= 100", \n'
                card +=  '            "35:20:meMode= 100", \n'
 
                card +=  '# Enable H0-->X(mumu)X(mumu) decay \n'
                card +=  '            "35:addChannel = 1 1. 100 6000113 6000113",# Enable H0-->X(mumu)X(jetjet) decay \n'
                card +=  '#            "35:addChannel = 1 1. 100 6000111 6000113", \n'
                card +=  '            "35:onMode = off", \n'
                card +=  '#`           "35:onIfAny = 6000111 6000113" \n'
                card +=  '            "35:onIfAny = 6000113 6000113" \n'
                card +=  '        ), \n'
    
                card +=  '        parameterSets = cms.vstring( \n'
                card +=  '            "pythia8CommonSettings", \n'
                card +=  '#            "pythia8CUEP8M1Settings", #Old Pythia Tune \n'
                card +=  '            "pythia8CP5Settings", \n'
                card +=  '            "pythia8PSweightsSettings", \n'
                card +=  '            "processParameters" \n'
                card +=  '        ) \n'
                card +=  '    ) \n'
                card +=  ') \n'
 
                ####
                outname = DATACARDDIR + "LO_GluGluH2_H2ToSSTobbbb_MH-"+str(H)+"_MS-"+str(S)+"_ctauS-"+str(ci)+"_13TeV.py"
                cardfile = open(outname, 'w')
                cardfile.write(card)
                cardfile.close()
                print "Written",outname


######
mH = [1000]
mS = [400,150]
ctaus = [500, 1000, 2000, 5000, 10000]
write(mH, mS, ctaus)

######
mH = [600]
mS = [150,50]
ctaus = [500, 1000, 2000, 5000, 10000]
write(mH, mS, ctaus)

######
mH = [400]
mS = [100,50]
ctaus = [500, 1000, 2000, 5000, 10000]
write(mH, mS, ctaus)

######
mH = [200]
mS = [50,25]
ctaus = [500, 1000, 2000, 5000, 10000]
write(mH, mS, ctaus)

######
mH = [125]
mS = [55,25,8]
ctaus = [500, 1000, 2000, 5000, 10000]
write(mH, mS, ctaus)
