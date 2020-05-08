# Forked branch of genproductions for UHH LLP group

## Instructions
```
bash #if you like bash
source /etc/profile.d/modules.sh #if you like bash
export SCRAM_ARCH=slc6_amd64_gcc700
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsrel CMSSW_10_2_18
cd CMSSW_10_2_18/src
cmsenv
git cms-init
scram b -j 10
```

Clone this forked repo:

```
mkdir -p Configuration
cd Configuration
git clone https://github.com/lbenato/genproductions.git GenProduction
cd $CMSSW_BASE/src
scram b -j 32
```

If you got compilation errors on Configuration/GenProduction/python/ThirteenTeV/DelayedJets/rpvNeutralino/GluinoGluinoToNeutralinoNeutralinoTo2T2B2S_template_cff.py and on Configuration/GenProduction/python/ThirteenTeV/DelayedJets/gluinoGMSB/gluinoGMSB_template.py, comment lines with "@" and put a number (1, for example). It does not impact our fragments.

## Script to produce gen fragments for Heavy Higgs (Matthew's datacards)

In these fragments, the whole process is handled by pythia, no need of external LHE.

```
cd $CMSSW_BASE/src/Configuration/GenProduction
python write_fragments_HeavyHiggs.py
```

Fragments will be saved in `python` folder.

## Script to launch cmsDrive commands

Example for 2018 production (Moriond 2020): https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/EXO-RunIIAutumn18DRPremix-02341

This script creates the needed python files for each step of the generation process. It must be launched from `$CMSSW_BASE/src` folder. Currently it's quite in a raw shape, it requires to comment-uncomment the needed steps (GEN-SIM, etc.).

```
cd $CMSSW_BASE/src
python Configuration/GenProduction/cms_drive_HeavyHiggs_2018.py
```

## Scripts to launch generation via crab

These scripts allow to submit each step of the generation process via crab. They must be copied and launched from `$CMSSW_BASE/src` folder.

```
cp $CMSSW_BASE/src/Configuration/GenProduction/scripts_to_submit/*.py $CMSSW_BASE/src/.
cd $CMSSW_BASE/src
```

* `crab_requests_lists_HeavyHiggs.py` includes dictionaries with the dataset names, crab areas, etc.
* `launch_crab.py` allows the actual submission.

Example for GEN-SIM step:

```
cd $CMSSW_BASE/src
python launch_crab.py -l HeavyHiggs -s GENSIM -a test
```

Possible options:
* `-s` (step) : GENSIM, RAWDIGI, AODSIM, MINIAODSIM
* `-a` (action) : test, submit, resubmit, status, kill, report

## OBSOLETE

Please disregard next section. These were some tests to compare full sim and fast sim.


#### GEN-SIM for Heavy Higgs (Matthew's datacards)

In this fragment, the whole process is handled by pythia, no need of external LHE.
Example for 2018 production (Moriond 2020): https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/EXO-RunIIAutumn18DRPremix-02341

##### 2018 Full sim
Test:

```
cmsDriver.py Configuration/GenProduction/python/fragment_Matthew.py --fileout file:test_M.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions auto:phase1_2018_realistic --step GEN,SIM --python_filename test_M_1_cfg.py --no_exec -n 5
```

Adapted from Moriond 2020 campaign:
```
cmsDriver.py Configuration/GenProduction/python/fragment_Matthew.py --fileout file:test_M.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 102X_upgrade2018_realistic_v15 --step GEN,SIM --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename test_M_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 5
```

##### 2018 Fast sim
Test:
```
cmsDriver.py Configuration/GenProduction/python/fragment_Matthew.py --conditions auto:phase1_2018_realistic --fast  -n 5 --era Run2_2018_FastSim --eventcontent RAWSIM -s GEN,SIM --datatier GEN-SIM --beamspot Realistic25ns13TeVEarly2018Collision --mc --fileout file:test_M_FastSim.root --python_filename test_M_FastSim_1_cfg.py
```

From Moriond 2020 campaign:
```
cmsDriver.py Configuration/GenProduction/python/fragment_Matthew.py --fileout file:test_M_FastSim.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 102X_upgrade2018_realistic_v15 --step GEN,SIM --nThreads 8 --geometry DB:Extended --era Run2_2018_FastSim --fast --python_filename test_M_FastSim_1_cfg.py --no_exec -n 5
```

#### RAW-GEN-SIM for Heavy Higgs (Matthew's datacards)
Recommended dataset for mixing: dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW

##### 2018 Full sim

From Moriond 2020 campaign, full sim, GEN-SIM needed as input:
```
cmsDriver.py --fileout file:test_M.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --procModifiers premix_stage2 --nThreads 8 --geometry DB:Extended --datamix PreMix --era Run2_2018 ---python_filename test_M_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 5
```
##### 2018 Fast sim
From Moriond 2020 campaign, performs everything in one step, but it does not work properly:

```
#cmsDriver.py Configuration/GenProduction/python/fragment_Matthew.py --datamix PreMix --pileup_input "file:PU.root" --fileout file:test_M_FastSim_with_PU.root --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --step GEN,SIM,DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --nThreads 8 --geometry DB:Extended --era Run2_2018_FastSim --fast --python_filename test_M_FastSim_with_PU_1_cfg.py --no_exec -n 5
```

#### AODSIM for Heavy Higgs (Matthew's datacards)

##### 2018 Fast sim
Test. Warning: recipe without pile-up:
```
cmsDriver.py Configuration/GenProduction/python/fragment_Matthew.py --conditions auto:phase1_2018_realistic --fast  -n 5 --era Run2_2018_FastSim --eventcontent AODSIM -s GEN,SIM,RECOBEFMIX,DIGI:pdigi_valid,L1,DIGI2RAW,L1Reco,RECO --datatier GEN-SIM-DIGI-RECO --beamspot Realistic25ns13TeVEarly2018Collision --mc --fileout file:test_M_FastSim_AOD.root --python_filename test_M_FastSim_AOD_1_cfg.py
```

From Moriond 2020 campaign, performs everything in one step, not really working:

   * "HLT" step does not work on FastSim
   * The following lines give tons of errors
```
cmsDriver.py Configuration/GenProduction/python/fragment_Matthew.py --fileout file:test_M_FastSim_no_PU_AOD.root --mc --eventcontent AODSIM --datatier GEN-SIM-DIGI-RECO --conditions 102X_upgrade2018_realistic_v15 --step GEN,SIM,RECOBEFMIX,DIGI:pdigi_valid,L1,DIGI2RAW,L1Reco,RECO --nThreads 8 --geometry DB:Extended --era Run2_2018_FastSim --fast --python_filename test_M_FastSim_no_PU_AOD_1_cfg.py --no_exec -n 5
```


# genproductions
Generator fragments for MC production

The package includes the datacards used for various generators inclusing POWHEG, MG5_aMC@NLO, Sherpa, Phantom, Pythia...

Further details are reported in the twiki: https://twiki.cern.ch/twiki/bin/view/CMS/GeneratorMain#How_to_produce_gridpacks

Instructions on how to use the fragments are here https://twiki.cern.ch/twiki/bin/view/CMS/GitRepositoryForGenProduction
