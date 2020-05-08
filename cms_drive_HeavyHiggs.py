#! /usr/bin/env python

import os, sys, getopt, multiprocessing
import copy, math
from array import array

def execute_cmsdrive(MH, MS, c, n):
    name = 'GluGluH2_H2ToSSTobbbb_MH-'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_TuneCP5_13TeV-pythia8'
    #GEN-SIM
    #os.system('echo cmsDriver.py Configuration/GenProduction/python/LO_GluGluH2_H2ToSSTobbbb_MH-'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_13TeV.py --fileout file:GluGluH2_H2ToSSTobbbb_MH-'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_output.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN,SIM --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename ' + name + '_cfg_GENSIM.py  --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n '+str(n)+' \n')
    #os.system('cmsDriver.py Configuration/GenProduction/python/LO_GluGluH2_H2ToSSTobbbb_MH-'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_13TeV.py --fileout file:GluGluH2_H2ToSSTobbbb_MH-'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_output.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN,SIM --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename ' + name + '_cfg_GENSIM.py  --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n '+str(n)+' \n')
    #RAW-DIGI
    #os.system('echo cmsDriver.py step2 --filein file:input.root --fileout file:GluGluH2_H2ToSSTobbbb_MH-'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_output.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --procModifiers premix_stage2 --nThreads 8 --geometry DB:Extended --datamix PreMix --era Run2_2018 --python_filename ' + name + '_cfg_RAWDIGI.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n '+str(n)+' \n')
    #os.system('cmsDriver.py step2 --filein file:input.root --fileout file:GluGluH2_H2ToSSTobbbb_MH-'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_output.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --procModifiers premix_stage2 --nThreads 8 --geometry DB:Extended --datamix PreMix --era Run2_2018 --python_filename ' + name + '_cfg_RAWDIGI.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n '+str(n)+' \n')
    #AODSIM
    #os.system('echo cmsDriver.py step3 --filein file:input.root --fileout file:output.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 102X_upgrade2018_realistic_v15 --step RAW2DIGI,L1Reco,RECO,RECOSIM --procModifiers premix_stage2 --nThreads 8 --era Run2_2018 --python_filename GluGluH2_H2ToSSTobbbb_cfg_AODSIM.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n '+str(n)+' \n')
    #os.system('cmsDriver.py step3 --filein file:input.root --fileout file:output.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 102X_upgrade2018_realistic_v15 --step RAW2DIGI,L1Reco,RECO,RECOSIM --procModifiers premix_stage2 --nThreads 8 --era Run2_2018 --python_filename GluGluH2_H2ToSSTobbbb_cfg_AODSIM.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n '+str(n)+' \n')
    #MINIAODSIM
    os.system('echo cmsDriver.py step4 --filein file:input.root --fileout file:output.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 102X_upgrade2018_realistic_v15 --step PAT --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename GluGluH2_H2ToSSTobbbb_cfg_MINIAODSIM.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n '+str(n)+' \n')
    os.system('cmsDriver.py step4 --filein file:input.root --fileout file:output.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 102X_upgrade2018_realistic_v15 --step PAT --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename GluGluH2_H2ToSSTobbbb_cfg_MINIAODSIM.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n '+str(n)+' \n')
    os.system('echo \n')

nevents=50 * 1000

######
mH = [1000]
mS = [400,150]
ctaus = [500, 1000, 2000, 5000, 10000]
for MH in mH:
    for MS in mS:
        for c in ctaus:
            execute_cmsdrive(MH,MS,c,nevents)
exit()
######
mH = [600]
mS = [150,50]
ctaus = [500, 1000, 2000, 5000, 10000]
for MH in mH:
    for MS in mS:
        for c in ctaus:
            execute_cmsdrive(MH,MS,c,nevents)

######
mH = [400]
mS = [100,50]
ctaus = [500, 1000, 2000, 5000, 10000]
for MH in mH:
    for MS in mS:
        for c in ctaus:
            execute_cmsdrive(MH,MS,c,nevents)

######
mH = [200]
mS = [50,25]
ctaus = [500, 1000, 2000, 5000, 10000]
for MH in mH:
    for MS in mS:
        for c in ctaus:
            execute_cmsdrive(MH,MS,c,nevents)

######
mH = [125]
mS = [55,25]
ctaus = [500, 1000, 2000, 5000, 10000]
for MH in mH:
    for MS in mS:
        for c in ctaus:
            execute_cmsdrive(MH,MS,c,nevents)

######
'''
mH = [125]
mS = [20]
ctaus = [500, 1000, 2000, 5000, 10000]
for H in mH:
    for S in mS:
        for c in ctaus:
            execute_cmsdrive(H,S,c,nevents)
'''
