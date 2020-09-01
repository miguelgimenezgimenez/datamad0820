echo "Hello World"
mkdir new_dir
rm -rf new_dir
cp lorem/sed.txt lorem-copy/sed.txt 
cp lorem/*  lorem-copy
cat lorem-copy/sed.txt
cat  lorem-copy/lorem.txt lorem-copy/at.txt 
cat  lorem-copy/sed.txt | head -n 3
cat  lorem-copy/sed.txt | tail  -n 3
echo "Homo homini lupus" >> lorem-copy/sed.txt
cat  lorem-copy/sed.txt | tail  -n 3
sed 's/et/ET/' lorem-copy/sed.txt 
whoami
pwd 
ls lorem/ | grep txt 
cat lorem/sed.txt | wc -l

# COUNT LOREM
COUNT=0
for FILE in *
do
  CURRENT=$(echo $FILE | grep "^lorem" | wc -l )
  COUNT=$(($COUNT+$CURRENT))
  CURRENT=$(ls $FILE | grep "^lorem" | wc -l)
  COUNT=$(($COUNT+$CURRENT))
done
echo $COUNT

cat lorem/at.txt | grep et | wc -l


# COUNT ET
cd lorem-copy
COUNT=0
for FILE in *
do
  CURRENT=$(cat $FILE | grep et -c)
  COUNT=$(($COUNT+$CURRENT))
done
echo $COUNT