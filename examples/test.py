'''
    on running without user input
'''

try:
    import os
    import sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)
except:
    pass

from flames import Flames


flame = Flames('John Doe', 'Jane Doe')
print(flame.find_it())
