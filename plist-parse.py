#!/usr/bin/env python3
import sys
import plistlib as pll
import json


#print('Reading', sys.argv[1])
#pl = pll.readPlist(sys.argv[1])
#print(pl)

with open(sys.argv[1], 'rb') as fd:
    pl = pll.load(fd, fmt=pll.FMT_BINARY)
    # for key in pl['com.apple.CFNetwork.defaultStorageSession']:
    #     print(key)
    print(json.dumps(pl, indent=2))

