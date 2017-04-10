import os
"""
This script uses the Anaconda program called "conda" to create
a new python3 environment called "py35"; Anaconda must be installed
on your computer prior to running this script. Download Anaconda 
at https://www.continuum.io/downloads. To run this script, open a 
command window in the same directory as the script and type:

"python CreatePythonEnvironment.py"  (without the quotation marks)

To use this new python environment, use the "activate" command:

>>C:\\Users\\jbellino> activate py35
"""

# First, create a string that we will feed to the os.system()
# which is the equivalent to typing this in at the command line.
s = 'conda create --name pybb'

# Add the python version we want to create
pyversion = 3.5
s += ' python={}'.format(pyversion)

# Add a few basic packages we'll want to use
pkglst = ['numpy', 'pandas', 'matplotlib', 'jupyter', 'notebook', 'xlrd', 'statsmodels']
for pkg in pkglst:
    s += ' ' + pkg

# This just tells conda to go ahead and build the pacakge without
# user confirmation
s += ' --y'

# Create the environment using the string we just built
os.system(s)
