# vcc_flowgraphs
GNU Radio Flowgraphs that work with the Astrodev Lithium radio as part of the Virginia Cubesat Constellation mission.

## WARNING: FCC and Liability
The flowgraphs in this repository, when combined with an appropriate SDR device (in this case an Ettus Research B210 for development) WILL radiate in the FCC controlled 400 MHz Satellite Band (And so will the Lithium radio).  It is the responsibility of the user of the flowgraphs in this repository to ensure that they follow ALL FCC regulations and guidelines for the proper use of these flowgraphs.  A couple of recommendations for best practices to remain compliant with all US Laws and FCC Regulations:
* Obtain an FCC License for operation in this band (i.e. [Experimental License](https://apps.fcc.gov/oetcf/els/forms/442Dashboard.cfm)).
* Contain all Radiated Emissions in a [Faraday Cage](https://en.wikipedia.org/wiki/Faraday_cage) such as those available from [Ramsey Electronics](http://www.ramseyelectronics.com/product.php?pid=25).
* Utilize Coaxial Cabling between all transmitters and receivers, lowest possible output power levels, and heavy attenuation to both protect the receiver front ends and minimize leaked RF levels.

IT IS THE RESPONSIBILITY OF THE END USER TO ENSURE THEY ARE IN COMPLIANCE WITH ALL LOCAL, STATE, AND FEDERAL LAWS WHEN USING THESE FLOWGRAPHS.  THE CREATOR OF THESE FLOWGRAPHS ASSUMES NO LIABILITY FOR OTHERS ACTIONS WITH THESE FLOWGRAPHS.

## Dependencies
These flowgraphs rely on blocks from Daniel Estevez's [gr-kiss](https://github.com/daniestevez/gr-kiss) GNU Radio Out-Of-Tree Module (OOTM).

## KISS Handling Python Scripts
For the moment, a couple of VERY rough python scripts are being used to handle the KISS Frame input/output for these flowgraphs.  The current versions of these scripts can be found in the [python_packet]() repository.  For the uplink, 


###gr-kiss vs gr-satellites
The gr-kiss OOTM has been deprecated and functionality has been rolled into [gr-satellites](https://github.com/daniestevez/gr-satellites). However, the flowgraphs in this repo use the gr-kiss module due to a couple of bugs in gr-satellites that are preventing functionality for the author (something to do with bad imports of the AO73 blocks in gr-satellites, which are not being used in these flowgraphs, but are crashing them anyway). It is highly likely that these bugs are user error in the pybombs installation by the creator of the flowgraphs in this repo (Zach Leffke), and not the fault of the author of gr-satellites. It is possible to use the flowgraphs in this repo with the gr-satellites KISS/HDLC blocks if someone else has an installation of that OOTM that is working properly, but in their current form these flowgraphs expect the gr-kiss derived blocks.  It is planned to swap out the gr-kiss blocks for the gr-satellites equivalent blocks once the installation issue is resolved.

