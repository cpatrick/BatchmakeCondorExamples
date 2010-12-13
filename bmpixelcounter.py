#!/usr/bin/env python

import subprocess as sp
import os
from config import *

scriptBase = 'BMPixelCounter'
scriptName = baseDir + scriptBase + '.bms'
condorScriptName = workingDir + scriptBase + '.dagjob'
sphereDir = workingDir + 'spheres/'
condorSubmitName = condorScriptName + '.condor.sub'

def main():

  try:
    os.mkdir(workingDir)
    print "Creating working directory."
  except OSError:
    print "Working directory present."

  try:
    os.mkdir(sphereDir)
    print "Creating sphere directory."
  except OSError:
    print "Sphere directory present."

  if len(os.listdir(sphereDir)) != 15:
    print "Generating spheres."
    os.chdir(sphereDir)
    sp.call([generateSpheres])
  else:
    print "Spheres present."

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

  # Create wrapper for PixelCounter
  sp.call([batchmake, 
           '-ap', batchmakeAppDir, 
           '-a', pixelCounter,
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
