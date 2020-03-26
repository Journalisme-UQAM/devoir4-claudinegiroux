#coding:utf-8

### BONJOUR CLAUDINE
### LES JOURNÉES SONT FOLLES!
### LA PANDÉMIE BOULEVERSE TANT DE CHOSES...

import csv, nltk, string
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from collections import Counter

# martino ="martino.csv"
martino = "../martino.csv" ### J'AI PLACÉ LE FICHIER AILLEURS, TOUT SIMPLEMENT

f= open(requests.get(martino))
chroniques = csv.reader(f)
next(chroniques)

tousMots=[]
#bigrams=[] J'ai décidé de mettre cette liste en commentaire puisque lorsque j'essayais d'append avec le bigrams plus bas, cela imprimait des listes vides
bigram=[]
for chro in chroniques:
    #print(chro[3])
    print(chro[1]) ### J'AJOUTE L'IMPRESSION DE LA DATE, POUR ME DONNER UNE IDÉE DE LA PROGRESSION DU SCRIPT
    #je décide d'imprimer le 3e éléments de chaque liste puisque ce sont ces éléments qui contiennent les mots qui nous intéressent

    tokens = word_tokenize(chro[3])
   # print(tokens)

    fr= SnowballStemmer("french")

    ### OH! EXCELLENT! JE VOIS QUE TU AS RETRANCHÉ D'AUTRES SIGNE DE PONCTUATION QUI N'ÉTAIENT PAS REPÉRÉS PAR "STRING"
    racines = [fr.stem(mot) for mot in word_tokenize(chro[3]) if mot not in stopwords.words("french") and mot not in string.punctuation and mot!="..." and mot!="’" and mot !="»" and mot != "«"]
    #print(racines)

    ### LES DEUX LIGNES CI-DESSOUS POURRAIENT ÊTRE MISES EN COMMENTAIRES SI TU FAIS RIEN AVEC LA VARIABLE "TOUSMOTS" APRÈS. MAIS CE N'EST RIEN DE GRAVE :)
    for racine in racines:
        tousMots.append(racine)

    for x,y in enumerate(racines[:-1]):
        bigrams="{} {}".format(racines[x], racines[x+1])
        if "islam" in bigrams or "musulm" in bigrams:
            print(bigrams)
            bigram.append(bigrams)

freq= Counter(bigram)
print(freq.most_common(50))

### ON VOIT QUE LA RACINISATION PRODUIT PARFOIS DE DRÔLES DE RÉSULTATS
### MAIS BRAVO! L'ESSENTIEL DE L'EXERCICE EST LÀ ET ÇA FONCTIONNE SUPER BIEN! :)
### À BIENTÔT :)
