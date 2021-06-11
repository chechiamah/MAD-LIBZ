# import for Text bob 
from textblob import TextBlob
import random
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#define score variables and indices
noun_score = 0 
adjective_score = 0 
adverb_score =  0
verb_score = 0 
score = 0 

indices_of_nouns = []
indices_of_adjectives = []
indices_of_verbs = []
indices_of_adverbs = []

text = "I found my missing locker key! he said. He happily put the key into his backpack and was smiling as he walked out the door. The day was still dark and gray but his mood was now a sunny one"

# define text 


# credits -->  https://github.com/thecodingsophist/madlibs/blob/master/madlibs-extra-edition.py 

#Parts of Speech with their tags 


# return true/ noun 
# give something to check to find noun 
# take a tagged and ask if it 
# needs something to check tag against 
# look at all in text and tagged_text and make a condtional for the following:
def noun (tag):
  if tag == 'NN':
    return True 

def adjective(tag):
  adjective_tags = set(["JJ", "JJR", "JJS"])
  if tag in adjective_tags:
    return True 

def adverb (tag):
  adverb_tags = set(["RB", "RBR", "RBS"])
  if tag in adverb_tags:
    return True

def verb (tag):
  verb_tags = set(["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"])
  if tag in verb_tags:
    return True

    
#SPECIFIC 
#test(in a new function)
#tag my text 

# for word in tagged text
  #if work is a noun (adjective, verb, adverb)
    #replace it is text with a ''
  #return modified text
 
def template (word): 
  for word in text: 
   if word == noun or adjective or verb or adverb: 
    text.replace(" ")
  return template 
  

#
# make the part of speech functions take an input 
# test that take against the tag IDs 

# for every word in tagged text: 
# if word is  a noun then 

def find_partofspeech (partofspeech): 
  global noun_score
  global adjective_score
  global adverb_score
  global verb_score
  if partofspeech == "noun":
   noun_score += 1 
  if partofspeech == "adjective": 
   adjective_score += 1 
  if partofspeech == "adverb": 
   adverb_score += 1 
  if partofspeech == "verb": 
    verb_score += 1 



def take_nouns_from(template):
    #takes all the nouns of the parameter text
    blob = TextBlob(template)
    template_tagged = blob.tags
    # indices_of_nouns = []
    tagged_words = [x[1] for x in template_tagged]
    index = 0
    global indices_of_nouns
    for tag in tagged_words:
        global noun 
        if (noun(tag)):
            indices_of_nouns += [index]
        index += 1
        tagged_words = tagged_words[index:]

    nouns = []
    words = [x[0] for x in template_tagged]

    for num in range(0, len(indices_of_nouns)):
        noun_index = indices_of_nouns[num]
        nouns += [words[noun_index]]

    for i in indices_of_nouns:
      print(i)
    return nouns

def take_adjectives_from(template): 
    #takes all the adjectives of the parameter text
    #also used to take out all the adjectives in the support text
    blob = TextBlob(template)
    template_tagged = blob.tags
    #indices_of_adjectives = []
    tagged_words = [x[1] for x in template_tagged]
    index = 0
    global indices_of_adjectives
    for tag in tagged_words:
        global adjective
        if (adjective(tag)): 
            indices_of_adjectives += [index]
        index += 1
        tagged_words = tagged_words[index:]

    adjectives = []
    words = [x[0] for x in template_tagged]

    for num in range(0, len(indices_of_adjectives)):
        adjective_index = indices_of_adjectives[num]
        adjectives += [words[adjective_index]]
    for i in indices_of_adjectives: 
      print(i)
    return adjectives

# adverbs 
def take_adverbs_from(template):
    #takes all the adverbs of the parameter text
    #also used to take out all the adverbs in the support text
    blob = TextBlob(template)
    template_tagged = blob.tags
    #indices_of_adverbs = []
    tagged_words = [x[1] for x in template_tagged]
    index = 0
    global indices_of_adverbs
    for tag in tagged_words:
        #print(tag)
        global adverb
        if(adverb(tag)):
          indices_of_adverbs += [index] 
        index += 1
        tagged_words = tagged_words[index:]

    adverbs = []
    words = [x[0] for x in template_tagged]

    for num in range(0, len(indices_of_adverbs)):
        adverb_index = indices_of_adverbs[num]
        adverbs += [words[adverb_index]]
    for adverb in adverbs:
      print(adverb)
    return adverbs
    
# verbs 
def take_verbs_from(template):
    #takes all the verbs of the parameter text
    #also used to take out all the verbs in the support text
    blob = TextBlob(template)
    template_tagged = blob.tags
    #indices_of_verbs = []
    tagged_words = [x[1] for x in template_tagged]
    index = 0
    global indices_of_verbs
    for tag in tagged_words:
        #print(tag)
        global verb
        if(verb(tag)):
          indices_of_verbs += [index]
        index += 1
        tagged_words = tagged_words[index:]

    verbs = []
    words = [x[0] for x in template_tagged]

    for num in range(0, len(indices_of_verbs)):
        verb_index = indices_of_verbs[num]
        verbs += [words[verb_index]]
    for verb in verbs:
      print(verb)
    return verbs
    

# set up w/ instructions

# FIX THIS TO MAKE IT TEST FOR EACH TIME IT APPEARS INSTEAD 

#make a 'while True' loop 
#COPY THIS: https://wiki.python.org/moin/ForLoop

#use the indices of nouns to put the words the user entered into that index 

#str.replace(text[4], user_noun[0])
# create a user variable 

def madlibs(): 
  print ("Welcome to MadLibs the game. In this games we will ask you to give us the parts of speech. At the end of the game, you will recieve a score that tells you how many you got correct.")
  
  noun_loop = len(take_nouns_from(text))
  new_text = text
  for i in range(0,noun_loop): 
    nouninput = input ("Enter a noun:")
    nltk.tag.pos_tag([nouninput])
       #or use your tagger from first project or use your textblob
    #if noun('NN'):
      #find_partofspeech("noun")
    new_text = ' '.join([x if index != indices_of_nouns[i] else nouninput for index,x in enumerate(new_text.split())])
  print(new_text)
  
  adjective_loop = len(take_adjectives_from(new_text))
  for i in range(0,adjective_loop): 
    adjectiveinput = input ("Enter an adjective:")
    #tag adjectiveinput
    #if adjective(set(["JJ", "JJR", "JJS"])):
      #find_partofspeech("adjective")
    new_text = ' '.join([x if index != indices_of_adjectives[i] else adjectiveinput for index,x in enumerate(new_text.split())]) 
  print(new_text)

  verb_loop = len(take_verbs_from(new_text))
  for i in range(0,verb_loop): 
    verbinput = input ("Enter an verb:")
    #if verb(set(["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"])):
      #find_partofspeech("verb")
    new_text = ' '.join([x if index != indices_of_verbs[i] else verbinput for index,x in enumerate(new_text.split())]) 
  print(new_text)

  adverb_loop = len(take_adverbs_from(new_text))
  for i in range(0,adverb_loop): 
    adverbinput = input ("Enter an adverb:")
    #if adverb(set(["RB", "RBR", "RBS"])):
      #find_partofspeech("adverb")
    new_text = ' '.join([x if index != indices_of_adverbs[i] else adverbinput for index,x in enumerate(new_text.split())]) 
  print(new_text)

  print()
#incorporate a point system (ask the group)
madlibs()
print(text)


#ASK For help 
#print("score:" + int(score) )


# last step: integration 

# tag a paragrapgh 
# do things based oof of tag input 
# modify and create new paragraph 

#score = (noun_score + adjective_score + adverb_score + verb_score)

#print(score); 
#Note: I commented out notes and notes and return functions that were part of the "take from" functions 

