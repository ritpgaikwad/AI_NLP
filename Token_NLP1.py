import spacy

nlp = spacy.load("en_core_web_sm")
txt = (
    "India is my country. "
    "I love India so much. "
)

doc = nlp(txt)

print("Tokenization")
for token in doc:
    print(token, token.idx)

print("Stop words removal")
print([token for token in doc if not token.is_stop])

print("Lemmatization")
print([token.lemma_ for token in doc])

print("Parts of Speech Tagging: ")
for token in doc:
    print(token.text, token.pos_)