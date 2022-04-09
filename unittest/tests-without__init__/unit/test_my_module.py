import os, sys

import unittest

module_dir = os.getenv("MY_MODULE_PATH", default=os.getcwd())
sys.path.append(module_dir)
print('a')

#from my_module import Sample
