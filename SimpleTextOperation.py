# ======================================================
# Hands On - NLP - Python - Simple Text Operation - 1(Hanker Rank)
# ======================================================
def calculateWordCounts(text):
    # Write your code here
    n_words = len(text)
    print(n_words)

    n_unique_words = len(set(text))
    print(n_unique_words)

    word_coverage1 = n_words / n_unique_words
    print(int(word_coverage1))


# ======================================================
# Hands On - NLP - Python - Simple Text Operation - 2 (Hanker Rank)
# ======================================================
def filterWords(text):
    # Write your code here
    # words = nltk.word_tokenize(text)
    ing_words = [word for word in set(text) if word.endswith('ing')]
    # print(ing_words)

    large_words = [word for word in list(text) if len(word) > 15]
    # print(large_words)

    # print("-------------------------------------------------------")

    upper_words = [word for word in set(text) if word.isupper()]
    # print(upper_words)

    return ing_words, large_words, upper_words

# ======================================================
# Hands On - NLP - Python - Simple Text Operation - 3 (Hanker Rank)
# ======================================================

def findWordFreq(text, word):
    # Write your code here
    # 1st Question
    text_dist = nltk.FreqDist(text)
    textfreq = text_dist[word]

    # 2nd Question
    text_dist = nltk.FreqDist(word for word in list(text) if word.isalpha())
    top1_text1 = text_dist.max()
    maxfreq = top1_text1

    return textfreq, maxfreq