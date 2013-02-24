#!/usr/bin/env python

# Mateusz Maciejewski, 09/2010
# simple script for renumbering pdb's, use to renumber
# residues and atoms.

import sys
import re

starting_res = int(sys.argv[2])
starting_atom = int(sys.argv[3])
#addenum = 0
n = 0
last_res = -1

for line in open(sys.argv[1]).readlines():

  if line[0:4]=='ATOM' or line[0:4]=='TER ':

    curr_res = line[23:26]
    
    if int(curr_res) != int(last_res) and last_res != -1:
      addenum+=int(curr_res)-int(last_res)
      
    elif last_res == -1:
      addenum = 0
      
    last_res = curr_res
    
    print '%s%5d%s%3d%s' %(line[0:6],(starting_atom+n),line[11:23],(starting_res+addenum),line[26:]),
    
    n+=1

  elif line[0:5]=='MODEL':
    print line,
    n=0

  elif line[0:6]=='ENDMDL':
    
    print line,
 
  else:
    print line,

