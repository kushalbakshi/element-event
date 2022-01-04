''' bpod_loader.py
For eventual inclusion in element-data-loader
'''

import pathlib
import scipy.io as spio


class BPod:
    """ Parse a bpod file into the following objects
    fields: top-level bpod fields
    number_trials: total number of trials
    trial_start_times: list of floats, seconds relative to session start
    trial_types: array of tinyint designating condition number
    """
    def __init__(self, full_dir):
        try:  # check for file in path
            self.filepath = next(pathlib.Path(full_dir).glob('*.mat'))
        except StopIteration:
            raise FileNotFoundError(f'No .mat file found at: {full_dir}')
        self.data = load_bpod_matfile(self.filepath)  # see helper below

    @property
    def fields(self):
        if self._fields is None:
            self._fields = list(self.data.keys())
        return self._fields

    @property
    def number_trials(self):
        if self._number_trials is None:
            self._number_trials = self.data['nTrials']
        return self._number_trials

    @property
    def trial_start_times(self):
        if self._trial_start_times is None:
            self._trial_start_times = list(self.data['TrialStartTimestamp'])
        return self._trial_start_times

    @property
    def trial_types(self):
        if self._trial_types is None and 'TrialTypes' in self.fields:
            self._trial_types = self.data['TrialTypes']
        return self._trial_types

    '''
    @property
    def [each relevant bpod property](self)]:
        if self.[relevant property] is None:
            self.[relevant property] = self.file.[specific structure]
    '''

# --------------------- HELPER LOADER FUNCTIONS -----------------


def load_bpod_matfile(mat_filepath):
    """
    Loading routine for behavioral file, bpod .mat
    """
    # loadmat optionally takes mdict, existing dictionary which it loads into
    # simplify_cells returns a simplified dict structure, instead of reversible
    #                mat-like files
    # squeeze_me compresses matrix dimensions
    mat_file = spio.loadmat(mat_filepath.as_posix(),squeeze_me=True,
                            struct_as_record=False,simplify_cells=True)
    # bpod files load as dict with the following keys
    # __header__    : mat version, flatform, creation date
    # __version__   : file version
    # __globals__
    # SessionData   : mat_struct
    if 'SessionData' in mat_file.keys():
        return mat_file['SessionData']
    else:
        raise FileNotFoundError('.mat file missing SessionData'
                                + f'field at: {mat_filepath}')
