# Import
import pandas as pd
import numpy as np
from rdkit.Chem import AllChem as Chem
from rdkit.Chem import PandasTools,Draw
import math
import openbabel
import darkchem
import sys
sys.path.append("../..")
import functions

# Define testing function
def test_standardize_smi():
    # Generate some data to use
    smilescc = {'Reactants': ['CC(=O)C', 'O=C1CCCCC1', 'O=C1CCCC1C', 'O=C1CCCC1C', 'CCCC(=O)CCC',
                          'CCCCC(=O)CCCC', 'CC(=O)CC(=O)C', 'CC(=O)CC(=O)C', 'COCC(=O)C',
                          'COCC(=O)C',
                          'CC(=O)c1ccccc1'],
             'Products': ['CCC(=O)C', 'CC1CCCCC1=O', 'CC1CCC(C1=O)C', 'O=C1CCCC1(C)C', 'CCCC(=O)C(CC)C',
                          'CCCCC(=O)C(CCC)C', 'CC(C(=O)C)C(=O)C', 'CC(=O)C(C(=O)C)(C)C', 'COCC(=O)CC',
                          'COC(C(=O)CC)C',
                          'CCC(=O)c1ccccc1']}

    smi = str(smilescc)

    # Operate the function wihch is being tested
    standardize_smi = functions.standardize_smi(smi)

    # Assert several arguments
    assert type(standardize_smi) == str


    return 0
