import os
import pathlib

import datajoint as dj
from . import find_full_path, find_root_directory

import scipy.io as spio
import numpy as np

class BPod:

	def __init__(self, full_dir):
		# check for file
		try:
			self.filepath=next(pathlib.Path(full_dir).glob('*.mat'))
		except StopIteration:
			raise FileNotFoundError(f'No bpod .mat file found at: {full_dir}')
		# check that .mat file found is bpod, by checking that it has a SessionData section
		try: self.file=load_bpod_matfile(self.file)
		except StopIteration:
			raise FileNotFoundError(f'.mat file missing SessionData field at: {full_dir}')

	@property
	def trialnumber(self):
		if self._trialnumber is None:
			self._trialnumber = self.file.nTrials
		return self._trialnumber

	'''
	@property
	def [each relevant bpod property](self)]:
		if self.[relevant property] is None:
			self.[relevant property] = self.file.[specific structure]
	'''

# --------------------- HELPER LOADER FUNCTIONS -----------------

# see full example here:
# https://github.com/mesoscale-activity-map/map-ephys/blob/master/pipeline/ingest/behavior.py

def load_bpod_matfile(dir, matlab_filepath):
	"""
	Loading routine for behavioral file, bpod .mat
	"""
	#Loading the file
	SessionData = spio.loadmat(matlab_filepath.as_posix(),
                            squeeze_me=True,
                            struct_as_record=False)['SessionData']
	return SessionData