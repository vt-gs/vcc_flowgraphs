# vcc_flowgraphs
GNU Radio Flowgraphs that work with the Astrodev Lithium radio as part of the Virginia Cubesat Constellation mission.

## Dependencies
These flowgraphs rely on blocks from Daniel Estevez's [gr-kiss](https://github.com/daniestevez/gr-kiss) GNU Radio Out-Of-Tree Module (OOTM).

The gr-kiss OOTM has been deprecated and functionality has been rolled into [gr-satellites](https://github.com/daniestevez/gr-satellites). However, the flowgraphs in this repo use the gr-kiss module due to a couple of bugs in gr-satellites that are preventing functionality for the author (something to do with bad imports of the AO73 blocks in gr-satellites, which are not being used in these flowgraphs, but are crashing them anyway). It is highly likely that these bugs are user error in the pybombs installation by the creator of the flowgraphs in this repo (Zach Leffke), and not the fault of the author of gr-satellites. It is possible to use the flowgraphs in this repo with the gr-satellites KISS/HDLC blocks if someone else has an installation of that OOTM that is working properly, but in their current form these flowgraphs expect the gr-kiss derived blocks.

