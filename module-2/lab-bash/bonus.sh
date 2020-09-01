name=MIGUEL
echo $name
mkdir $name
rm -rf $name

cd lorem

for FILE in *
do
  echo $FILE
  y=${FILE%.*}
  chrlen=${#y}
  printf "%s is %d characters length \n" $y $chrlen
done
