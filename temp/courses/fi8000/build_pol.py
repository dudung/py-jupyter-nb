#!/usr/bin/env python -W ignore::DeprecationWarning
import mbuild as mb
import mbuild
from mbuild.lib.recipes.polymer import Polymer
import argparse
import sys

parser = argparse.ArgumentParser(description="A program to build a simple polymer with the same monomer")
parser.add_argument('-m','--mono',type=str,help='Monomer structure in mol2 format. SMILES format is also accepted',required=True)
parser.add_argument('-c','--cap',type=str,help='Molecule to define the capping group.',required=True)
parser.add_argument('-i1','--index1',type=int,help='First index of the atom to be replaced in the monomer. The index is always starting from 0.')
parser.add_argument('-i2','--index2',type=int,help='Second index of the atom to be replaced in the monomer. The index is always starting from 0.')
parser.add_argument('-r','--replace',type=bool,help='Whether the atom will be replaced.',default=True)
parser.add_argument('-ic','--index_cap',type=int,help='Index of the capping atom to be removed from its molecular form.')
parser.add_argument('-s','--separation',type=float,help='Separation distance between the fragment in Angstrom unit. Default=0.15.',default=0.15)
parser.add_argument('-n','--repetition',type=int,help='The number of repetition units of the polymer. Default= 10',default=10)
opt = parser.parse_args(sys.argv[1:])

mono = opt.mono
cap = opt.cap


monomer = mb.load(mono)

capping = mb.load(cap)

chain = Polymer()

chain.add_monomer(compound=monomer, indices=[opt.index1,opt.index2],separation=opt.separation,replace=True)

chain.add_end_groups(capping,index=opt.index_cap,separation=opt.separation,duplicate=False)

chain.build(n=opt.repetition,sequence='A')

chain.save('polymer_{}.xyz'.format(opt.repetition),overwrite=True)
