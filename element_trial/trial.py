"""Events are linked to Trials"""

import datajoint as dj
import inspect
import importlib
from . import event


schema = dj.schema()

_linking_module = None


def activate(trial_schema_name, event_schema_name, *, create_schema=True,
             create_tables=True, linking_module=None):
    """
    activate(trial_schema_name, event_schema_name, *, create_schema=True,
             create_tables=True, linking_module=None)
        :param trial_schema_name: schema name on the database server to activate
                            the `trial` element
        :param event_schema_name: schema name on the database server to activate
                            the `event` element
        :param create_schema: when True (default), create schema in the
                              database if it does not yet exist.
        :param create_tables: when True (default), create tables in the
                              database if they do not yet exist.
        :param linking_module: a module (or name) containing the required
                               dependencies to activate the `trial` element:
        Upstream tables:
            + Session: parent table to BehaviorRecording, typically
                       identifying a recording session.
    """
    if isinstance(linking_module, str):
        linking_module = importlib.import_module(linking_module)
    assert inspect.ismodule(linking_module), "The argument 'dependency' must"\
                                             + " be a module or module name"

    global _linking_module
    _linking_module = linking_module

    event.activate(event_schema_name, create_schema=create_schema,
                   create_tables=create_tables, linking_module=_linking_module)

    schema.activate(trial_schema_name, create_schema=create_schema,
                    create_tables=create_tables,
                    add_objects=_linking_module.__dict__)

# ----------------------------- Table declarations ----------------------


@schema
class Block(dj.Imported):
    definition = """ # Experimental blocks
    -> event.BehaviorRecording
    block_id               : smallint # block number (1-based indexing)
    ---
    block_start_time       : float     # (s) relative to recording start
    block_stop_time        : float     # (s) relative to recording start
    """

    class Attribute(dj.Part):
        definition = """  # Additional block attributes to fully describe a block
        -> master
        attribute_name    : varchar(16)
        ---
        attribute_value   : varchar(2000)
        """


@schema
class TrialType(dj.Lookup):
    definition = """
    trial_type                : varchar(16)
    ---
    trial_type_description='' : varchar(256)
    """


@schema
class Trial(dj.Imported):
    definition = """  # Experimental trials
    -> event.BehaviorRecording
    trial_id            : smallint # trial number (1-based indexing)
    ---
    -> TrialType
    trial_start_time    : float  # (second) relative to recording start
    trial_stop_time     : float  # (second) relative to recording start
    """

    class Attribute(dj.Part):
        definition = """  # Additional trial attributes to fully describe a trial
        -> master
        attribute_name  : varchar(16)
        ---
        attribute_value : varchar(2000)
        """


@schema
class BlockTrial(dj.Imported):
    definition = """
    -> Block
    -> Trial
    """


@schema
class TrialEvent(dj.Imported):
    definition = """
    -> Trial
    -> event.Event
    """
