#!/usr/bin/python3
# ______  ______             
# ___  / / /__(_)__   ______ 
# __  /_/ /__  /__ | / /  _ \
# _  __  / _  / __ |/ //  __/
# /_/ /_/  /_/  _____/ \___/ 
#
# The MIT License (MIT)
#
# Copyright © 2022 8bitgeek at github
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the “Software”), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS 
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
# IN THE SOFTWARE.
import os

test_no=2

def test_path(folder):
    return folder+'/test'+str(test_no)

def test_script():
    return './test'+str(test_no)+'.py'

print(test_path('p2p-framework'))



while os.path.exists(test_path('p2p-framework')) and os.path.isdir(test_path('p2p-framework')):
    print(test_path('p2p-framework'))
    cwd = os.getcwd()
    os.chdir(test_path('p2p-framework'))
    result=os.system(test_script())
    
    print(result)
    os.chdir(cwd)
    test_no+=1


