# force floating point division. Can still use integer with //
from __future__ import division
# This file is used for importing the common utilities classes.
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append("../")
import Dilute

def run():
    """
    Utility file: we write down our stocks and desired concentrations
    """
    stocks = [263.4]
    # what volume are the stocks, in <vol>
    volumes = [45]
    # what the post-dilution concenration is, <mass>/<vol>
    common_conc = 52
    DesiredConc = np.array([common_conc for _ in stocks])
    obj = Dilute.print_dilutions(stocks,volumes,DesiredConc,
                                 unit_conc=["ng/uL" for _ in stocks])


if __name__ == "__main__":
    run()
