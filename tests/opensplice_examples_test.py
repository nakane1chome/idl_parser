import os, sys, glob
import unittest
from idl_parser import parser
from idl_parser.type import IDLType

__nocoveralls = False # This might be redundant but just in case ...
try:
    from coveralls import Coveralls
    from coveralls.api import log
except:
    sys.stdout.write('''
#######################################
# 
#   importing "coveralls" failed.
#   
#######################################
''')
    __nocoveralls = True

IDL_DIR = 'idls/opensplice_examples/'

class OpenSpliceExamplesTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_parser(self):
        # find files
        idl_files = glob.glob(IDL_DIR+"*.idl")
        for idl_path in idl_files:
            print("**** Attempt to parse: " + idl_path )
            parser_ = parser.IDLParser()
            with open(idl_path, 'r') as idlf:
                m = parser_.load(idlf.read())


if __name__ == '__main__':
    unittest.main()


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(OpenSpliceExamplesTest))
    return suite
