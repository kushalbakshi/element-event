from pynwb import NWBFile

from element_session import session
from element_trial import trial


def trial_to_nwb(trial_key):
    scan_query = session.Session & trial.TrialEvent & trial_key
    # https://github.com/nwb-extensions/ndx-events-record
    return NWBFile(scan_query)


""" From CHEN 2017 https://github.com/vathes/DJ-NWB-Chen-2017

# =============== TrialSet ====================
# NWB 'trial' (of type dynamic table) by default comes with three mandatory
# attributes: 'start_time' and 'stop_time'. Other trial-related information
# needs to be added in to the trial-table as additional columns (with column
# name and column description)

dj_trial = experiment.SessionTrial * experiment.BehaviorTrial
skip_adding_columns = experiment.Session.primary_key + ['trial_uid', 'trial']

if experiment.SessionTrial & session_key:
    # Get trial descriptors from TrialSet.Trial and TrialStimInfo
    trial_columns = [{'name': tag,
              'description': re.sub('\s+:|\s+', ' ', re.search(
                f'(?<={tag})(.*)', str(dj_trial.heading)).group()).strip()}
             for tag in dj_trial.heading.names
             if tag not in skip_adding_columns + ['start_time', 'stop_time']]

    # Add new table columns to nwb trial-table for trial-label
    for c in trial_columns:
        nwbfile.add_trial_column(**c)

    # Add entry to the trial-table
    for trial in (dj_trial & session_key).fetch(as_dict=True):
        trial['start_time'] = float(trial['start_time'])
        trial['stop_time'] = (float(trial['stop_time']) if
                              trial['stop_time'] else 5.0)
        [trial.pop(k) for k in skip_adding_columns]
        trial['early_lick'] = True if trial['early_lick'] == 'early' else False
        nwbfile.add_trial(**trial)

# ===========================================================================
# ============================= BEHAVIOR TRIAL EVENTS =======================
# ===========================================================================

behavior = nwbfile.create_processing_module(
    'behavior', 'Time of behavioral events in this session')
behav_event = pynwb.behavior.BehavioralEvents(name='BehavioralEvents')
behavior.add_data_interface(behav_event)

for trial_event_type in \
        (experiment.TrialEventType & \
            experiment.TrialEvent & session_key).fetch('trial_event_type'):
    event_times, trial_starts = \
        (experiment.TrialEvent * experiment.SessionTrial
            & session_key & {'trial_event_type': trial_event_type}).fetch(
        'trial_event_time', 'start_time')

    if trial_event_type == 'sample':
        description = 'Timestamps: beginning of the sampling on each trial.'
    elif trial_event_type == 'delay':
        description = 'Timestamps: beginning of the delay on each trial.'
    elif trial_event_type == 'go':
        description = 'Time stamps of the go cue signal on each trial.'

    if len(event_times) > 0:
        event_times = np.hstack(event_times.astype(float)
                                + trial_starts.astype(float))
        behav_event.create_timeseries(
            name=trial_event_type, unit='a.u.', conversion=1.0,
            data=np.full_like(event_times, 1),
            timestamps=event_times,
            description=description)

"""
