#/bin/sh

set -e

DISTDIR=`pwd`/dist
DISTFILE=$DISTDIR/prodmaster.tar.gz

if [ -d $DISTDIR ]; then
    rm -vf $DISTDIR/*    
else
    mkdir -p $DISTDIR
fi

find . -name "*.pyc" | xargs tar -cvzf $DISTFILE

if [ -f $DISTFILE ]; then
    echo "$DISTFILE is successfully created."
    exit 0
else
    echo "Creation of $DISTFILE has been failed!"
fi

exit 1
