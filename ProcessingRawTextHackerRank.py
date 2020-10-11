from urllib import request
import nltk

textURL = "https://hrcdn.net/s3_pub/istreet-assets/2KDELtu3svGwJgNXUXFE7Q/001.txt"


textcontent = request.urlopen(textURL).read()


tokens1 = nltk.word_tokenize(textcontent.decode('unicode_escape'))
tokenizedlcwords = [word.lower() for word in tokens1]

noofwords = len(tokenizedlcwords)

noofunqwords = len(set(tokenizedlcwords))

wordcov = int(noofwords / noofunqwords)

wordfreq = nltk.FreqDist(word for word in list(tokenizedlcwords) if word.isalpha())

maxfreq = wordfreq.max()

print(noofwords, noofunqwords, wordcov, maxfreq)
#return noofwords, noofunqwords, wordcov, maxfreq