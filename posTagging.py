import spacy
import codecs

fname = input("Enter the location of the text file :")
fn = open(fname, "a")
f = codecs.open(fname, 'r')

nlp = spacy.load("en_core_web_sm")

doc = nlp(f.read())
#print(doc)

print("--------------------------------****---------------------------")
for token in doc:
    print(f'{token.text:{20}} {token.pos_}')