import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pywt
import pdb

'''
api: load_data(input_file)
description: use pandas to load xlsx
'''
def load_data(input_file):
	data = pd.read_excel(input_file)
	return data
	#pdb.set_trace()

def main():
	data = load_data('input_data.xlsx')
	proc_signal(np.array(data['07A-11']))


if __name__ == '__main__':
	main()
