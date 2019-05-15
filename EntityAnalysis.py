import spacy
from AbusedMail import Mail

# Load spaCy's English NLP model
nlp = spacy.load('en_core_web_lg')


def print_token_info(token):
    text = token.text if token.text is not None else ""
    pos = spacy.explain(token.pos_) if token.pos_ is not None else ""
    dep = spacy.explain(token.dep_) if token.dep_ is not None else ""
    lemma = token.lemma_ if token.lemma_ is not None else ""

    return text, pos, dep, lemma


class NLP_CORE:
    def __init__(self, text):
        self.document = nlp(text)

    def get_tokens(self):
        tokens = []
        for token in self.document:
            tokens.append(token.text)

        return tokens

    def print_significant_info(self):
        for token in self.document:
            text, pos, dep, lemma = print_token_info(token)
            print(f"{text}:{15} {pos}:{15} {dep}:{15} {lemma}:{15}")

    def print_named_entities(self):
        for ent in self.document.ents:
            print(f"{ent.text}:{15} {spacy.explain(ent.label_)}")


# Load abused mail
first_mail = Mail("1st_mail")

# The text we want to examine
text = first_mail.get_string()

abused = NLP_CORE("Quick brown fox jummped over lazy dog")
abused.print_significant_info()
