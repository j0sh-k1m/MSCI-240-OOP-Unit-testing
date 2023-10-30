# run_tests.py
#
# Author: Oliver Schneider
# Email: 
# Student ID: 1234567890
#
# use this to conveniently run your unittests


from test.test_speaker import TestSpeaker
import unittest


# if __name__ == '__main__':
#     unittest.main()



import sys 
  
def main(out = sys.stderr, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite) 
      
if __name__ == '__main__': 
    with open('testing.out', 'w') as f: 
        main(f) 