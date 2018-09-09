timestamp=$( date +%s)

mkdir $timestamp
  
mv articles/ $timestamp
mv articlesClean/ $timestamp
mv tdm/ $timestamp

zip -r -q -9 $timestamp.zip $timestamp -m

mv $timestamp.zip articlesBackup


mkdir articles articlesClean tdm

cat urls.txt | xargs wget -q -P articles/ -nd -A .html -r -np

ls -1 articles/ | python3 newsTidy.py

python3 autoNewsAnalysis.py
