#!/usr/bin/env python
from collections import defaultdict

mass_points = {

#    'MH-1000' : {
#        'MH' : 1000,
#        'MS' : [400,150],#[400],#[400,150],
#    },

    'MH-600' : {
        'MH' : 600,
        'MS' : [150,50],
    },

#    'MH-400' : {
#        'MH' : 400,
#        'MS' : [100,50],
#    },

#    'MH-200' : {
#        'MH' : 200,
#        'MS' : [50,25],
#    },

#    'MH-125' : {
#        'MH' : 125,
#        'MS' : [55,25],
#    },
}

ctau = [500, 1000, 2000, 5000, 10000]
#ctau = [500]

requests_GENSIM = defaultdict(dict)

for c in ctau:
    #print 'ctau: ', c
    #lista = ['MH-400']
    #print "xxxxxxxxxxxxxxxxxxxxxxx"
    #print "Submitting only: ", lista
    #print "xxxxxxxxxxxxxxxxxxxxxxx"
    #for MH in lista:
    for MH in mass_points.keys():
        for MS in mass_points[MH]['MS']:
           #print MS
           name = 'GluGluH2_H2ToSSTobbbb_'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_TuneCP5_13TeV-pythia8'
           requestName = name + '_Fall18_GENSIM'
           psetName = name + '_cfg_GENSIM.py'
           outputPrimaryDataset = name + '_PRIVATE-MC'
           outLFNDirBase = '/store/user/lbenato/GluGluH2_H2ToSSTobbbb_'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_Fall18'
           outputDatasetTag = 'RunIIFall18wmGS-102X_upgrade2018_realistic_v11_GENSIM'#TBChecked
           requests_GENSIM[name]['requestName'] = requestName
           requests_GENSIM[name]['psetName'] = psetName
           requests_GENSIM[name]['outputPrimaryDataset'] = outputPrimaryDataset#first string in dataset name
           requests_GENSIM[name]['outLFNDirBase'] = outLFNDirBase#first thing in the files path
           requests_GENSIM[name]['outputDatasetTag'] = outputDatasetTag#second string in dataset



requests_RAWDIGI = defaultdict(dict)

for c in ctau:
    for MH in mass_points.keys():
        for MS in mass_points[MH]['MS']:
           #print MS
           name = 'GluGluH2_H2ToSSTobbbb_'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_TuneCP5_13TeV-pythia8'
           requestName = name + '_Fall18_RAWDIGI'
           psetName = 'GluGluH2_H2ToSSTobbbb_cfg_RAWDIGI.py'
           outputPrimaryDataset = name + '_PRIVATE-MC'
           outLFNDirBase = '/store/user/lbenato/GluGluH2_H2ToSSTobbbb_'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_Fall18'
           outputDatasetTag = 'RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_RAWDIGI'#TBChecked
           inputRandomString = 'xxxxxxx'
           if mass_points[MH]['MH']==1000:
               if MS==400:
                   if   c==500: inputRandomString = 'dfcad4dcc243197616f47c510b252a29'
                   elif c==1000: inputRandomString = '93d49f0b5f4d74eb5e771b588d42163f'
                   elif c==2000: inputRandomString = 'ba939d675dadaac1f785dd4101f5f222'
                   elif c==5000: inputRandomString = '41f78368b521dfce5878b5c576cad2a5'
                   elif c==10000: inputRandomString = '9d26beda62c1ba9d3b25d69e3ecdabca'
               if MS==150:
                   if   c==500: inputRandomString = 'da68ccae1a8c7b50cff0ab0dcb761671'
                   elif c==1000: inputRandomString = 'b6d622ed492c20f56b6c6023b34430e6'
                   elif c==2000: inputRandomString = '250571ab2f000f3ad0177d146cf83a68'
                   elif c==5000: inputRandomString = '9a383855bccf142ac36252e8902d7914'
                   elif c==10000: inputRandomString = 'f8019f0015d78b261e52e908eb7eb3fa'
           elif mass_points[MH]['MH']==600:
               if MS==150:
                   if   c==500: inputRandomString = 'f7c068c84fea56ad8feeafcc4dfcebf8'
                   elif c==1000: inputRandomString = '847948938035fe82c955a59cc87f2f16'
                   elif c==2000: inputRandomString = '534b41fbb6b40345b687a8557cb45312'
                   elif c==5000: inputRandomString = '839d68f4fbb60e2a55e810d400bae2f7'
                   elif c==10000: inputRandomString = '874cc86ad74a26cc62c1dc91a764e0c1'
               if MS==50:
                   if   c==500: inputRandomString = 'cfcc8f1156a5dabe7c6e9f1467846ed8'
                   elif c==1000: inputRandomString = 'ed5226e4d3881740ddf41475d0c8ec96'
                   elif c==2000: inputRandomString = '1de5a2998939046b379751a7fa0a3af1'
                   elif c==5000: inputRandomString = 'e030e3dc3f56c622677d01547e24a0b9'
                   elif c==10000: inputRandomString = 'd1f87ecbe651526fa902cb811f857a28'
           elif mass_points[MH]['MH']==400:
               if MS==100:
                   if   c==500: inputRandomString = 'a372c54d810e53872f2c8897ed22ea4b'
                   elif c==1000: inputRandomString = '921536a0f673fdb870893373564712c2'
                   elif c==2000: inputRandomString = 'f08b31907729272814264402c5668a41'
                   elif c==5000: inputRandomString = '42561556587cafc85cee876556c3c211'
                   elif c==10000: inputRandomString = '62bcf51f14643a31dd3e97e38ade8e48'
               if MS==50:
                   if   c==500: inputRandomString = '2f422adc6ec5b4b970bf1ad323452531'
                   elif c==1000: inputRandomString = '42746fc2c9fd837145f96f0ca35f4890'
                   elif c==2000: inputRandomString = '747565e394b15b386e62fb025891fdee'
                   elif c==5000: inputRandomString = 'ab12b1d6e2fa6a1d9165b52cb27f17d1'
                   elif c==10000: inputRandomString = '9f05a67ab041ab13a3cb7dd4e272cf49'
           elif mass_points[MH]['MH']==200:
               if MS==50:
                   if   c==500: inputRandomString = ''
                   elif c==1000: inputRandomString = ''
                   elif c==2000: inputRandomString = ''
                   elif c==5000: inputRandomString = ''
                   elif c==10000: inputRandomString = ''
               if MS==25:
                   if   c==500: inputRandomString = ''
                   elif c==1000: inputRandomString = ''
                   elif c==2000: inputRandomString = ''
                   elif c==5000: inputRandomString = ''
                   elif c==10000: inputRandomString = ''
           elif mass_points[MH]['MH']==125:
               if MS==55:
                   if   c==500: inputRandomString = ''
                   elif c==1000: inputRandomString = ''
                   elif c==2000: inputRandomString = ''
                   elif c==5000: inputRandomString = ''
                   elif c==10000: inputRandomString = ''
               if MS==25:
                   if   c==500: inputRandomString = ''
                   elif c==1000: inputRandomString = ''
                   elif c==2000: inputRandomString = ''
                   elif c==5000: inputRandomString = ''
                   elif c==10000: inputRandomString = ''
           inputDatasetBase = '/'+outputPrimaryDataset+'/lbenato-RunIIFall18wmGS-102X_upgrade2018_realistic_v11_GENSIM-'+inputRandomString+'/USER'
           requests_RAWDIGI[name]['requestName'] = requestName
           requests_RAWDIGI[name]['psetName'] = psetName
           #requests_RAWDIGI[name]['outputPrimaryDataset'] = outputPrimaryDataset#first string in dataset name
           requests_RAWDIGI[name]['outLFNDirBase'] = outLFNDirBase#first thing in the files path
           requests_RAWDIGI[name]['outputDatasetTag'] = outputDatasetTag#second string in dataset
           requests_RAWDIGI[name]['inputDataset']     = inputDatasetBase

requests_AODSIM = defaultdict(dict)

for c in ctau:
    for MH in mass_points.keys():
        for MS in mass_points[MH]['MS']:
           #print 
           name = 'GluGluH2_H2ToSSTobbbb_'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_TuneCP5_13TeV-pythia8'
           requestName = name + '_Fall18_AODSIM'
           psetName = 'GluGluH2_H2ToSSTobbbb_cfg_AODSIM.py'
           outputPrimaryDataset = name + '_PRIVATE-MC'
           outLFNDirBase = '/store/user/lbenato/GluGluH2_H2ToSSTobbbb_'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_Fall18'
           outputDatasetTag = 'RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_AODSIM'#TBChecked
           inputRandomString = '5aa1749307f00d6302ec929df355f761'
           inputDatasetBase = '/'+outputPrimaryDataset+'/lbenato-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_RAWDIGI-'+inputRandomString+'/USER'
           requests_AODSIM[name]['requestName'] = requestName
           requests_AODSIM[name]['psetName'] = psetName
           #requests_AODSIM[name]['outputPrimaryDataset'] = outputPrimaryDataset#first string in dataset name
           requests_AODSIM[name]['outLFNDirBase'] = outLFNDirBase#first thing in the files path
           requests_AODSIM[name]['outputDatasetTag'] = outputDatasetTag#second string in dataset
           requests_AODSIM[name]['inputDataset']     = inputDatasetBase

requests_MINIAODSIM = defaultdict(dict)

for c in ctau:
    for MH in mass_points.keys():
        for MS in mass_points[MH]['MS']:
           #print 
           name = 'GluGluH2_H2ToSSTobbbb_'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_TuneCP5_13TeV-pythia8'
           requestName = name + '_Fall18_MINIAODSIM'
           psetName = 'GluGluH2_H2ToSSTobbbb_cfg_MINIAODSIM.py'
           outputPrimaryDataset = name + '_PRIVATE-MC'
           outLFNDirBase = '/store/user/lbenato/GluGluH2_H2ToSSTobbbb_'+str(MH)+'_MS-'+str(MS)+'_ctauS-'+str(c)+'_Fall18'
           outputDatasetTag = 'RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_MINIAODSIM'#TBChecked
           inputRandomString = '51dbace3c073d03a4eeb2fde7d5a06e2'
           inputDatasetBase = '/'+outputPrimaryDataset+'/lbenato-RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_AODSIM-'+inputRandomString+'/USER'
           requests_MINIAODSIM[name]['requestName'] = requestName
           requests_MINIAODSIM[name]['psetName'] = psetName
           requests_MINIAODSIM[name]['outLFNDirBase'] = outLFNDirBase#first thing in the files path
           requests_MINIAODSIM[name]['outputDatasetTag'] = outputDatasetTag#second string in dataset
           requests_MINIAODSIM[name]['inputDataset']     = inputDatasetBase

#for a in requests_AODSIM.keys():
#    print a
#    print requests_AODSIM[a]
#exit()

'''
requests_RAWDIGI = {
#ggH2, MH-1000 MS-400
#
    'GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-1000_TuneCP5_13TeV-pythia8' : {
        'requestName' : 'GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-1000_TuneCP5_13TeV-pythia8_Fall18_RAWDIGI',
        'psetName' : 'GluGluH2_H2ToSSTobbbb_cfg_RAWDIGI.py',
        'inputDataset' : '/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC/lbenato-RunIIFall18wmGS-102X_upgrade2018_realistic_v11_GENSIM-93d49f0b5f4d74eb5e771b588d42163f/USER',
        'outLFNDirBase' : '/store/user/lbenato/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-1000_Fall18',
        'outputPrimaryDataset' : 'GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC',
        'outputDatasetTag' : 'RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_RAWDIGI',
        },
}
'''
