import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> D N | N
    VP -> V | V NP
    D -> "the" | "a"
    N -> "she" | "city" | "car"
    V -> "saw" | "walked"
""")

grammarMath = nltk.CFG.fromstring("""
    S -> NP | VP
    NP -> SR N SR N | N SR N
    VP -> N MD N | SR N MD N
    SR -> '+' | '-'
    MD -> '*' | '/'
    N -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10'
    OP -> '+' | '-' | '*' | '/'
""")

parser = nltk.ChartParser(grammarMath)

sentence = input("Sentence: ").split()

valid_sentence = False
for tree in parser.parse(sentence):
    valid_sentence = True
    tree.pretty_print()
    tree.draw()

if not valid_sentence:
    print('Invalid sentence')