import datajoint as dj
import inspect
import importlib
import pathlib
from element_interface.utils import find_full_path
from .readers import bpod

schema = dj.schema()

_linking_module = None


def activate(schema_name, *, create_schema=True, create_tables=True,
             linking_module=None):
    """
    activate(schema_name, *, create_schema=True, create_tables=True,
             linking_module=None)
        :param schema_name: schema name on the database server to activate
                            the `behavior` element
        :param create_schema: when True (default), create schema in the
                              database if it does not yet exist.
        :param create_tables: when True (default), create tables in the
                              database if they do not yet exist.
        :param linking_module: a module (or name) containing the required
                               dependencies to activate the `session` element:
            Upstream tables:
                + Session: parent table to ProbeInsertion, typically
                           identifying a recording session.
            Functions:
                + get_trial_root_dir() -> list
                    Retrieve the root data director(y/ies) with behavioral
                    recordings (e.g., bpod files) for all subject/sessions.
                    :return: a string for full path to the root data directory
                + get_trial_sess_dir(session_key: dict) -> str
                    Retrieve the session directory containing the recording(s)
                    for a given Session
                    :param session_key: a dictionary of one Session `key`
                    :return: a string for full path to the session directory
    """
    if isinstance(linking_module, str):
        linking_module = importlib.import_module(linking_module)
    assert inspect.ismodule(linking_module), "The argument 'dependency' must"\
                                             + " be a module or module name"

    schema.activate(schema_name, create_schema=create_schema,
                    create_tables=create_tables,
                    add_objects=linking_module.__dict__)

# -------------- Functions required by the element-trial   ---------------


def get_trial_root_dir() -> list:
    """
    All data paths, directories in DataJoint Elements are recommended to be
    stored as relative paths, with respect to some user-configured "root"
    directory, which varies from machine to machine

    get_trial_root_dir() -> list
        This user-provided function retrieves the list of possible root data
        directories containing the behavioral data for all subjects/sessions
        :return: a string for full path to the behavioral root data directory,
         or list of strings for possible root data directories
    """
    return _linking_module.get_trial_root_dir()


def get_trial_sess_dir(session_key: dict) -> str:
    """
    get_trial_sess_dir(session_key: dict) -> str
        Retrieve the session directory, with all recordings for a given Session
        :param session_key: a dictionary of one Session `key`
        :return: a string for full path to the session directory
    """
    return _linking_module.get_trial_sess_dir(session_key)

# ----------------------------- Table declarations ----------------------


@schema
class TrialType(dj.Lookup):
    definition = """
    trial_type: varchar(16)
    ---
    trial_type_description: varchar(256)
    """


@schema
class Trial(dj.Imported):
    definition = """
    -> Session
    trial      : smallint # trial number (1-based indexing)
    ---
    start_time : float  # (second) relative to recording start
    stop_time  : float  # (second) relative to recording start
    """


@schema
class EventType(dj.Lookup):
    definition = """
    event_type: varchar(16)
    ---
    event_type_description='': varchar(256)
    """


@schema
class EventTrialized(dj.Imported):
    definition = """ # TRIAL SCHEMA, rename to Event
    -> Trial
    -> EventType
    event_start_time   : float  # (second) relative to recording start
    ---
    event_end_time=null: float  # (second) relative to recording start
    """


@schema
class Event(dj.Imported):
    definition = """ # EVENT SCHEMA
    -> Session
    -> EventType
    event_start_time   : float  # (second) relative to recording start
    ---
    event_end_time=null: float  # (second) relative to recording start
    """


@schema
class TrialEvent(dj.Imported):
    definition = """
    -> Trial
    -> Event
    """


@schema
class BehaviorTrial(dj.Imported):
    definition = """
    -> Trial
    ---
    -> TrialType
    """

    class TrialVariable(dj.Part):
        definition = """
        -> master
        variable_name: varchar(16)
        ---
        variable_value: varchar(2000)
        """


@schema
class BehaviorRecording(dj.Imported):
    definition = """
    -> session.SessionDirectory
    recording_id: varchar(16)
    ---
    recording_notes: varchar(256)
    """

    class BehFile(dj.Part):
        definition = """
        -> master
        filetype: varchar(16)
        """

    def make(self, key):
        trial_root_dir = pathlib.Path(get_trial_root_dir(key))
        trial_sess_dir = pathlib.Path(get_trial_sess_dir(key))
        trial_dir_full = find_full_path(trial_root_dir, trial_sess_dir)

        for trial_pattern, trial_file_type in zip(['*mat', '*_u.csv'],
                                                  ['bpod', 'UnivariateCSV']):
            trial_filepaths = [fp for fp in
                               trial_dir_full.rglob(trial_pattern)]
            if trial_filepaths:
                filetype = trial_file_type
                break
            else:
                raise FileNotFoundError('Neither bpod mat file nor _u.csv file'
                                        f' found in {trial_sess_dir}')

            if filetype == 'bpod':
                for filepath in trial_filepaths:
                    bpod_data = bpod.BPod(filepath)
                    '''
                    key['property'] = bpod_data.property
                    '''
                    return bpod_data
            elif filetype == 'UnivariateCSV':
                for filepath in trial_filepaths:
                    pass
            else:
                raise NotImplementedError(f'{filetype} files of type are '
                                          + 'not yet supported')
