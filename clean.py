#!/usr/bin/env python

import shutil

ignoreList = open('.gitignore')
for line in ignoreList.readlines():
  try:
    shutil.rmtree(line[:-1])
  except OSError:
    pass
