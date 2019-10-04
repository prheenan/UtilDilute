# force floating point division. Can still use integer with //
from __future__ import division
# This file is used for importing the common utilities classes.
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append("../")
import Dilute 

def run():
    Stats = [ ["EDTA","mM",420,1,0],
              ["Tris-HCl","mM",1000,10,0]]
    Dilute.PrintSolutionSteps(Stats,1000,"mL",
                              BufferName="DI H20")


if __name__ == "__main__":
    run()