# coding: utf-8

import spacy
from AbusedMail import Mail

# Load spaCy's English NLP model
nlp = spacy.load('en_core_web_lg')

# Load abused mail
first_mail = Mail("1st_mail")

# The text we want to examine
text = first_mail.get_string()

# Parse the text with spaCy
document = nlp(text)

# print out all the named entities that were detected
for entity in document.ents:
    print(entity.text, entity.label_)

# # Replace a specific entity with the word "PRIVATE"
# def replace_entity_with_placeholder(token):
#     if token.ent_iob != 0 and (token.ent_type_ == "PERSON" or token.ent_type_ == "ORG"):
#         return "[PRIVATE] "
#     else:
#         return token.string
#
#
# # Loop through all the entities in a piece of text and apply entity replacement
# def scrub(text):
#     doc = nlp(text)
#     for ent in doc.ents:
#         ent.merge()
#     tokens = map(replace_entity_with_placeholder, doc)
#     return "".join(tokens)
#
#
# print(scrub(text))
