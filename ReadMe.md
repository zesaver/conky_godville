Conky Widget for Godville
=========================

About
-----

This widget provides a Godville game client (read only) for Linux Conky. It is based on the [script](http://godville.net/forums/show_topic/257) by [lol2Fast4U](http://godville.net/gods/lol2Fast4U) but with switching to python parser 100% of the code has been rewritten.
Changes:
- updated to use json (as recommended by Godville Admins)
- updated to be compartible with new Conky versions
- added Conky Manager support
- added long strings split (by words)
- written in python
- inventory count bug corrected
- some logic improvements made
- etc

Installing
----------

First you need to allow API requests on your [godville settings page](http://godville.net/user/profile). Then...

#### If you are using git and Conky Manager (recommended):

just place all the files to the folder under your conky manager folder, provide your name and (optional) API key in `godville.py` and make sure you've allowed executing of `godville.py` - now here you go!

You can do it with simple cloning the repo:

    cd ~/.conky && git clone git@github.com:zesaver/conky_godville.git

Now you can activate it in Conky Manager.

#### If you are not using Conky Manager (not tested yet):

just place all the files to any folder you like, provide your name and (optional) API key in `godville.py` and make sure you've allowed executing of `godville.py`. Then add to your `~/.conkyrc` following:

    ${execi 15 /path/to/godville.py  | fold -s -w 50}

*Please, note the path to `godville.py` at the end of the conky file `godville`. By default it expects to be in the current working folder. Usually this is handled well by Conky app itself, but sometimes can lead to `file not found` issues.*


Miscellaneous
-------------

This software is distributing "as is" without any warranty. You can use, copy, modify and share any part of this script without any restrictions. Also feel free to contact me if any questions or ideas.
