import numpy as np
import pandas as pd
import calendar
from datetime import datetime
from matplotlib import pyplot as plt

from scipy.ndimage.filters import gaussian_filter1d

import pywt
import pywt.data


class Wavelet(object):
    """
    Class used to represent each Wavelet object.
    
    Raises:
        ValueError: If plot_original_data is called without any data to plot.
    """
    def __init__(self):
        self.raw = None
        self.datetime = None

    def plot_original_data(self):
        if self.raw is None or self.datetime is None:
            raise ValueError("No raw data to plot")

        # Testing gaussian filter
        #plt.plot(self.datetime, self.raw)
        raw_smooth = gaussian_filter1d(self.raw, sigma=5)
        plt.plot(self.datetime[:5000], raw_smooth[:5000], label="raw data (gaussian filter)", color="black")
        plt.legend()
        plt.show()

