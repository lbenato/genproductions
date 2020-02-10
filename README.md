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

## cmsDrive commands

Move to the main CMSSW area:
```
cd $CMSSW_BASE/src
```

### GEN-SIM for Heavy Higgs (Matthew's datacards)

In this fragment, the whole process is handled by pythia, no need of external LHE.

#### 2018 Full sim
```
cmsDriver.py Configuration/GenProduction/python/fragment_Matthew.py --fileout file:test_M.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions auto:phase1_2018_realistic --step GEN,SIM --python_filename test_M_1_cfg.py --no_exec -n 5
```
#### 2018 Fast sim
```
cmsDriver.py Configuration/GenProduction/python/fragment_Matthew.py --conditions auto:phase1_2018_realistic --fast  -n 5 --era Run2_2018_FastSim --eventcontent RAWSIM -s GEN,SIM --datatier GEN-SIM --beamspot Realistic25ns13TeVEarly2018Collision --mc --fileout file:test_M_FastSim.root --python_filename test_M_FastSim_1_cfg.py
```

### AODSIM for Heavy Higgs (Matthew's datacards)

#### 2018 Fast sim
```
cmsDriver.py Configuration/GenProduction/python/fragment_Matthew.py --conditions auto:phase1_2018_realistic --fast  -n 5 --era Run2_2018_FastSim --eventcontent AODSIM -s GEN,SIM,RECOBEFMIX,DIGI:pdigi_valid,L1,DIGI2RAW,L1Reco,RECO --datatier GEN-SIM-DIGI-RECO --beamspot Realistic25ns13TeVEarly2018Collision --mc --fileout file:test_M_FastSim_AOD.root --python_filename test_M_FastSim_AOD_1_cfg.py
```

# genproductions
Generator fragments for MC production

The package includes the datacards used for various generators inclusing POWHEG, MG5_aMC@NLO, Sherpa, Phantom, Pythia...

Further details are reported in the twiki: https://twiki.cern.ch/twiki/bin/view/CMS/GeneratorMain#How_to_produce_gridpacks

Instructions on how to use the fragments are here https://twiki.cern.ch/twiki/bin/view/CMS/GitRepositoryForGenProduction
