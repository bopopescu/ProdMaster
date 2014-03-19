#/bin/sh


DISTDIR=`pwd`/dist
DISTFILE=$DISTDIR/prodmaster_src.tar.gz
ZIPFILE=$DISTDIR/prodmaster_src.zip
TMPDIR=prodmaster

rm -rf $DISTDIR

mkdir -p $DISTDIR/$TMPDIR


find hu/ -name "*.py" -exec rsync -qazR "{}" $DISTDIR/$TMPDIR \;
find mysql/ -name "*.py" -exec rsync -qazR "{}" $DISTDIR/$TMPDIR \;
cp -r prodmaster.sh $DISTDIR/$TMPDIR
cp -r prodmaster.bat $DISTDIR/$TMPDIR

cd $DISTDIR
# tar -czf $DISTFILE $TMPDIR
zip -r $ZIPFILE $TMPDIR
cd - 

rm -rf $DISTDIR/$TMPDIR

if [ -f $ZIPFILE ]; then
    echo "$ZIPFILE is successfully created."
    exit 0
else
    echo "Creation of $ZIPFILE has been failed!"
fi

exit 1
