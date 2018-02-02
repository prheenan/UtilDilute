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

def mw_DNA(seq=None,**kw):
    """
    :param seq: DNA sequence; otherwise just gets one average bp mass
    :return: Molecular weight, in daltons
    """
    if (seq is None):
        mass = [molecular_weight(seq=str(s), seq_type='DNA') 
                for s in ["A","T","G","C"]]
        return np.mean(mass)
    # POST: some sequence to use
    return Bio.molecular_weight(seq=s, seq_type='DNA')

def dalton_to_g():
    return 1.66e-23

