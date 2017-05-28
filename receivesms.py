#!/usr/bin/env python
from __future__ import print_function
import os
import sys

numparts = int(os.environ['DECODED_PARTS'])

text = ''
# Are there any decoded parts?
if numparts == 0:
    text = os.environ['SMS_1_TEXT']
# Get all text parts
else:
    for i in range(0, numparts):
        varname = 'DECODED_%d_TEXT' % i
        if varname in os.environ:
            text = text + os.environ[varname]

# Do something with the text
print('Number %s have sent text: %s' % (os.environ['SMS_1_NUMBER'], text))