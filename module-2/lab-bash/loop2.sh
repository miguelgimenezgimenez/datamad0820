cd lorem-copy
COUNT=0
for FILE in *
do
  CURRENT=$(cat $FILE | grep et -c)
  COUNT=$(($COUNT+$CURRENT))
done
echo $COUNT