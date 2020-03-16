#coding:utf-8

import csv, nltk, string
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from collections import Counter

martino ="martino.csv"

f= open(martino)
chroniques = csv.reader(f)
next(chroniques)

tousMots=[]
#bigrams=[] J'ai décidé de mettre cette liste en commentaire puisque lorsque j'essayais d'append avec le bigrams plus bas, cela imprimait des listes vides
bigram=[]
for chro in chroniques:
    #print(chro[3])
    #je décide d'imprimer le 3e éléments de chaque liste puisque ce sont ces éléments qui contiennent les mots qui nous intéressent

    tokens = word_tokenize(chro[3])
   # print(tokens)

    fr= SnowballStemmer("french")

    racines = [fr.stem(mot) for mot in word_tokenize(chro[3]) if mot not in stopwords.words("french") and mot not in string.punctuation and mot!="..." and mot!="’" and mot !="»" and mot != "«"]
    #print(racines)

    for racine in racines:
        tousMots.append(racine)

    for x,y in enumerate(racines[:-1]):
        bigrams="{} {}".format(racines[x], racines[x+1])
        if "islam" in bigrams or "musulm" in bigrams:
            print(bigrams)
            bigram.append(bigrams)

freq= Counter(bigram)
print(freq.most_common(50))
