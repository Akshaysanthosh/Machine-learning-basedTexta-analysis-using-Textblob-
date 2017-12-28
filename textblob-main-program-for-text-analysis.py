"""
A Machine learning based text analyizing progarm that use textblob
(language processing libarary) for  Sentiment Analysis and Identifiying Part-of-speech , 
and noun phrase Tokenization ,Words and inflection and to Get word and 
noun phrase frequencies

@author: Akshay santhosh (sakshay797@gmail.com)
"""

#importing from textblob libarary

from textblob import TextBlob

#give your input text

Input_text=('''' provide your text here ''')


wiki=TextBlob(input_text)

# 1 . For sentiment analysis

wiki.sentiment.polarity


# 2.ForPart-of-speech tags and noun phrases…

wiki.pos_tags

wiki.noun_phrases  

#3. Tokenization

zen = TextBlob("text")

zen.words            

zen.sentences


# 4.for to Get word and  noun phrase frequencies
#use specific word from the text


wiki.word_counts['specific word or Noun'] 
