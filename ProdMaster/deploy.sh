#/bin/sh


DISTDIR=`pwd`/dist
DISTFILE=$DISTDIR/prodmaster.tar
CDISTFILE=$DISTFILE.gz

if [ -d $DISTDIR ]; then
    rm -vf $DISTDIR/*    
else
    mkdir -p $DISTDIR
fi

echo -n "Removing old byte compiled files (*.pyc) and cache dirs... "
find . -name "*.pyc" -exec rm "{}" \;
find . -name "__pycache__" -exec rm -rf "{}" \;
echo "Done."


echo -n "Compiling python sourcefiles... "
python3 -c 'import compileall; compileall.compile_dir("hu/", force=True, quiet=True) '
python3 -c 'import compileall; compileall.compile_dir("mysql/", force=True, quiet=True) '
echo "Done."

echo -n "Preparing newly compiled pyc files... "
ORIG_FILELIST=`find . -name "*.pyc" -exec ls "{}" \; | grep -v __init__`
for orig_file in $ORIG_FILELIST
do
    new_file=`echo $orig_file | sed s:__pycache__/:: | sed s:.cpython-32::`
    mv $orig_file $new_file
done
echo "Done."

DIST_FILELIST=`find . -name "*.pyc" -exec ls "{}" \; | grep -v __init__`
DIST_FILELIST="$DIST_FILELIST `find . -name '__init__.py'`"

tar -cvf $DISTFILE prodmaster.sh prodmaster.bat

for one_file in $DIST_FILELIST
do
    tar -rvf $DISTFILE $one_file
done

gzip $DISTFILE

if [ -f $CDISTFILE ]; then
    echo "$CDISTFILE is successfully created."
    exit 0
else
    echo "Creation of $CDISTFILE has been failed!"
fi

exit 1
