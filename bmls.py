#!/usr/bin/env python

import subprocess as sp
import os

# Change these variables for your system
batchmakeAppDir = '/home/cpatrick/Builds/BatchMake-Build/bin'
baseDir = '/home/cpatrick/Source/BatchmakeCondorExamples'
condorPath = '/usr/bin'

# Probably don't need to modify these guys
workingDir = baseDir + '/working'
batchmake =  batchmakeAppDir + '/BatchMake'
bmGridSend = batchmakeAppDir + '/bmGridSend'
bmGridStore = batchmakeAppDir + '/bmGridStore'
scriptBase = '/BMLS'
scriptName = baseDir + scriptBase + '.bms'
condorScriptName = workingDir + scriptBase + '.dagjob'
condorSubmitName = condorScriptName + '.condor.sub'
condorSubmitDag = condorPath + '/condor_submit_dag'
condorSubmit = condorPath + '/condor_submit'

def main():

  try:
    os.mkdir(workingDir)
    print "Creating working directory."
  except OSError:
    print "Working directory present."
  os.chdir(workingDir)
  

  # Create wrapper for bmGridSend
  sp.call([batchmake, 
           '-ap', batchmakeAppDir, 
           '-a', bmGridSend, 
           '-p', workingDir])

  # Create wrapper for bmGridStore
  sp.call([batchmake, 
           '-ap', batchmakeAppDir, 
           '-a', bmGridStore, 
           '-p', workingDir])

  # Create the condor scripts
  sp.call([batchmake,
           '-ap', batchmakeAppDir,
           '-p', workingDir,
           '--condor', scriptName, condorScriptName])
  
  # Create the condor submit script
  sp.call([condorSubmitDag,
           '-no_submit', '-f', condorScriptName])
  
  # Submit the script to the condor grid
  sp.call([condorSubmit, condorSubmitName])

if __name__ == "__main__":
  main()
