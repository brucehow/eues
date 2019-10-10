import numpy as np
import pandas as pd
import kernel

def load_data(input_file):
	data = pd.read_excel(input_file)
	return data

def main():
	inputfile = './input/Tb data Cheetah.xlsx'
	data = load_data(inputfile)
	cols  = data.columns.values

	for i in range(2, len(cols)):
		print("start to process test case: {}".format(cols[i]))
		orig_sig  = np.array(data.iloc[:,i])
		proc_sig, base  = kernel.proc_signal(orig_sig)
		visal_f, sttis_f  = kernel.get_features(proc_sig + base)
		kernel.plot_features(orig_sig, proc_sig, base, visal_f, cols[i])
		kernel.dump_features(sttis_f, cols[i])
		print("end of test case: {}\n".format(cols[i]))

if __name__ == '__main__':
	main()