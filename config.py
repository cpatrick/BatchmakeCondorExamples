
#!/usr/bin/env python

import subprocess as sp
import os

# Change these variables for your system
batchmakeAppDir = '/home/cpatrick/Builds/BatchMake-Build/bin/'
baseDir = '/home/cpatrick/Source/BatchmakeCondorExamples/'
condorPath = '/usr/bin/'

# Probably don't need to modify these guys
workingDir = baseDir + 'working/'
batchmake =  batchmakeAppDir + 'BatchMake'
bmGridSend = batchmakeAppDir + 'bmGridSend'
bmGridStore = batchmakeAppDir + 'bmGridStore'
pixelCounter = batchmakeAppDir + 'PixelCounter'
generateSpheres = batchmakeAppDir + 'GenerateSpheres'
condorSubmitDag = condorPath + 'condor_submit_dag'
condorSubmit = condorPath + 'condor_submit'
