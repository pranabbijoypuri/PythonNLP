import nltk



textcontent = ""
taggedtextcontent = ""
defined_tags = ""

words = nltk.word_tokenize(textcontent)
nltk_pos_tags = nltk.pos_tag(words)

tagged_pos_tag = [nltk.tag.str2tuple(word) for word in taggedtextcontent.split()]

baseline_tagger = nltk.UnigramTagger(model=defined_tags)
unigram_pos_tag = baseline_tagger.tag(words)

print(nltk_pos_tags, tagged_pos_tag, unigram_pos_tag)



