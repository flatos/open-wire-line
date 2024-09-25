# Open-Wire Transmission Line Construction with 3D-Printed Spacers

![Graph](img/Assembly.png)


This project describes the construction of homemade open-wire transmission line, along with some performance measurements.

Both STL files and the corresponding SolidWorks models are included.

An important caveat:  as of this writing (Sep 2024) I've constructed an initial length of this feedline,
but it hasn't yet been exposed for any significant length of time to UV light and the effects of weather, 
so its long-term reliability is yet to be proven.  
I'll update this page in the future as data becomes available.


## Description

I needed a length of open-wire transmission line to feed a multi-band doublet antenna, and commercially-available options are scarce or non-existent.
I had purchased a 500 ft spool of antenna wire (`DX Engineering DXE-ANTW-500`) for the antenna itself and decided to construct the feedline from the same material.
This is a 14 AWG stranded wire with a UV-resistant PVC jacket.

It appears that this wire is now only available in smaller spools (300, 150, 75 feet).
Some other wire with the same jacket diameter (0.115") would presumably work just as well.

I decided on a wire spacing of 3 inches, with spacers placed every 18 inches, purely for mechanical (or aesthetic?) reasons.
The wire spacing isn't very significant electrically -- practical values all result in characteristic impedancess in the 500 - 600 ohm range.

The spacers are printed from ASA filament, which is similar to ABS but known for its superior UV resistance.  
Some domestic filament manufacturers I've purchased the ASA filament from are [Coex](https://coex3d.com/) and [3DXTech](https://www.3dxtech.com/).
I've included versions which can be assembled using acetone as a solvent,  as well as a version that uses cable ties to attach the wires.


## Models

The models provided in the `\models` directory are:


| | File | Desc |
| :---: | --- | --- |
| 1 | Spreader_3inch_4a.* | 3 inch spreader (for welding with acetone) |
| 2 | Spreader_3inch_4a_1hole.* | ...same, with (1) mounting hole |
| 3 | Spreader_3inch_4a_2hole.* | ...same, with (2) mounting holes |
| 4 | Spreader_3inch_4b.* | Wire clips for above parts (2 per spreader) |
| 5 | Spreader_3inch_6.* | Version for assembly with wire ties |



Material cost per spacer is approximately $0.08.






![Graph](img/Explode.png)
[DX Engineering web site](https://www.dxengineering.com/)
A redesigned fan shroud for the LulzBot HE tool head found on my Taz Workhorse 3D printer.

Probably (?) fits other tool heads too, but is not compatible with the other tool head I own, the HS+.

I modified the existing design to allow the heater block to turn the entire 360 degrees without interference from the fan shroud. 
I've been using this part for more than two years without problem.

I used the original STL files from LulzBot to read off the exact locations of mating planes and mounting points; otherwise the design is original.

This repository contains both the Solidworks models and STL files for the parts.



## Description




![Graph](img/top.png)
![Graph](img/bot.png)
![Graph](img/exploded.png)

A rather rough-looking example printed in nylon-CF. I used ABS for the final print.

![Graph](img/pic1.png)
![Graph](img/pic2.png)


## Disclaimer
You access to and use the contents of this site at your own risk.\
The author assumes no responsibility or liability for any errors or omissions in the content of this site.\
The information and models provided on this site are provided in good faith, however we make no representation  or warranty of any kind,
express or implied, regarding the accuracy, adequacy,  validity, reliability, or completeness of any information on the site.


## Contact
ac8p@proton.me


