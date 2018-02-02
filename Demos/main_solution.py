# force floating point division. Can still use integer with //
from __future__ import division
# This file is used for importing the common utilities classes.
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append("../")
import DilutionUtil 

def run():
    HEPES_1x = 50
    KCL_1x = 25
    ZnCl2_1x = 0.1
    Stats = [ ["HEPES","mM",975,HEPES_1x,0],
              ["KCl","mM",2500,KCL_1x,0],
              ["ZnCl2","mM",15,ZnCl2_1x,0],
              ["TCEP","mM",50,1,0],
    ]
    # I convert it into the 4x buffer
    conc_mult = 4
    stats_4x = copy.deepcopy(Stats)
    for i in range(len(Stats)):
        stats_4x[i][3] *= conc_mult
    DilutionUtil.PrintSolutionSteps(stats_4x,50,"mL",
                                    BufferName="DI H20")
