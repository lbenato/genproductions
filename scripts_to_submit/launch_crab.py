#!/usr/bin/env python
import os
from collections import defaultdict


#######skeleton of config##########
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import sys
config = config()

config.User.voGroup='dcms'

config.General.workArea = 'crab_projects_LLP'
config.General.requestName = 'request'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'python/pset.py'
#enable multi-threading
config.JobType.maxMemoryMB = 7000#15900 #more memory
config.JobType.numCores = 8

#config.Data.outputPrimaryDataset = 'xxxx'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100 #this will create 500 root files
config.Data.totalUnits = 50 * 1000
config.Data.outLFNDirBase = '/store/user/lbenato/xxxx'
config.Data.publication = True
config.Data.outputDatasetTag = 'xxxxx'
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'

config.Site.storageSite = 'T2_DE_DESY'

##fix issues
from multiprocessing import Process
requests = defaultdict(dict)

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    ########parser#######
    import optparse
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser(usage)
    parser.add_option("-a", "--crabaction", action="store", type="string", dest="crabaction", default="test")
    parser.add_option("-l", "--lists", action="store", type="string", dest="lists", default="HeavyHiggs")
    parser.add_option("-s", "--step", action="store", type="string", dest="step", default="GENSIM")
    (options, args) = parser.parse_args()
    requests = {}
    crabConfig = ""
    crab_project_area = ""

    if options.lists == "HeavyHiggs" and options.step == "GENSIM":
        from crab_requests_lists_HeavyHiggs import requests_GENSIM
        requests = requests_GENSIM
        crab_folder = 'crab_projects_private_mc_HeavyHiggs'
        workarea = "/nfs/dust/cms/user/lbenato/" + crab_folder
        config.JobType.pluginName = 'PrivateMC'
        config.General.workArea = workarea

    elif options.lists == "HeavyHiggs" and options.step == "RAWDIGI":
        from crab_requests_lists_HeavyHiggs import requests_RAWDIGI
        requests = requests_RAWDIGI
        config.Data.unitsPerJob = 100
        config.JobType.maxMemoryMB = 15900
        config.Data.splitting = 'EventAwareLumiBased'
        crab_folder = 'crab_projects_private_mc_HeavyHiggs_RAWDIGI'
        workarea = "/nfs/dust/cms/user/lbenato/" + crab_folder
        config.JobType.pluginName = 'Analysis'
        config.General.workArea = workarea

    elif options.lists == "HeavyHiggs" and options.step == "AODSIM":
        from crab_requests_lists_HeavyHiggs import requests_AODSIM
        requests = requests_AODSIM
        config.Data.unitsPerJob = 500
        config.JobType.maxMemoryMB = 7000
        config.Data.splitting = 'EventAwareLumiBased'
        crab_folder = 'crab_projects_private_mc_HeavyHiggs_AODSIM'
        workarea = "/nfs/dust/cms/user/lbenato/" + crab_folder
        config.JobType.pluginName = 'Analysis'
        config.General.workArea = workarea

    elif options.lists == "HeavyHiggs" and options.step == "MINIAODSIM":
        from crab_requests_lists_HeavyHiggs import requests_MINIAODSIM
        requests = requests_MINIAODSIM
        config.Data.unitsPerJob = 1000
        config.JobType.maxMemoryMB = 7000
        config.Data.splitting = 'EventAwareLumiBased'
        crab_folder = 'crab_projects_private_mc_HeavyHiggs_MINIAODSIM'
        workarea = "/nfs/dust/cms/user/lbenato/" + crab_folder
        config.JobType.pluginName = 'Analysis'
        config.General.workArea = workarea

    for a, j in enumerate(requests):
        print j
        config.General.requestName       = requests[j]['requestName']
        config.JobType.psetName          = requests[j]['psetName']
        config.Data.outLFNDirBase        = requests[j]['outLFNDirBase']
        config.Data.outputDatasetTag     = requests[j]['outputDatasetTag']
        if options.step == 'GENSIM':
            config.Data.outputPrimaryDataset = requests[j]['outputPrimaryDataset']
        if not options.step == 'GENSIM':
            config.Data.inputDataset         = requests[j]['inputDataset']
            config.Data.inputDBS             = 'phys03'
        if options.crabaction=="test":
            os.system('echo test: submitting this config...\n')
            print(config)
        elif options.crabaction=="submit":
            os.system('echo submitting this config...\n')
            print(config)
            #submit(config) --> throwing errors, see: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Multiple_submission_fails_with_a
            p = Process(target=submit, args=(config,))
            p.start()
            p.join()
        elif options.crabaction=="status":
            os.system('echo status -d ' + workarea + '/crab_'+requests[j]['requestName']+'\n')
            os.system('crab status -d ' + workarea + '/crab_'+requests[j]['requestName']+'\n')
            os.system('echo ----------------------------------------------------\n') 
        elif options.crabaction=="resubmit":
            os.system('echo resubmit -d ' + workarea + '/crab_'+requests[j]['requestName']+'\n')
            os.system('crab resubmit -d ' + workarea + '/crab_'+requests[j]['requestName']+'\n')
        elif options.crabaction=="getoutput":
            os.system('echo getoutput -d ' + workarea + '/crab_'+requests[j]['requestName']+'\n')
            os.system('crab getoutput -d ' + workarea + '/crab_'+requests[j]['requestName']+'\n')
        elif options.crabaction=="kill":
            os.system('echo kill -d ' + workarea + '/crab_'+requests[j]['requestName']+'\n')
            os.system('crab kill -d ' + workarea + '/crab_'+requests[j]['requestName']+'\n')
        elif options.crabaction=="report":
            os.system('echo report -d ' + workarea + '/crab_'+requests[j]['requestName']+'\n')
            os.system('crab report -d ' + workarea + '/crab_'+requests[j]['requestName']+'\n')
        else:
            print "Invalid crab action. Please type: -a submit/status/resubmit/getoutput/kill"
            exit()
    
    os.system('echo --------------------------\n') 


#Here: modify the type of config
'''
elif options.lists == "HeavyHiggs" and options.step == "RAWSIM":
    from crab_requests_lists_HeavyHiggs import requests_RAWSIM
    requests = {}
    for a in requests_RAWSIM.keys():
        requests[a] = requests_RAWSIM[a]
    crabConfig = "....py"
    config.JobType.pluginName = 'Analysis'
    config.Data.inputDataset =  '....'
    config.Data.inputDBS = 'phys03'


elif options.lists == "HeavyHiggs" and options.step == "AODSIM":
    from crab_requests_lists_HeavyHiggs import requests_AODSIM
    requests = {}
    for a in requests_AODSIM.keys():
        for b in reduced_masses:
            if "MS-"+str(b) in a:
                requests[a] = requests_AODSIM[a]
    crabConfig = "crabConfig_AODSIM_ggH_5jun.py"
    config.JobType.pluginName = 'Analysis'
    config.Data.inputDataset =  '....'
    config.Data.inputDBS = 'phys03'

elif options.lists == "HeavyHiggs" and options.step == "MINIAODSIM":
    from crab_requests_lists_HeavyHiggs import requests_MINIAODSIM
    print "CALO???"
    requests = {}
    for a in requests_MINIAODSIM.keys():
        for b in reduced_masses:
            if "MS-"+str(b) in a:
                requests[a] = requests_MINIAODSIM[a]
    crabConfig = ".....py"
    config.JobType.pluginName = 'Analysis'
    config.Data.inputDataset =  '....'
    config.Data.inputDBS = 'phys03'
'''







