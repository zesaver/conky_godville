Conky Widget for Godville
=========================

About
-----

This widget provide a Godville game client for Linux Conky. It is based on the [script](http://godville.net/forums/show_topic/257) by [lol2Fast4U](http://godville.net/gods/lol2Fast4U).
Changes:
- updated to be compartible with new Conky versions
- added Conky Manager support
- added long strings split (by words)

Installing
----------

If you are using git and Conky Manager (recommended):

just place all the files to the folder under your conky manager folder, make shure you've allowed executing of `godville.sh` - and here you go! You can activate it in Conky Manager. You can do it with simple cloning the repo:

    cd ~/.conky && git clone git@github.com:zesaver/conky_godville.git

If you are not using Conky Manager (not tested yet):

just place all the files to any folder you like, make shure you've allowed executing of `godville.sh` and add to your `conkyrc` following:

    ${execi 15 /path/to/godville.sh  | fold -s -w 50}

Miscellaneous
-------------

You can use, copy, modify and share any part of this script without any restrictions. Also fill free to contact me if any questions.
