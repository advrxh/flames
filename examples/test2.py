'''
    running with user input
'''

try:
    import os
    import sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)
except:
    pass

from pyflames import Flames

name_a = input('NAME - 1: ')
name_b = input('NAME - 2: ')

flame = Flames(name_a, name_b)

print('It seems, {} between you!!'.format(flame.find_it()))
