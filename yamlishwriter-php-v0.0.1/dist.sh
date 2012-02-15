#!/bin/sh

distname=$1
distarc="$distname.tar.gz"

echo "Making $distarc"
for f in `cat MANIFEST`
do
	d=`dirname $f`
	mkdir -p "$distname/$d"
	echo "Adding $f"
	cp $f "$distname/$f"
done

tar zcf $distarc $distname
rm -rf $distname
