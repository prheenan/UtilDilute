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


def extinction_coefficient(protein_dict):
    """
    see:
    Thermo Fisher Scientific (2010). 
    Thermo Scientific NanoDrop Spectrophotometers: Protein 280.

    tools.thermofisher.com/content/sfs/brochures/
    Thermo-Scientific-NanoDrop-Products-Protein-Technical-Guide-EN.pdf
    
    :param protein_dict: dictionary of key:value paris, where key is an ammino
    acid code, and value is the number of times that aa appears.

    :return: molar-absorptibivity coefficient (extinction coefficient) in
    1/(M*cm)
    """
    aa_coeffs = dict(W=5500,
                     Y=1490,
                     C=125)
    aa_contributions = [protein_dict[k] * v for k,v in aa_coeffs.items()]
    total = sum(aa_contributions)
    return total

def OD_conversions(extinction_coeff,molecular_weight):
    """
    See:
    Thermo Fisher Scientific (2010).
    Thermo Scientific NanoDrop Spectrophotometers: Protein 280.

    :param extinction_coeff: the extinction coefficient at A280 in 1/(M*cm)
    :param molecular_weight:
    :return:
    """
    epsilon_inverse_M_cm = extinction_coeff
    M_per_OD280_1cm = 1/(1 * epsilon_inverse_M_cm)
    # get the 'epsilon 1%' or epsilon in unit of g/(100mL * cm)
    epsilon_g_per_100mL_per_cm = epsilon_inverse_M_cm * 10 / molecular_weight
    #determine the conversion from A280_1cm to mg/mL; see ibid
    mg_per_mL_per_OD280_1cm = 1/(epsilon_g_per_100mL_per_cm) * 10
    return mg_per_mL_per_OD280_1cm,M_per_OD280_1cm

