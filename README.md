# canonical-behavior
Draft of DataJoints element for trial-based behavior tracking for U24

## Process:
I looked at the structure for `element-array-ephys` for general principle on how to call and load files. I mirrored the main datajoint implementation as split from 'readers'. I incorporated feedback from project-specific `behavior.py` elsewhere in table development.

## To do:
- Discuss initial table structure
- What filetypes should we support? Is it worth our time to make a generalist import tool? Perhaps with a user-generated table of datajoint variable names and their corresponding csv column name?
- The [BPod folks](https://github.com/sanworks/) havbe an active github. Chris to investigate if there's already a comprehensive import tool
- Chris to generate diagram
