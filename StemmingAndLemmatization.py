import nltk
from nltk.corpus import stopwords
from nltk import LancasterStemmer
from nltk import PorterStemmer

textcontent = "this is an input"
# Write your code here
pattern = r'[A-Za-z0-9]+'
tokenizedwords = nltk.regexp_tokenize(textcontent, pattern)

# print(tokenizedwords)

tokenizedwords = [word.lower() for word in set(tokenizedwords)]

stop_words = set(stopwords.words('english'))
filteredwords = [w for w in tokenizedwords if not w in stop_words]

porter = nltk.PorterStemmer()
porterstemmedwords = [porter.stem(w) for w in filteredwords]

lancaster = LancasterStemmer()
lancasterstemmedwords = [lancaster.stem(w) for w in filteredwords]

wnl = nltk.WordNetLemmatizer()
lemmatizedwords = [wnl.lemmatize(w) for w in filteredwords]

print( porterstemmedwords, lancasterstemmedwords, lemmatizedwords)



