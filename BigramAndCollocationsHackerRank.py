
import nltk
from nltk.corpus import stopwords

textcontent = "Thirty-five sports disciplines and four cultural activities will be offered during seven days of competitions. He skated with charisma, changing from one gear to another, from one direction to another, faster than a sports car. Armchair sports fans settling down to watch the Olympic Games could be for the high jump if they do not pay their TV licence fee. Such invitationals will attract more viewership for sports fans by sparking interest among sports fans. She barely noticed a flashy sports car almost run them over, until Eddie lunged forward and grabbed her body away. And he flatters the mother and she kind of gets prissy and he talks her into going for a ride in the sports car."
word = "sports"


# Write your code here

pattern = r'[A-Za-z0-9_]+'
tokenizedwords = nltk.regexp_tokenize(textcontent, pattern)

tokenizedwords = [w.lower() for w in tokenizedwords]

tokenizedwordsbigrams = list(nltk.bigrams(tokenizedwords))

stop_words = set(stopwords.words('english'))
tokenizednonstopwordsbigrams = [(w1, w2) for (w1, w2) in tokenizedwordsbigrams if not( w1 in stop_words or w2 in stop_words)]

#print(tokenizednonstopwordsbigrams)

cfd_bigrams = nltk.ConditionalFreqDist(tokenizednonstopwordsbigrams)

mostfrequentwordafter = cfd_bigrams[word].most_common(3)
print(mostfrequentwordafter)
print("-------------")

gen_text = nltk.Text(tokenizedwords)
collocationwords = gen_text.collocations()


# For Hacker Rank use the following code
# collocationwords = gen_text.collocation_list()






