import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter a text: ")

doc = nlp(text)

def getCommands(doc):
    command = []

    for token in doc:
        print(token, token.dep_, token.pos_)
        if token.dep_ in ("ROOT", "conj") and token.pos_ in ("VERB", "ADJ"):
            command.append(token.text)
    return command

def getEntities(doc):
    entities = {}
    
    for ent in doc.ents:
        # print(ent.text, ent.label_)
        
        if ent.label_ not in entities:
            entities[ent.label_] = []
        
        entities[ent.label_].append(ent.text)
    
    return entities

command = getCommands(doc)
entities = getEntities(doc)


print({
    "command": command,
    "entities": entities
})



# Mail John and James about the meeting tomorrow from Google mail