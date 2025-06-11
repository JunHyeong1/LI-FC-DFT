# Linear Interpolation Fractional Charge Density Functional Theory (LI-FC-DFT) (Deprecated)
Moved to https://github.com/Yang-Laboratory/FC-DFT/tree/main
This is a program that supports single-point energy, geometry optimization, and vibrational frequency calculations of systems with fractional number of electrons by imposing the Perdew-Parr-Levy-Balduz condition.

The program is written on geomeTRIC code. Currently, it supports PySCF (freeware) and Jaguar (commercially available).

Sample calculations and useful scripts will be uploaded very soon.

I will try my best to update README... If this page is not helpful to you, please leave a message on 'Issues' tab or contact me directly.

Contact Email: kjh0910q[at]kaist.ac.kr
## Requirements
- Python >= 3.6
- <a href="https://github.com/leeping/geomeTRIC">geomeTRIC 
- <a href="https://pyscf.org/">PySCF 
- <a href="https://www.schrodinger.com/products/jaguar">Jaguar
  
## How to Install  
1. Install geomeTRIC.
  
  - `pip install geomeTRIC --prefix <path>`
  
2. Go to the directory.
  
  - `cd <path>/geomeTRIC`

3. Clone the files.
  
  - `git clone https://github.com/JunHyeong1/LI-FC-DFT.git`
  
4. (Jaguar users only) Open 'engine.py' and set the variable for the scratch directory. This is to prevent crashing resulted from assigning wrong PID at the top level.
  - `myscratch = 'path-for-scratch-directory' + result_str`

## Citation

Please cite the paper below if this code was directly or indirectly helpful to your research.

Jun-Hyeong Kim, Dongju Kim, Weitao Yang, and Mu-Hyun Baik. Fractional Charge Density Functional Theory and Its Application to the Electro-inductive Effect. J. Phys. Chem. Lett. 2023, 14, 3329-3334 - ChemRxiv: 10.26434/chemrxiv-2023-l77m4

## Common Misunderstandings
- FC stands for 'Fractional Charge', not 'Fried Chicken', 'Football Club', and 'Fitness Center'.

- DFT means 'Density Functional Theory', not 'Discrete Fourier Transformation' and 'Daejeon Football Team'.
