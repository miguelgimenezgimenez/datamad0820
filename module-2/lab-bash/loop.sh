COUNT=0
for FILE in *
do
  CURRENT=$(echo $FILE | grep "^lorem" | wc -l )
  COUNT=$(($COUNT+$CURRENT))
  CURRENT=$(ls $FILE | grep "^lorem" | wc -l)
  COUNT=$(($COUNT+$CURRENT))
done
echo $COUNT