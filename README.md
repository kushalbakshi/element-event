# element-trial
This repository is a work in progress not yet ready for public release.
It serves as a draft of a DataJoint element for trialized experiments behavior
for our U24 itiative.

## Schemas
`trial` should be activated if all events are tied to specific trials.
`event` should be activated if events occur independently of trials.

The current draft of `trial` contains all proposed tables. When we're sure of
the contents, including make functions, one would copy the contents of the
`trial` schema over to events, and then remove the trialized version of the
event table.

## Filetypes

### Bpod
MATLAB is the only officially supported environment. SciPy has a lot of support
for loading matlab files. In the current draft, SciPy is used to import Bpod
.mat files as embedded dictionaries. Micheal Wulf shared the Bpod files that
are currently in `workflow-trial/user_data/Bpod_files` as a diverse set of
examples.

Under `element_trial/readers/`, there are two files: `Bpod.py` and
`Bpod_fields_notes.py`. The former is a draft of an eventual reader that could
be folded into `element_data_loader`. It handles general ingestion for fields
that are consisitent across examples. The latter highlights just how different
Bpod files can be. A fully realized loader may need to pull directly from
Bpod 'raw' fields to reconstruct the experiement, as many other fields are
organized differently across trials.

Development for this reader was partially conducted within
`workflow_trial/notebooks/1_.ipynb`. This contains code snipits for exploring
the loaded Bpod data.

Ecosystem: The SanWorks team
([git repositories here](https://github.com/sanworks?tab=repositories)) offers
no offical python support, suggesting instead that users
[export to JSON](https://sanworks.io/forum/showthread.php?tid=626&pid=1169).
The PyBpod project ([github](https://github.com/pyBpod/pyBpod),
[docs](https://pyBpod.readthedocs.io/en/v1.8.1/)) offers a python-based GUI
alternative for running Bpod hardware. So far as I could tell, they do not
offer any usefull ingestion functions we would want to incorporate.


### Alternate generalized format

We previously discussed also supporing a univariate csv format that would
contain 4 values: timestamp on, timestamp off, data type and value. This has
not yet been implemented.


## To do:
- [X] Support functions
   - [X] Pull `find_full_path` and `find_root_directory` from `element-data-loader.utils`.
   - [X] To find root/session dirs, refer to config file if exists. If not, linking module
- [ ] Table definitions
   - [X] Discuss table structure
	 - [X] Decide supported filetypes:
      - Bpod
      - Generalizable 'Univariate' CSV: timestamp on, off, data type, value
    - [ ] Develop ingestion functions
- [ ] Test tables with example data
   - Aeon, bonsai system API
   - Kepecs group provided Bpod files
- [X] Contact the [Bpod team](https://github.com/sanworks/)
   - [X] Already an implementation of loading to Python - No
   - [X] Create joint sustainability roadmap - Unlikely
- [ ] Analysis package
	 - [ ] Load processed data
   - [ ] Create table definitions
   - [ ] Trigger analysis on raw data import
- [ ] Quality control metrics
- [ ] GitHub Actions for PyPI release
- [ ] example workflow
   - [ ] Integration tests with pytest
   - [ ] Tutorials in text format (i.e. Jupyter notebook)
   - [ ] Tutorial in video format
   - [ ] Docker for tests
   - [X] Example dataset(s) for public release
   - [ ] Example dataset loaded to DJ Archive
   - [ ] NWB export
   - [ ] README
- [ ] RRID

## Installation

```
pip install element-trial
```

if you have an older version of ***element-trial*** installed, using `pip`, upgrade with

```
pip install --upgrade element-trial
```

Install `element-data-loader`

```
element-data-loader @ git+https://github.com/datajoint/element-data-loader
```


