"""Events are linked to Trials"""

import datajoint as dj
import inspect
import importlib

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
                + get_trial_root_data_dir() -> list
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


def get_trial_root_data_dir() -> list:
    """
    All data paths, directories in DataJoint Elements are recommended to be
    stored as relative paths, with respect to some user-configured "root"
    directory, which varies from machine to machine

    get_trial_root_data_dir() -> list
        This user-provided function retrieves the list of possible root data
        directories containing the behavioral data for all subjects/sessions
        :return: a string for full path to the behavioral root data directory,
         or list of strings for possible root data directories
    """
    return _linking_module.get_trial_root_data_dir()


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
class BehaviorRecording(dj.Manual):
    definition = """
    -> Session
    recording_id    : varchar(16)
    ---
    recording_notes : varchar(256)
    """

    class BehaviorFile(dj.Part):
        definition = """
        -> master
        filepath    : varchar(16)
        """


@schema
class TrialType(dj.Lookup):
    definition = """
    trial_type              : varchar(16)
    ---
    trial_type_description  : varchar(256)
    """


@schema
class Trial(dj.Imported):
    definition = """
    -> Session
    trial      : smallint # trial number (1-based indexing)
    ---
    -> TrialType
    start_time : float  # (second) relative to recording start
    stop_time  : float  # (second) relative to recording start
    """

    class TrialVariable(dj.Part):
        definition = """
        -> master
        variable_name: varchar(16)
        ---
        variable_value: varchar(2000)
        """


@schema
class EventType(dj.Lookup):
    definition = """
    event_type               : varchar(16)
    ---
    event_type_description='': varchar(256)
    """


@schema
class Event(dj.Imported):
    definition = """
    -> Trial
    event_start_time   : float  # (second) relative to recording start
    ---
    -> EventType
    event_end_time=null: float  # (second) relative to recording start
    """

    class EventVariable(dj.Part):
        definition = """
        -> master
        variable_name: varchar(16)
        ---
        variable_value: varchar(2000)
        """
