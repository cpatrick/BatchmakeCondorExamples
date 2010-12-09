#!/usr/bin/env python

# Lib imports
import subprocess as sp
import os

# Configuration
from config import *

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
