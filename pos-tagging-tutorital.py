import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
# Add match ID "HelloWorld" with no callback and one pattern
pattern = [{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}]
pattern1 = [{"POS":"NOUN"}, {"POS":"ADP"}]
matcher.add("HelloWorld", None, pattern)
matcher.add("p1",None,pattern1)

doc = nlp("Hello, world! Hello world! The chemical was spilled on I-696 on purpose by an evil wizard officials stated.")
matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)
