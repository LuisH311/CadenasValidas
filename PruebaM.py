import nltk
from nltk import CFG

grammar = CFG.fromstring("""
    S -> INTEGER OP INTEGER
    OP -> '+' | '-' | '*' | '/'
    INTEGER -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")

parser = nltk.ChartParser(grammar)

sentence = input("Ingrese la estructura a analizar: ")

sentence = sentence.replace(" ", "")

trees = list(parser.parse(sentence))

if len(trees) > 0:
    for tree in trees:
        print('branch:', tree)
        tree.pretty_print()
        tree.draw()
else:
    print('Cadena no válida')