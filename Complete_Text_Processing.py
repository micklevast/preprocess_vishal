#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd


# In[13]:


import numpy as np


# In[14]:


import spacy


# In[ ]:





# In[15]:


from spacy.lang.en.stop_words import STOP_WORDS as stopwords


# In[16]:


df=pd.read_csv('twitter4000.csv' ,encoding='latin1')


# In[22]:


df  #if sentiment is 0=> negative
#     ifsentiment is 1=>positive


# In[27]:


df.head(50)


# In[18]:


df.head(3)


# In[20]:


df['sentiment'].value_counts()


# In[ ]:





# ## Word counts

# In[21]:


len('this is text')


# In[22]:


len('this is text'.split()) #this split() method give us total word in the string


# In[36]:


y=lambda x:  (x*x)


# In[37]:


y(5)


# In[40]:


words_list=lambda x:str(x).split()


# In[41]:


df['twitts'].apply(words_list)


# In[42]:


df['twitts'].apply(lambda x:len(str(x).split())) # x is sentence of column twitts
# twitts ke string pass as argument in lambda function


# In[7]:


# store in df number of words a line have
df['words_count']=df['twitts'].apply(lambda x:len(str(x).split()))


# In[46]:


df


# In[47]:


df['words_count'].max()


# In[48]:


df['words_count'].min()


# In[50]:


# check in which line words_count is =1
df['words_count']==1


# In[52]:


df[df['words_count']==1] #print which line have word_count==1


# In[53]:


df[df['sentiment']==0] #people with negative sentiment


# In[ ]:





# ## Characters Count

# In[14]:


len("this is  ") #space char also counted #=>to avoid that problem we can write a custom function


# In[20]:


x="this sister is very noisy"


# In[21]:


s=x.split() #split functio split string into[ list] of word
s


# In[4]:


ll=["vishal",'chauhan','mob number:',9820314081]
ll


# In[7]:


" ".join((ll))


# In[ ]:





# In[22]:


def char_count(x):
    s=x.split() #split string to list of words
    x=''.join(s) #join words of list without space init
    return len(x)


# In[23]:


char_count('this is  ') #here we don't count space


# In[24]:


df['char_counts']=df['twitts'].apply(lambda x:len(x))


# In[25]:


df


# In[26]:


df['char_counts_withoutSpace']=df['twitts'].apply(lambda x:char_count(x))


# In[46]:


df


# In[ ]:





# ## Average Word Length

# In[12]:


x="this is" #char=6 word=2=>so 6/2=3 charector per word or avg word len=3
y='THANKYOU GUYS' #char=12 word=2=>12/2=6 char per words


# In[13]:


def char_count(x):
    s=str(x).split()
    x="".join(s);
    return (len(x));


# In[14]:


char_count(x)


# In[15]:


def word_counts(x):
    return(len(x.split()))


# In[16]:


word_counts(y)


# In[27]:


df['char_counts_withoutSpace']


# In[18]:


df['word_counts']=df['twitts'].apply(lambda x:word_counts(x))
df


# In[53]:


df['word_counts']


# In[28]:


df['avg_word_len']=df['char_counts_withoutSpace']/df['word_counts']


# In[58]:


df


# In[59]:


df.sample(4)


# In[61]:


# here add new column in twitts list
df['analyser']='vishal chauhan'


# In[62]:


df


# In[ ]:





# ## Stop words count

# In[ ]:


# What are stop words? 🤔
# The words which are generally filtered out before processing a natural language are called stop words.
# These are actually the most common words in any language (like articles, prepositions, pronouns, conjunctions, etc)
# and does not add much information to the text. Examples of a few stop words in English are “the”, “a”, “an”, “so”, “what”.


# In[ ]:


# from spacy.lang.en.stop_words import STOP_WORDS as stopwords  #here we imported imp library


# In[63]:


stopwords  #this are the words which occurs very frequently=>tell very less about text sentiment


# In[64]:


print(stopwords)


# In[65]:


len(stopwords)


# In[66]:


# so what is sence of removing the stopwords
len(df)  #outof these 


# In[67]:


x="this is the textdata"


# In[68]:


x.split() #we get tokenise version of text data


# In[3]:


def vowel(x):
    if x=='a'or x=='e'or x=='i'or x=='o'or x=='u':
        return 1;
    else:
        return 0;


# In[6]:


# Example for Iterating through a string Using List Comprehension
h_letters = [ letter for letter in 'human']
print( h_letters)


# In[5]:


# Example for Iterating through a string Using List Comprehension
h_letters = [ letter for letter in 'human'if vowel(letter)==1]
print( h_letters)


# In[75]:


[stop_words_found_within_x for stop_words_found_within_x in x.split() if stop_words_found_within_x in stopwords]
#     jo stopword x ke stopwords se milte hai use ek comprenhensive list bna do


# In[76]:


[t for t in x.split() if t in stopwords]


# In[77]:


len([t for t in x.split() if t in stopwords])


# In[ ]:


# above methos is for to know which is stopwords inside a strng


# In[79]:


xx=df['twitts'].apply(lambda x:len([t for t in x.split() if t in stopwords])) #it will return a count of stopword in each line of twitts


# In[80]:


df['stop_words_len']=xx


# In[81]:


df


# In[82]:


df.sample(5) #this will gave us some random rows


# In[ ]:





# ## Count #HashTags and @Mentions

# In[86]:


x='this is #hashtag and this is @mention'


# In[84]:


x.split()  #this is tokenise version of x string


# In[85]:


[t for t in x.split() if t.startswith('#')] #read those t witch start with #


# In[87]:


[t for t in x.split() if t.startswith('@')]


# In[88]:


len([t for t in x.split() if t.startswith('@')])


# In[89]:


df['mentions_count']=df['twitts'].apply(lambda x:len([t for t in x.split() if t.startswith('@')]))


# In[91]:


df['hashtags_count']=df['twitts'].apply(lambda x:len([t for t in x.split() if t.startswith('#')]))


# In[92]:


df


# In[96]:


df.sample(10)


# In[ ]:





# ## If numeric digits are present in twitts

# In[97]:


x='this is 1 and 2'


# In[98]:


x.split()


# In[99]:


x.split()[2] #excess any items of list


# In[100]:


x.split()[4].isdigit()


# In[101]:


x.split()[0].isdigit()


# In[102]:


[t for t in x.split() if t.isdigit()]


# In[103]:


len([t for t in x.split() if t.isdigit()])


# In[105]:


df['numeric_count']=df['twitts'].apply(lambda x:len([t for t in x.split() if t.isdigit()]))


# In[106]:


df


# In[107]:


df.sample(5)


# In[ ]:





# ## Upper case words count

# In[108]:


# intensity of upper case words are high in text so the sentiment also


# In[112]:


x="I AM HAPPY"
y='i am happy'


# In[110]:


[t for t in x.split() if t.isupper()]


# In[113]:


[t for t in y.split() if t.isupper()]


# In[114]:


len([t for t in x.split() if t.isupper()])


# In[115]:


df['upper_count']=df['twitts'].apply(lambda x:len([t for t in x.split() if t.isupper()]))


# In[116]:


df


# In[118]:


df.iloc[3998]['twitts'] #to get a particular line


# In[ ]:





# # Preprocessing and cleaning

# ## Lower case conversion

# In[120]:


x="this is text"
t="THIS IS TEXT"
z="My name is KHAN"


# In[121]:


x.lower()


# In[122]:


t.lower() #this is known as text normalisation


# In[123]:


z.lower()


# In[124]:


a=45


# In[125]:


a.lower() #this will gave an error
# to avoid this problen 
# we need to convert each token into string then aplly lower() method


# In[126]:


str(a).lower()


# In[127]:


df['twitts']=df['twitts'].apply(lambda x:str(x).lower()) #make all twitts to lower case


# In[128]:





# In[129]:


df.iloc[3256]


# In[131]:


df.iloc[3256]['twitts']


# In[132]:


t.upper()


# In[15]:


df['twitts'][222]


# In[17]:


df.loc[222]['twitts']


# In[ ]:





# In[ ]:





# ## Contraction to Expansion

# In[8]:


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
    "coz":"because"
}


# In[167]:


x="i'm don't he'll" #'i am do not he will' =>this is expansion of given x


# In[168]:


def cont_to_exp(x): #contraction to expansion
    if type(x) is str:
        for key in contractions:
            value=contractions[key]
            x=x.replace(key,value) #replacing key with value which is  expansion form of key
        return x
    else:
        return x
    
    


# In[169]:


cont_to_exp(x)


# In[ ]:





# In[ ]:





# In[139]:


df.iloc[4]['twitts']


# In[140]:


df.iloc[3999]['twitts']


# In[172]:


get_ipython().run_cell_magic('timeit', ' #give time for to complete run', "df['twitts_in_expansion_from_contraction']=df['twitts'].apply(lambda x:cont_to_exp(x))")


# In[8]:


df


# In[ ]:





# ## Counts and remve emails

# In[18]:


x="my gmail is visindra2000@gmial.com ohk."


# In[21]:


def is_word_contain_in_sent(w,s):
    if w in s:
        return 1
    else:
        return 0


# In[22]:


is_word_contain_in_sent('.com',x)


# In[ ]:


df['twitts'].is_word_contain_in_sent('.com')


# In[23]:


df['is eamil']=df['twitts'].apply(lambda x:is_word_contain_in_sent('.com',x))


# In[24]:


df


# In[23]:


import re #by method 2


# In[27]:


# Series.str can be used to access the values of the series as strings and apply several methods to it.
# Pandas Series.str.contains() function is used to test if pattern or regex is contained within a string of a Series or Index.
# The function returns boolean Series or Index based on whether a given pattern or regex is contained within 
# a string of a Series or Index.

# importing pandas as pd
import pandas as pd

# importing re for regular expressions
import re

# Creating the Series
sr = pd.Series(['New_York', 'Lisbon', 'Tokyo', 'Paris', 'Munich'])

# Creating the index
idx = ['City 1', 'City 2', 'City 3', 'City 4', 'City 5']

# set the index
sr.index = idx

# Print the series
print(sr)

# find if 'is' substring is present
result = sr.str.contains(pat = 'is')
 
# print the result
print(result)


# In[28]:


sr.str


# In[180]:


df['twitts'].str.contains('.com')


# In[ ]:





# In[179]:


df[df['twitts'].str.contains('gmail.com')]


# In[182]:


df.iloc[2448]['twitts']


# In[184]:


df[df['twitts'].str.contains('hotmail.com')]


# In[185]:


df.iloc[3713]['twitts']


# In[198]:


x='@securerecs arghh me please  markbradbury_16@hotmail.com  markbradbury_16@hotmail.comxyz end'


# In[199]:


re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',x) #this is a way to find xyz@.abc type of words in sentences


# In[200]:


re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)+\b',x)


# In[194]:


df['emails']=df['twitts'].apply(lambda x:re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',x))


# In[195]:


df['emails_count']=df['emails'].apply(lambda x:len(x))


# In[196]:


df


# In[197]:


df[df['emails_count']>0]


# In[29]:


re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"email_removed_filled",x)  
#this is a way to replace and fill=>substitute=sub()


# In[207]:


df['twitts']=df['twitts'].apply(lambda x:re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"",x)) #substitute with space


# In[ ]:





# In[208]:


df[df['emails_count']>0]


# In[ ]:





# ## Counts URLs and Remove it

# In[57]:


x="hi thanks for vsiist http://youtube.com/kgptalkie"
y='hello every body https://git:@git.com/username/repo.git=riif?%$?'


# In[31]:


x


# In[ ]:


#  shh://git:@git.com/username/repo.git=riif?%$?

# http|https|ftp|ssh  +>read as http or https or ftp or ssh


# In[61]:


re.findall(r'(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*',y)
# here's an explanation:
# (https?:\/\/) matches http:// or https://
# (\s)* optional whitespaces
# (www\.)? optionally matches www.
# (\s)* optionally matches whitespaces
# ((\w|\s)+\.)* matches 0 or more of one or more word characters followed by a period
# ([\w\-\s]+\/)* matches 0 or more of one or more words(or a dash or a space) followed by '\'
# ([\w\-]+) any remaining path at the end of the url followed by an optional ending
# ((\?)?[\w\s]*=\s*[\w\%&]*)* matches ending query params (even with white spaces,etc)


# In[59]:


re.findall(r'http://\S+|https://\S+',y)


# In[58]:


re.findall(r'http://\S+|https://\S+',x)


# In[60]:


re.findall(r'(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*',x)


# In[62]:


re.findall(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b',x)


# In[ ]:





# In[63]:


# this is best method=>by sir
re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?',x)


# In[64]:


df['url_flags']=df['twitts'].apply(lambda x:len(re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?',x)))


# In[65]:


df[df['url_flags']>0]


# In[1]:


df[df['url_flags']>0].sample(5)


# In[72]:


# want to remove those url
re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?','',x)


# In[73]:


df['twitts_without_email']=df['twitts'].apply(lambda x:re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?','',x))


# In[82]:


df['twitts_without_email'].sample(6)


# In[ ]:





# ## remove ReTwitts(RT)

# In[27]:


x="rt @vishal:hello worldrt @pavan:hello world rtnavale"


# In[28]:


re.findall(r'\brt\b',x) #find string =>\b
# \brt\b=>means before and after of 'rt' there should not any char


# In[30]:


r=re.sub(r'\brt\b','',x)  #=>here rt is removed
r
r.strip()


# In[100]:


y="  this is vishal    ohk "
y.strip() #end ke extra space are removed


# In[103]:


r.strip()


# In[ ]:





# In[104]:


df['twitts']=df['twitts'].apply(lambda x:re.sub(r'\brt\b','',x).strip())


# In[ ]:





# ## Special chars removal or punctuation removal

# In[ ]:


# most coomon re 
Basic Syntax
.             One character except new line
\.            A period. \ escapes a special character.
\d            One digit
\D            One non-digit
\w            One word character including digits
\W            One non-word character
\s            One whitespace
\S            One non-whitespace
\b            Word boundary
\n            Newline
\t            Tab

Modifiers
$             End of string
^             Start of string
ab|cd         Matches ab or de.
[ab-d]	      One character of: a, b, c, d
[^ab-d]	      One character except: a, b, c, d
()            Items within parenthesis are retrieved
(a(bc))       Items within the sub-parenthesis are retrieved

Repetitions
[ab]{2}       Exactly 2 continuous occurrences of a or b
[ab]{2,5}     2 to 5 continuous occurrences of a or b
[ab]{2,}      2 or more continuous occurrences of a or b
+             One or more
*             Zero or more
get_ipython().run_line_magic('pinfo', '0')


# In[105]:


df.sample(4)


# In[112]:


x='@Onion my way 2 da pool party! Lost a lil weight!, ...i...?'

x


# In[113]:


re.sub(r'[^\w]+',"",x)


# In[114]:


re.sub(r'[^\w ]+',"",x) #so we  remove all special char and punctuation marks from data


# In[115]:


df['twitts_without_punctuation']=df['twitts'].apply(lambda x:re.sub(r'[^\w ]+',"",x))


# In[116]:


df


# In[117]:


df.sample(5)


# In[ ]:





# ## Remove RT

# In[34]:


import re


# In[ ]:


# rt=>retwitts


# In[31]:


x='RT @username hello hi'


# In[29]:


df[df['twitts'].str.contains('RT ')]


# In[30]:


df[df['twitts'].str.contains('rt @ ')]


# In[36]:


df[df['twitts'].str.contains('rt ')] #find which twitts contains rt


# In[ ]:


df[df['twitts'].str.contains('RT ')]


# In[32]:


x


# In[37]:


re.sub(r'\bRT\b',"",x) #\bRT\b these are \b boundries


# In[38]:


y='RT @username hello hirt RTih'


# In[42]:


re.sub(r'\bRT\b',"",y) #this will not remove (RTih) which also contains RT but not on boundries
# notice here we got some extra space so we want to trim them


# In[41]:


re.sub(r'\bRT\b',"",y).strip()


# In[44]:


df['twitts_removed_rt']=df['twitts'].apply(lambda x:re.sub(r'\bRT\b',"",x).strip())


# In[45]:


df


# In[ ]:





# ## Special chars removal or punctuation removal

# In[46]:


df.sample(3)


# In[47]:


x="@caitiebecker Awww I'm sorry that you are sick.."


# In[48]:


re.sub(r'[\w]+',"",x) #substitute the words with ""=>then we get only  alpha-numeric words(special char)


# In[49]:


re.sub(r'[^\w]+',"",x) #substitue which is not the words by ""


# In[50]:


re.sub(r'[^\w ]+',"",x) #kepp seprate every words


# In[51]:


df["twitts_without_specialChar"]=df['twitts'].apply(lambda x:re.sub(r'[^\w ]+',"",x))


# In[54]:


df.sample(3)


# In[ ]:





# ## Remove multiple space "hi    HEllo    "

# In[55]:


x='hi     hello                how r u'


# In[56]:


x.split()


# In[57]:


' '.join(x.split())


# In[58]:


df['twitts_without_extra_space']=df['twitts'].apply(lambda x:' '.join(x.split()))


# In[59]:


df.sample(5)


# In[ ]:





# ## Remove Html tags

# In[31]:


get_ipython().system('pip install beautifulsoup4')


# In[32]:


from bs4 import BeautifulSoup


# In[38]:


from bs4 import BeautifulSoup as bs


# In[33]:


BeautifulSoup


# In[39]:


bs


# In[36]:


x="<html><h1> THis is vishal chauhan  </h1></html>"
x


# In[37]:


x.replace('<html><h1>','')


# In[68]:


x.replace('<html><h1>','').replace('</h1></html>',"") #this  is normal way to replace what we want
# but not proper way


# In[ ]:





# In[76]:


BeautifulSoup(x,'lxml').get_text()


# In[77]:


BeautifulSoup(x,'lxml').get_text().strip() #use strip() to remove extra space
# theses is best way to get plain text from html tags


# In[74]:


print(BeautifulSoup(x,'lxml'))
print(BeautifulSoup(x))


# In[35]:


BeautifulSoup(x).get_text()


# In[44]:


bs(x).get_text().strip()


# In[ ]:





# In[79]:


get_ipython().run_cell_magic('time', ' ', "#to count wntire time to run these wntire functional block\ndf['twitts_plainTXT']=df['twitts'].apply(lambda x:BeautifulSoup(x,'lxml').get_text().strip())")


# In[80]:


df.sample(3)


# In[ ]:





# ## Remove Accented Chars

# In[ ]:


# Accented Characters - Wordfasthttps://wordfast.com › WFP
# Accent. Sample. Shortcut. Notes. Acute. Ó ó. Ctrl+', V. '= apostrophe key. V= any vowel. Circumflex. Ô ô. Shift+Ctrl+^, V. Grave. Ò ò. Ctrl+`, V. Tilde.


# In[45]:


import unicodedata


# In[ ]:





# In[ ]:





# In[84]:


x="'à, è, ì, ò, ù,
À, È, Ì, Ò, Ù

CTRL+` (ACCENT GRAVE), the letter

á, é, í, ó, ú, ý
Á, É, Í, Ó, Ú, Ý

CTRL+' (APOSTROPHE), the letter

â, ê, î, ô, û
Â, Ê, Î, Ô, Û

CTRL+SHIFT+^ (CARET), the letter

ã, ñ, õ
Ã, Ñ, Õ'"


# In[92]:



char = "áêÕ"
len(char)

[ unicodedata.name(c) for c in char ]


# In[ ]:





# In[ ]:





# In[85]:


x="Âccêntêd têxt"


# In[86]:


x


# In[87]:


import unicodedata


# In[ ]:


get_ipython().set_next_input('What is NFKD normalization');get_ipython().run_line_magic('pinfo', 'normalization')
Normalization Form Canonical Composition. Characters are decomposed and then recomposed by canonical equivalence.
NFKD. Normalization Form Compatibility Decomposition. Characters are decomposed by compatibility, and multiple combining 
characters are arranged in a specific order.


# In[88]:


def remove_accented_chars(x):
    x=unicodedata.normalize('NFKD',x).encode('ascii','ignore').decode('utf-8','ignore')
    return x


# 

# In[89]:


remove_accented_chars(x)


# In[95]:


df['twitts']=df['twitts'].apply(lambda x:remove_accented_chars(x))


# In[96]:


df.sample(3)


# In[ ]:





# ## Remove stopwords

# In[97]:


print(stopwords)


# In[98]:


x="this is a stop words ohk."


# In[101]:


xx=[t for t in x.split() if t not in stopwords] #making comprenhensive list
xx


# In[103]:


xxx=[t for t in x.split() if t in stopwords] 
xxx


# In[104]:


x_without_stopwords=' '.join([t for t in x.split() if t not in stopwords])


# In[105]:


x_without_stopwords


# In[ ]:





# In[106]:


df['twitts_no_stopwords']=df['twitts'].apply(lambda x:' '.join([t for t in x.split() if t not in stopwords]))


# In[107]:


df.sample(5)


# In[ ]:





# ## Convert into base or root from of word
# 

# In[108]:


nlp=spacy.load('en_core_web_sm')


# In[110]:


text2 = "I am hanging outs in a gardens"  #hanging base is hang
doc2 = nlp(text2)
" ".join([token.lemma_ for token in doc2])


# In[112]:


text="i would follow yours paths ohk.then only i could succeeded in my lifes goals, i did that in proper ways so succeeded"
doc=nlp(text)
" ".join(token.lemma_ for token in doc)

# did->do
# paths->path
# succeeded->succeed


# In[118]:


def make_to_base(x):
    x=str(x)
    x_list=[];
    doc=nlp(x)
    
    for token in doc:
        token_to_lemma=token.lemma_
        x_list.append(token_to_lemma)
    return ' '.join(x_list)


# In[119]:


make_to_base(x) #is->be
# to avoid these problem


# In[122]:


def make_to_base(x):
    x=str(x)
    x_list=[];
    doc=nlp(x)
    
    for token in doc:
        token_to_lemma=token.lemma_
        if token_to_lemma=='-PRON-' or token_to_lemma=='be':
            token_to_lemma=token.text  #means no change
        
        x_list.append(token_to_lemma)
    return ' '.join(x_list)


# In[123]:


make_to_base(x)


# In[124]:


df['twitts_apply_lemma']=df['twitts'].apply(lambda x:make_to_base(x))


# In[125]:


df.sample(3)


# In[ ]:





# ## Coomon Words removal

# In[46]:


x="this is  this is okey bye" #this is common words


# In[47]:


df['twitts']


# In[49]:


text=" ".join(df['twitts'])


# In[50]:


len(text)


# In[51]:


len(text.split())


# In[ ]:


# calculate freq


# In[52]:


text1=text.split()


# In[53]:



pd.Series(text1)


# In[54]:


pd.Series(text1).value_counts() # convert text into pad series


# In[55]:


comm_freq=pd.Series(text1).value_counts()


# In[56]:


f20=comm_freq[:20] #first 20 common words


# In[57]:


f20  #generally stopwords are the most common frequently words in text data


# In[62]:


x="this is my name ohk hello world and i am vishal"


# In[63]:


l=[t for t in x.split() if t not in f20]


# In[64]:


l


# In[67]:


df['twitts_without_common_words']=df['twitts'].apply(lambda x:" ".join([t for t in x.split() if t not in f20]))
# or
# df['twitts_without_common_words']=df['twitts'].apply(lambda x:" ".join([t for t in x.split() if t not in stopwords]))


# In[68]:


df.sample(3)


# In[ ]:





# ## rare occuring words removal

# 

# In[17]:


text=df['twitts']
text


# In[18]:


text=" ".join(text)
text


# In[19]:


lst=text.split()


# In[77]:


lst


# In[20]:


count_freq=pd.Series(lst).value_counts()


# In[85]:


f20=count_freq[:20]


# In[88]:


count_freq.head(5)


# In[99]:


count_freq


# In[119]:


[count_freq<=1]


# In[ ]:





# In[135]:


rare_twitts=comm_freq.tail(11439)  #these are less common words  in twitters data twitts


# In[136]:


df['twitts_rare_words_removed']=df['twitts'].apply(lambda x:" ".join([t for t in x.split() if t not in rare_twitts]))


# In[138]:


get_ipython().run_cell_magic('timeit', '', 'df.sample(3)')


# In[ ]:





# ## Word CLoud VISulization

# In[21]:


# !pip install wordcloud


# In[7]:


get_ipython().system('pip install wordcloud')


# In[6]:


from wordcloud import WordCloud


# In[8]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[22]:


lst


# In[23]:


text=" ".join(lst)


# In[24]:


text


# In[25]:


len(text)


# In[26]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:





# In[28]:


wc=WordCloud(width=800,height=500).generate(text)


# In[30]:


plt.imshow(wc)   #give word cloud in which words are most common freq occuring words


# In[38]:


freq_occur=pd.Series(lst).value_counts()


# In[39]:


freq_occur.head(10)


# In[ ]:





# In[ ]:


# Word Cloud is a data visualization technique used for representing text data in which the size of each word indicates
# its frequency or importance. Significant textual data points can be highlighted using a word cloud.
# Word clouds are widely used for analyzing data from social network websites.


# In[51]:


wc2=WordCloud(width=1000,height=800,background_color='yellow').generate(text)
plt.imshow(wc2)
plt.show()


# In[ ]:





# In[49]:


wc3 = WordCloud(width = 800, height = 800,
                background_color ='red',
                stopwords = stopwords,
                min_font_size = 10).generate(text)


# In[50]:


# plot the WordCloud image                      
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wc3)
plt.axis("off")
plt.tight_layout(pad = -5)
 
plt.show()


# In[48]:


# plot the WordCloud image                      
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wc3)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()


# In[ ]:





# ## Spelling Correction

# In[52]:


get_ipython().system('pip install -U textblob')


# In[53]:


get_ipython().system('python -m textblob.download_corpora')


# In[54]:


from textblob import TextBlob


# In[77]:


x="vishal is a cllever boyy so don't abuse himmm hee will reply verry hardd."


# In[75]:


TextBlob(x)


# In[78]:


x=TextBlob(x).correct()
x


# In[ ]:





# ## Tokenisation with TextBlob

# In[79]:


x="thanks#watching this video. please like it"


# In[80]:


TextBlob(x).words # token using TextBlob


# In[81]:


# token using spacy
doc=nlp(x)


# In[82]:


nlp=spacy.load('en_core_web_sm')


# In[83]:


doc=nlp(x)
doc


# In[84]:


for token in doc:
    print(token)


# In[ ]:





# ## language Translation and detection

# In[103]:


x


# In[93]:


# TextBlob(x).words


# In[91]:


tb=TextBlob(x)
tb.detect_language()


# In[92]:


tb.translate(from_lang='auto',to='hi')


# In[100]:


y="ब्रेकिंग न्यूज: जो बिडेन अमेरिका के राष्ट्रपति हैं जो चंद्रमा के समान बहुत चमकदार दिख रहे हैं।"


# In[97]:


tb=TextBlob(y)


# In[98]:


tb.translate(from_lang='hi',to='en')


# In[ ]:


mr	Marathi
mai	 	Maithili
chi (B)
zho (T)	zh	Chinese
bho	 	Bhojpuri
goh	 	German
guj	gu	Gujarati
ar->areabic
bn->bengali


# In[119]:


x="તાજા સમાચાર:જો બિડેન અમેરિકાના પ્રમુખ છે જે ચંદ્ર જેવા ચમકતા દેખાતા હોય છે."
tb=TextBlob(x)
tb.translate(to='bn')


# In[107]:


x='Breaking news:joe Bidden is the president of America looking very shinning as the similar to the moon.'
tb=TextBlob(x)
tb.translate(to='gu')


# In[110]:


x='Breaking news:joe Bidden is the president of America looking very shinning as the similar to the moon.'
tb=TextBlob(x)
tb.translate(to='zh')


# In[111]:


x="突发新闻：乔·比登是美国总统，看起来很像月亮。"
tb=TextBlob(x)
tb.translate(to='hi')


# In[112]:


x="突发新闻：乔·比登是美国总统，看起来很像月亮。"
tb=TextBlob(x)
tb.translate(to='mr')


# In[117]:


x='Breaking news:joe Bidden is the president of America looking very shinning as the similar to the moon.'
tb=TextBlob(x)
tb.translate(to='fr')


# In[118]:


x='Breaking news:joe Bidden is the president of America looking very shinning as the similar to the moon.'
tb=TextBlob(x)
tb.translate(to='ar')


# In[ ]:





# ## Use TextBlob's inbuilt Sentiment Classifier

# In[120]:


from textblob.sentiments import NaiveBayesAnalyzer


# In[121]:


x="we are going to stand together.as a result we are gonna win this game"


# In[122]:


tb=TextBlob(x,analyzer=NaiveBayesAnalyzer())


# In[123]:


tb


# In[124]:


tb.sentiment


# In[125]:


y="hey bro what are u doing here. go there otherwise i will complain to your seniors"


# In[128]:


tb=TextBlob(y,analyzer=NaiveBayesAnalyzer())
tb.sentiment
# p_neg=probability of negative
# p_pos=probability of positive


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Detecting Nouns

# In[85]:


x="Breaking news:joe Bidden is the president of America looking very shinning as the similar to the moon."


# In[86]:


doc2=nlp(x)


# In[88]:


for noun in doc2.noun_chunks:
    print(noun)


# In[ ]:





# ## language Translation and detection

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




