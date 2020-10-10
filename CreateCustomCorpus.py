from nltk.corpus.reader.plaintext import PlaintextCorpusReader


filecontent1 = "This is a cow"
filecontent2 = "This is a Dog"

corpusdir = 'nltk_data/'
with open(corpusdir + 'content1.txt', 'w') as text_file:
    text_file.write(filecontent1)
with open(corpusdir + 'content2.txt', 'w') as text_file:
    text_file.write(filecontent2)

text_corpus = PlaintextCorpusReader(corpusdir, ["content1.txt", "content2.txt"])

no_of_words_corpus1 = len(text_corpus.words("content1.txt"))
print(no_of_words_corpus1)
no_of_unique_words_corpus1 = len(set(text_corpus.words("content1.txt")))

no_of_words_corpus2 = len(text_corpus.words("content2.txt"))
no_of_unique_words_corpus2 = len(set(text_corpus.words("content2.txt")))



