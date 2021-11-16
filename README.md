# canonical-behavior
This repository is a work in progress. It serves as a draft of a DataJoints element for trial-based behavior for our U24 itiative.

## Notes:
I looked at the structure for `element-array-ephys` for general principle on how to call and load files. I mirrored the main DataJoint implementation as split from 'readers'. I incorporated feedback from project-specific `behavior.py` elsewhere in table development.

## To do:
- [ ] Support functions
   - [ ] Other elements/workflows pull `find_full_path` and `find_root_directory` either from their own `__init__.py` files or from `element-data-loader.utils`. Which is best practice?
   - [ ] `workflow-array-ephys` relies on the linking module for functions to get root and session directories, but the MAP project defines these internally.  Which is best practice?
- [ ] Table definitions
   - [ ] Discuss table structure
	 - [ ] Decide supported filetypes
      -  [ ] BPOD
      -  [ ] Kepec standard, TBD
      -  [ ] Generalizable CSV with user-determined column name to DJ variable name correspondence?
- [ ] Contact the [BPod team](https://github.com/sanworks/)
   - [ ] Already an implementation of loading to Python?
   - [ ] Create joint sustainability roadmap
- [ ] Contact Kepec team - joint sustainability roadmap
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
   - [ ] Example dataset(s) for public release, in DJ Archive
   - [ ] NWB export
   - [ ] README
- [ ] RRID