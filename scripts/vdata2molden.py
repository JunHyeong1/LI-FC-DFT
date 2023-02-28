#!/home/baikgrp/calcs/JH2/prog/python3.6/bin/python3

"""
This code is for personal usage. Don't fix and move this code in any occasion. 
If I find you did that, I immediately force you to recover the hard drive or write the same code.

"""
from ase import *
import os

def convert_to_molden(mydir, filename):
    BOHR2ANGS = 0.529177249
    ANGS2BOHR = 1.0 / BOHR2ANGS
    mylist = []
    with open(os.path.join(mydir, filename), 'r') as f:
        lines = f.readlines()
        addlist = []
        InOut = False
        for idx, line in enumerate(lines):
            if 'Iteration' in line: InOut = True
            if InOut and line == '\n':
                mylist.append(addlist)
                addlist = []
            elif InOut and 'Iteration' not in line:
                addlist.append(line)
            else: pass
            if idx == len(lines) - 1: mylist.append(addlist)
    
    coords = mylist[0]
    freq = []
    norm = []
    for idx, info in enumerate(mylist):
        if idx != 0:
            freq.append(info[0])
            norm.append(info[1:])
    molden_file = filename.replace('vdata_last', 'molden')
    with open(os.path.join(mydir, molden_file), 'w') as f:
        f.write('[Molden Format]\n')
        f.write('Made from vdata_last...\n')
        f.write('[Atoms] Angs\n')
        for idx, atom in enumerate(coords):
            atom_symbol = atom.split()[0]
            x, y, z = float(atom.split()[1]), float(atom.split()[2]), float(atom.split()[3])
            atom_to_ase = Atom(atom_symbol)
            atomic_num = atom_to_ase.number
            f.write('%-3s %-5d %-3d' %(atom_symbol, idx+1, atomic_num))
            for xyz in [x, y, z]:
                f.write('%15.8f' %xyz)
            f.write('\n')
        f.write('[FREQ]\n')
        for frequency in freq:
            f.write(frequency)
    
        f.write('[FR-NORM-COORD]\n')
        for idx, mode in enumerate(norm):
            f.write('vibration%5d\n' %(idx+1))
            for atomic_mode in mode:
                x, y, z = float(atomic_mode.split()[0]), float(atomic_mode.split()[1]), float(atomic_mode.split()[2])
                for xyz in [x, y, z]:
                    f.write('%12.6f' %xyz)
                f.write('\n')
    
        f.write('[FR-COORD]\n')
        for atom in coords:
            atom_symbol = atom.split()[0]
            x, y, z = float(atom.split()[1]), float(atom.split()[2]), float(atom.split()[3])
            f.write('%2s' %atom_symbol)
            for xyz in [x, y, z]:
                f.write('%16.10f' %(xyz*ANGS2BOHR))
            f.write('\n')


if __name__ == "__main__":
    mydir = os.getcwd()
    myfile = os.listdir()
    for files in myfile:
        if 'vdata_last' in files and 'swp' not in files:
            convert_to_molden(mydir, files)
