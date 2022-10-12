# Changelog

Observes [Semantic Versioning](https://semver.org/spec/v2.0.0.html) standard and [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) convention.

## [0.1.2] - 2022-08-26
### Added
+ Added `attribute_blob` as `longblob` in the Attribute tables - support storing non-string types of data

## [0.1.1] - 2022-06-10
### Added
+ NotImplementedError where Imported tables do not offer make function
+ get_trialized_alignment_event_times docstring specificity
### Changed
+ Diagram to reflect design with trial.BlockTrial as imported 

## [0.1.0] - 2022-05-10
### Added
+ Draft based on [Cajal](https://github.com/cajal/pipeline) and [Kavli Institute](https://github.com/kavli-ntnu/dj-docs) precursor projects
+ Table architecture
+ AlignmentEvent design to capture windows relative to an event
+ Adopted black formatting into code base

[0.1.2]: https://github.com/datajoint/element-event/releases/tag/0.1.2
[0.1.1]: https://github.com/datajoint/element-event/releases/tag/0.1.1
[0.1.0]: https://github.com/datajoint/element-event/releases/tag/0.1.0