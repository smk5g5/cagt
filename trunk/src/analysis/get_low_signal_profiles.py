
import sys
sys.path.append('../../')


def get_low_signal_profiles(data, low_signal_cutoff_value, low_signal_cutoff_quantile):
	ncol = data.data.shape[1]
	nrow = len(data.ids)
	low_signal_rows = filter(\
	lambda id: sorted(data.get_row(id))\
	[int(float(ncol)*low_signal_cutoff_quantile)]<low_signal_cutoff_value,\
	data.ids)
	return low_signal_rows