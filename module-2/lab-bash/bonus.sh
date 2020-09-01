name=MIGUEL
echo $name
mkdir $name
rm -rf $name


# count characters in lorem folder's files
cd lorem
for FILE in *
do
  echo $FILE
  y=${FILE%.*}
  chrlen=${#y}
  printf "%s is %d characters length \n" $y $chrlen
done

# processess info
top
# processor info
sysctl -a | grep machdep.cpu

# ALIAS SHOULD BE ADDED IN .bashrc or .zshrc file:
alias jn="jupyter notebook" 


# compress :
tar -zcvf lorem.tar.gz lorem 
# extract
tar -zxvf lorem.tar.gz
