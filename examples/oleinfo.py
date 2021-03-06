#!/usr/bin/env python
"""
pyvba example: parse ole information
"""

import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pyole import *


def print_usage():
    message = 'Usage: [Option] ' + sys.argv[0] + ' OLEFile\r\n\r\n'
    message += 'Options:\r\n'
    message += '-h\tshow help message\r\n'
    message += '-d\tdebug mode\r\n'
    print message
    

if __name__ == '__main__':
    
    if len(sys.argv) == 2:
        
        try:
            init_logging(False)
            
            olefile = OLEFile(sys.argv[1])
            print olefile.OLEHeader.Signature.encode('hex')
            print olefile.Directory[0].Name
            print olefile.find_object_by_name('Root Entry')
            print olefile.Directory[2].Name
            print olefile.find_object_by_index(2)
            
        except Exception as e:
            print e
            
    elif len(sys.argv) == 3:
        
        if sys.argv[1] == '-d':
            
            init_logging(True)
            
            try:
                olefile = OLEFile(sys.argv[2])
            except Exception as e:
                print e
            
        else:
            print_usage()
    else:
        print_usage()
