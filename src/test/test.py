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

# given a folder, return the full 
# path to what would be the test script
def test_script_path(folder):
    script_path = folder+'/'+'test.py'
    return script_path

# return true of the folder is a 
# test script folder
def is_test_path(folder):
    return os.path.isfile(test_script_path(folder))

# run a test
def run_test(path):
    if ( is_test_path(path) ):
        status='PASS'
        result=os.system(test_script_path(path))
        if result!=0:
            status='FAIL('+str(result)+')'
        print(status+' '+path)

# itterate the test folders and 
# run each test
def run_unit_tests(path):
    dir_list = os.listdir(path)
    for dir_entry in dir_list:
        test_path=path+'/'+dir_entry
        run_test(test_path)

# itterate the frameworks
def run_framework_tests():
    dir_list = os.listdir('./')
    for dir_entry in dir_list:
        if os.path.isdir(dir_entry):
            run_unit_tests(dir_entry)

run_framework_tests()
