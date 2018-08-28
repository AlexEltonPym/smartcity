rm -rf articles articlesClean tdm
mkdir articles articlesClean tdm

cat urls.txt | xargs wget -P articles/ -nd -A .html -r -np

ls -1 articles/ | python3 newsTidy.py
python3 autoNewsAnalysis.py

