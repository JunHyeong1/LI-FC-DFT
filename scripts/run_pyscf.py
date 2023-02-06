from geometric import *
import numpy as np
from pyscf import gto
from pyscf import lib
from pyscf import hessian
from pyscf.dft import uks
from pyscf.hessian.uks import Hessian
from pyscf.hessian import thermo
from pyscf.geomopt import geometric_solver
from pyscf.tools import molden
import sys
import tempfile
import os

def test_pplb(filename, i):
    output = open('output_negative' + str(i) + '.csv', 'w')
    mol = gto.M(atom=filename, basis='631+g**')
    mol.output='output_negative'+str(i)+'.log'
    mol.charge, mol.spin = 1, 1
    delta = i / 10.0
    myengine = engine.PySCF(mol, i / 10.0, xc = 'cam-b3lyp')
    myengine.maxsteps = 100
    myengine.mol = mol.copy()
    
    tmpf = tempfile.mktemp(dir=lib.param.TMPDIR)
    
    a = optimize.run_optimizer(customengine=myengine, input=tmpf)
    pplb_energy = a[0].qm_energies[-1]
    neutral = a[1]
    charged = a[2]
    myoutput = 'pplb_opt_negative_'+str(delta)+'.xyz'
    print('Saving xyz file... to ', myoutput)
    neutral.mol.tofile(myoutput, format='xyz')
    print('hessian neutral started')
    hess_neutral = hessian.uks.Hessian(neutral).kernel()
    print('hessian charged started')
    hess_charged = hessian.uks.Hessian(charged).kernel()
    neutral_thermo = thermo.harmonic_analysis(neutral.mol, hess_neutral)
    charged_thermo = thermo.harmonic_analysis(charged.mol, hess_charged)
    pplb_hessian = (1.0 - delta) * hess_neutral + delta * hess_charged
    pplb_thermo = thermo.harmonic_analysis(neutral.mol, pplb_hessian)
    output.write(str(delta) + ',' + str(pplb_energy))
    #output.write(',' + str(pplb_thermo['freq_wavenumber']))
    output.close()

    for idx, mode in enumerate(pplb_thermo['norm_mode']):
        myfile = 'norm_mode_negative'+str(i)+'_'+str(idx)
        print(mode)
        np.savetxt(myfile, mode, fmt='%12.6f')
    f = open('norm_mode_negative'+str(i), 'w')
    f.write('[FR-NORM-COORD]\n')

    for idx in range(len(pplb_thermo['norm_mode'])):
        f.write('vibration     '+str(idx)+'\n')
        myfile = 'norm_mode_negative'+str(i)+'_'+str(idx)
        tmp = open(myfile, 'r')
        tmp1 = tmp.readlines()
        tmp.close()
        for line in tmp1: f.write(line)
        os.system('rm -rf '+myfile)
    f.close()
    moldenname = 'norm_mode_negative'+str(i)+'.molden'
    molden.from_scf(neutral, moldenname)
    f = open(moldenname, 'a')
    f.write('[FREQ]\n')
    for freq in pplb_thermo['freq_wavenumber']:
        f.write(str(freq)+'\n')
    f.close()
    os.system('cat '+'norm_mode_negative'+str(i)+' >> '+moldenname)
       
#    return pplb_thermo['freq_wavenumber']

if __name__=='__main__':
    name, i = sys.argv[1], int(sys.argv[2])
    lib.num_threads(int(os.environ['OMP_NUM_THREADS']))
    #neutral = test_neutral(name)
    #charged = test_charged(name)
    test_pplb(name, i)
    #print('Neutral: \n', neutral)
    #print('Charged: \n', charged)
    #print('PPLB:    \n', pplb)
