import spacy
# Import required libraries
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


import codecs

fname = input("Enter the location of the text file :")
fn = open(fname, "a")
f = codecs.open(fname, 'r')

nlp = spacy.load("en_core_web_sm")

doc = nlp(f.read())


from nltk import pos_tag, word_tokenize, RegexpParser   
from spacy import displacy


#nlp = spacy.load("en_core_web_sm")
#doc = nlp("The quick brown fox jumps over the lazy dog")
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])
displacy.render(doc, style='dep')


# Example text
file = open(fname, 'r')
print(sample_text)
#"The quick brown fox jumps over the lazy dog"
   
# Find all parts of speech in above sentence
tagged = pos_tag(word_tokenize(file.read()))
   
#Extract all parts of speech from any text
chunker = RegexpParser("""
                       NP: {<DT>?<JJ>*<NN>}    #To extract Noun Phrases
                       P: {<IN>}               #To extract Prepositions
                       V: {<V.*>}              #To extract Verbs
                       PP: {<P> <NP>}          #To extract Prepostional Phrases
                       VP: {<V> <NP|PP>*}      #To extarct Verb Phrases
                       """)
  
# Print all parts of speech in above sentence
output = chunker.parse(tagged)
print("After Extracting\n", output)
output.draw()