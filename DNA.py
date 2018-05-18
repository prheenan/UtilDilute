# force floating point division. Can still use integer with //
from __future__ import division
# other good compatibility recquirements for python3
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
# This file is used for importing the common utilities classes.
import numpy as np
import matplotlib.pyplot as plt
import sys

from Bio.SeqUtils import molecular_weight

def mw_DNA(seq=None,seq_type='DNA',double_stranded=True,**kw):
    """
    :param seq: DNA sequence; otherwise just gets one average bp mass
    :return: Molecular weight, in daltons
    """
    opt = dict(seq_type=seq_type,
               double_stranded=double_stranded,
               **kw)
    if (seq is None):
        mass = [molecular_weight(seq=str(s), **opt)
                for s in ["A","T","G","C"]]
        return np.mean(mass)
    # POST: some sequence to use
    return molecular_weight(seq=seq, **opt)

def nM_per_ng_per_uL(seq=None,seq_len=None):
    if seq is None:
        assert seq_len is not None
        molar_mass = mw_DNA() * seq_len
    else:
        molar_mass = mw_DNA(seq=seq)
    # get the conversion from ng/uL to g/L
    to_g_per_L = 1e-3
    to_mole_per_L = to_g_per_L/molar_mass
    to_n_mol_per_L = to_mole_per_L * 1e9
    return to_n_mol_per_L
    

def dalton_to_g():
    return 1.66e-23

def _check_nM():
    """
    Make sure the conversions are OK within a pct or so. 

    see: support.illumina.com/bulletins/2016/11/converting-ngl-to-nm-when-calculating-dsdna-library-concentration-.html
    
    They just say:

    [nM] = ([ng/uL] / ( (660 g/mol) * N_bp)) * 1e6
    """
    lens = [1,10,1000]
    f_expected = lambda _x: 1/(660 * _x) * 1e6
    for l in lens:
        expected = f_expected(l)
        actual = nM_per_ng_per_uL(seq_len=l)
        np.testing.assert_allclose(expected,actual,atol=0,rtol=1e-2)
        
def test():
    _check_nM()


if __name__ == "__main__":
    test()
