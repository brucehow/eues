import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pywt
import math
from reconstruct  import *
from get_features import *
from visualize_features import *


'''
api: load_data(input_file)
description: use pandas to load xlsx
'''
def load_data(input_file):
	data = pd.read_excel(input_file)
	return data
