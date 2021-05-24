# !pip install spacy==2.1.0
# !pip install neuralcoref

!pip install spacy
!pip install nltk
import spacy

# import neuralcoref
# !python -m spacy download en_core_web_sm

#import codecs

from spacy import displacy

import nltk 

nltk.download('punkt')  
nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')
from nltk import pos_tag, word_tokenize, RegexpParser

# To read the text as user input. 

fname = input("Enter the text :")
#print(fname)

'''
fn = open(fname, "a")
f = codecs.open(fname, 'r')
file = open(fname, 'r')
'''

nlp = spacy.load("en_core_web_sm")

doc = nlp(fname)

#print(doc)

# To find POS-Tagging of the text in the selected text file.

print("--------------------------------****--------------------------------\n")
print("****  POS tagging  ****\n")
for token in doc:
    print(f'{token.text:{20}} {token.pos_:{20}}')
    
# We Initialsed a func "show_ents" to highlight the entities in the given text.

print("--------------------------------****--------------------------------\n")
print("****  Named-Entity Relationship  ****\n")
def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text,"-",ent.label_,"-",str(spacy.explain(ent.label_)))
    else:
        print("no named entities found")
displacy.render(doc,style='ent',jupyter=True)

# To get the syntactic and dependency parsing for the given text file.

# !pip install neuralcoref
# import spacy
# import neuralcoref
# !python -m spacy download en_core_web_sm

print("--------------------------------****--------------------------------\n")
print("****  Coreference Detection  ****\n")
#nlp = spacy.load("en_core_web_sm")
neuralcoref.add_to_pipe(nlp)
# # doc = nlp('Angela lives in Boston. She is quite happy in that city.')
doc = nlp(fname)
# print(doc)
print(doc._.coref_clusters)

print("--------------------------------****--------------------------------\n")

print("****  Syntactic Parse  ****\n")
!pip install spacy
import spacy
doc = nlp(fname)
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])
    

displacy.render(doc, style='dep')

tagged = pos_tag(word_tokenize(fname))
   
#Extract all parts of speech from text

chunker = RegexpParser("""
                       NP: {<DT>?<JJ>*<NN>}    #To extract Noun Phrases /t
                       P: {<IN>}               #To extract Prepositions /t
                       V: {<V.*>}              #To extract Verbs /t
                       PP: {<P> <NP>}          #To extract Prepostional Phrases /t
                       VP: {<V> <NP|PP>*}      #To extarct Verb Phrases
                       """)
  
# Print all parts of speech in above sentence

output = chunker.parse(tagged)
print("After Extracting\t", output)
output.draw()
