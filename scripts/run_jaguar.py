from geometric import *
import numpy as np
import sys
import tempfile
import os

def test_pplb(filename, i):
    delta = i / 100.0
    myengine = engine.Jaguar(delta, jaguar_input =filename, threads=7)
    mydir = None
    if 'positive' in filename: mydir = 'jaguar_temp_positive'+str(i)
    else: mydir = 'jaguar_temp_negative'+str(i)
    tmpf = tempfile.mktemp(dir=mydir)
    if not os.path.exists(mydir): os.makedirs(mydir)
    
    a = optimize.run_optimizer(customengine=myengine, input=tmpf, hessian='last')

if __name__=='__main__':
    name, i = sys.argv[1], int(sys.argv[2])
    #neutral = test_neutral(name)
    #charged = test_charged(name)
    test_pplb(name, i)
    #print('Neutral: \n', neutral)
    #print('Charged: \n', charged)
    #print('PPLB:    \n', pplb)
