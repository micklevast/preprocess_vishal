import re
import os
import sys

import pandas as pd
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from bs4 import BeautifulSoup
from textblob import TextBlob

import unicodedata
nlp=spacy.load('en_core_web_sm')

def _get_wordcounts(x):
    length=len(str(x).split())
    return length

def _get_charcount(x):
    s=x.split() #split string to list of words
    x=''.join(s) #join words of list without space init
    return len(x)

def _get_avg_wordlength(x):
    count=_get_charcount(x)/_get_wordcounts(x)
    return count

def _get_stopwords_counts(x):
    l=len([t for t in x.split() if t in stopwords])
    return l

def _get_hashtags_counts(x):
    l=len([t for t in x.split() if t.startswith('#')])
    return l

def _get_mentions_counts(x):
    l=len([t for t in x.split() if t.startswith('@')])
    return l

def _get_digit_counts(x):
    return len([t for t in x.split() if t.isdigit()])

def _get_uppercase_counts(x):
    return len([t for t in x.split() if t.isupper()])

def _cont_to_exp(x):
    contractions={
    "hasn't":"has not",
    "havn't":"have not",
    "how'll":"how will",
    "shoulda":"should have",
    "mighta":"might have",
    "gotcha":"got you",
    "it's":"it is",
    "i'll":"i will",
    "i'm":"i am",
    "he'll":"he will",
    "don't":"do not",
    "won't":"will not",
    'u':"you",
    'ur':"your",
    "they'd":"they would",
    "bak":"back",
    "cause":"becouse",
    "dis":"this",
    "coz":"because"}
    if type(x) is str:
        for key in contractions:
            value=contractions[key]
            x=x.replace(key,value) #replacing key with value which is  expansion form of key
        return x
    else:
        return x
    
def _get_emails(x):
    emails=re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',x)
    counts=len(emails)
    return counts,emails

def _remove_emails(x):
    return re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"",x)

def _get_urls(x):
    urls=re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?',x)
    counts=len(urls)
    return counts,urls

def _remove_urls(x):
    # want to remove those url
    return re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?','',x)

def _remove_rt(x):
    return re.sub(r'\brt\b','',x).strip()

def _remove_special_chars(x):
    x=re.sub(r'[^\w ]+',"",x)
    x=' '.join(x.split())
    return x

def _remove_html_tags(x):
    return BeautifulSoup(x,'lxml').get_text()

def _remove_accented_chars(x):
    x=unicodedata.normalize('NFKD',x).encode('ascii','ignore').decode('utf-8','ignore')
    return x


def _remove_stopwords(x):
    return ' '.join([t for t in x.split() if t not in stopwords])

def _make_base(x):
    x=str(x)
    x_list=[];
    doc=nlp(x)
    
    for token in doc:
        token_to_lemma=token.lemma_
        x_list.append(token_to_lemma)
    return ' '.join(x_list)

def _get_value_counts(df,col):
    text=' '.join(df[col])
    text=text.split()
    freq=pd.Series(text).value_counts()
    return freq


def _remove_common_words(x,freq,n=20): #n=no of words to removed
    fn=freq[:n]
    x=" ".join([t for t in x.split() if t not in fn])
    return x

def _remove_rarewords(x,freq,n=20):
    fn=freq.tail(n)
    x=" ".join([t for t in x.split() if t not in fn])
    return x

def spelling_correction(x):
    x=TextBlob(x).correct()
    return x

