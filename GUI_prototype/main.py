import numpy as np
import kernels

def main():
	inputfile = './input/Tb data Cheetah.xlsx'
	data = kernels.load_data(inputfile)
	cols  = data.columns.values

	for i in range(2, len(cols)):
		print("start to process test case: {}".format(cols[i]))
		orig_sig  = np.array(data.iloc[:,i])
		proc_sig, base  = kernels.proc_signal(orig_sig)
		visal_f, sttis_f  = kernels.get_features(proc_sig + base)
		kernels.plot_features(orig_sig, proc_sig, base, visal_f, cols[i])
		kernels.dump_features(sttis_f, cols[i])
		print("end of test case: {}\n".format(cols[i]))
if __name__ == '__main__':
	main()