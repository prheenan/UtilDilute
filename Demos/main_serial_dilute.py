# force floating point division. Can still use integer with //
from __future__ import division
# This file is used for importing the common utilities classes.
import numpy as np
import matplotlib.pyplot as plt
import sys



sys.path.append("../")
import Dilute as DilutionUtil 

def run():
    """
    Serially dilute something
    """
    ConcString = "ng/uL"
    VolString = "uL"
    # stock concentration
    dna_length = (3520-1607)+1
    dna_ng_uL = 171.5
    stock_ng_uL = dna_ng_uL
    stock_nM = stock_ng_uL/(660*dna_length) * 1e6
    Stock = dna_ng_uL
    # Desired concentrations
    Desired = [20]
    # desired volumes (for each)
    Volumes = [171 * 40/20]
    DilutionUtil.PrintSerialSteps(Stock,Volumes,Desired,
                                  ConcString=ConcString,BufferString="TE",
                                  dilution_concentration=0)
    

if __name__ == "__main__":
    run()
