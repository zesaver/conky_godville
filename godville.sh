#!/bin/sh
# by lol2Fast4U
USERNAME="zesaver"
curl http://godville.net/gods/api/$USERNAME.xml 2>/dev/null | xsltproc /home/zesaver/.conky/Godville/godville.xslt - $FILTER | grep -v "<?xml"
