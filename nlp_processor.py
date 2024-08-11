import spacy

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
    
    def parse(self, text):
        doc = self.nlp(text)
        intent = None
        entities = {}
        for token in doc:
            if token.dep_ == 'ROOT':
                intent = token.lemma_
            elif token.ent_type_:
                entities[token.ent_type_] = token.text
        return intent, entities
