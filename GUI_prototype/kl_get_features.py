import numpy as np
from scipy import signal
from scipy import stats
import csv
import pdb
'''
api: erode, dilate, get_baseline, get_onsets, get_peaks
description: a series api to detect onsets and peaks using
1-D morphological filter
'''
def erode(sig, struct_len):
	ret = np.zeros_like(sig)
	for i in range(0, len(ret) - struct_len, 1):
		ret[i] = np.min(sig[i:i+struct_len])
	ret[i:] = ret[i-1]
	return ret

def dilate(sig, struct_len):
	ret = np.zeros_like(sig)
	for i in range(struct_len-1, len(ret) , 1):
		ret[i] = np.max(sig[i - struct_len + 1:i+1])
	ret[0:struct_len-2] = ret[struct_len-1]
	return ret

def get_onsetsline(sig, struct_len):
	ret1 = erode(sig, struct_len)
	ret2 = dilate(ret1, struct_len)
	return ret2

def get_onsets(baseline, mask_len):
	delta = baseline[1:] - baseline[0:-1]
	start, end, pre_start, pre_end, onsets = -1, -1, -1, -1, []
	for i in range(len(delta)):
		if -1 == start and 0 != delta[i]:
			start = i
			#print("start:{}, value{}; ".format(start, delta[i]), )
		if -1 != start and -1 == end and 0 == delta[i]:
			end = i
			#print("end:{}, value{}; ".format(end, delta[i]), )
		if -1 != start and -1 != end:
			if(end - start < mask_len):
				#pre_start = start
				end = -1
				continue

			if (start - pre_end < mask_len):
				#print("debug0",)
				#print(pre_end, start, end, start - pre_end, end - start, mask_len)
				start = pre_start
				onsets[-1] = start + np.argmin(baseline[start:end])
				#start, end = -1, -1
			else:
				onsets.append(start + np.argmin(baseline[start:end]))
				#print("debug1",)
				#print(pre_end, start, end, start - pre_end, end - start, mask_len)

			pre_start, pre_end = start,end
			start,end = -1,-1
	#pdb.set_trace()
	return np.array(onsets)

def get_peaks(sig, onsets):
	peaks, areas = [], []
	for i in range(len(onsets)-1):
		peak = onsets[i] + np.argmax(sig[onsets[i]:onsets[i+1]])
		peaks.append(peak)
		areas.append(np.sum(sig[onsets[i]:onsets[i+1]]))
	return np.array(peaks), np.array(areas)

def get_returns(sig, onsets, peaks, sd):
	rturns = np.zeros_like(peaks)
	for i in range(len(peaks)):
		sample = np.abs(sig[peaks[i]:onsets[i+1]] - sd - sig[onsets[i+1]])
		rturns[i] = peaks[i] + np.argmin(sample)
	return rturns
def get_baseline(sig, struct_len):	
	return get_onsetsline(sig, struct_len)

def remove_fakeonsets(sig, onsets, thd):
	true_onsets = []
	for i in range(len(onsets)-1):
		sample = sig[onsets[i]:onsets[i+1]]
		height = np.max(sample) - np.min(sample)
		if height >= thd:
			true_onsets.append(onsets[i])
	return np.array(true_onsets)

def get_time_window(sig):
	start = 0
	end   = sig.size
	return start, end
'''
api: get_features(sig, fs = 1/60)
description: extract features from processed signal
'''
def get_statistics(feature):
	mnv = np.mean(feature)
	stdv = feature.std()
	semv = stats.sem(feature)
	return mnv, stdv, semv

def get_features(sig, fs = 1/60):
	struct_len = 80
	onsetsline = get_onsetsline(sig, struct_len)
	baseline = get_baseline(sig, 3*struct_len)
	onsets = get_onsets(onsetsline, int(0.5*struct_len))
	#pdb.set_trace()
	onsets = remove_fakeonsets(sig, onsets, 1*np.std(baseline))
	peaks, areas  = get_peaks(sig, onsets)
	#onsets, peaks = remove_fakepoints(sig, onsets, peaks, 2.5*np.std(baseline))
	rturns = get_returns(sig, onsets, peaks, 0.25*np.std(baseline))

	onsets_1 = onsets[:-1]
	t_onsets = onsets_1*fs
	t_peaks  = (peaks - onsets_1)*fs
	t_duration  = (rturns - onsets_1)*fs
	t_tobaseline = (onsets[1:] - onsets_1)*fs
	amplitude = sig[peaks] - sig[onsets_1]
	t_inter = (onsets[1:] - rturns)*fs


	return (onsets, peaks, rturns, baseline), \
	(t_onsets, t_peaks, t_tobaseline, t_duration, amplitude, areas, t_inter)

def dump_features(eues_info, filename):
	t_onsets, t_peaks, t_tobaseline, t_duration, amplitude, areas, t_inter = eues_info
	eues_num = t_peaks.size
	waveletnum = 1000 #TBD
	mean_amp, std_amp, sem_amp = get_statistics(amplitude)
	mean_dur, std_dur, sem_dur = get_statistics(t_duration)
	mean_area, std_area, sem_area = get_statistics(areas)
	mean_inter, std_inter, sem_inter = get_statistics(t_inter)
	with open('./output/{}_eues_info.csv'.format(filename), 'w', newline='') as f:
		wt = csv.writer(f)
		wt.writerow(['EUEs Id', 'time of onset', 'time to max',\
					 'time to return to baseline', 'duration', 'amplitude',
					 'area under the curve', 'inter EUEs time'])
		for idx, line in enumerate(zip(t_onsets, t_peaks, t_tobaseline, t_duration, amplitude, areas, t_inter)):
			wt.writerow([idx] + list(line))

	with open('./output/{}_overall_info.txt'.format(filename), 'w') as f:
		f.write('total number of EUEs detected: {}\n'.format(eues_num))
		f.write('number of wavelets: {}\n'.format(waveletnum))
		f.write('feature   : {:>10s} {:>10s} {:>10s}\n'.format('MEAN','SD', 'SEM'))
		f.write('amplitude : {:10.4f} {:10.4f} {:10.4f}\n'.format(mean_amp, std_amp, sem_amp))
		f.write('duration  : {:10.4f} {:10.4f} {:10.4f}\n'.format(mean_dur, std_dur, sem_dur))
		f.write('area      : {:10.4f} {:10.4f} {:10.4f}\n'.format(mean_area, std_area, sem_area))
		f.write('inter time: {:10.4f} {:10.4f} {:10.4f}\n'.format(mean_inter, std_inter, sem_inter))


	



