
import nltk
from nltk.draw import TreeWidget


grammarMath = nltk.CFG.fromstring("""
    S -> 'F' 'U' 'N' 'C' 'T' 'I' 'O' 'N' ' ' NF '(' AR ')' 
    NF -> INF CSLNF | INF LT CSLNF FNF
    INF -> LT CNFL | '_' CNFG 
    CNFL -> N CNFN | '_' CNFG |
    CNFN -> LT CNFL | '_' CNFG | N CNFN |
    CNFG -> LT CNFL | N CNFN | 
    CSLNF -> LT CSLNF |
    FNF -> N CNFN | '_' CNFG 
    AR -> '(' CA ')' | '(' CA VAR ')'
    VAR -> ',' CA VAR |
    CA -> LT CAL | N CAN 
    CAL -> LT CAL | N CAN | '_' CAG |
    CAN -> LT CAL | '_' CAG |
    CAG -> LT CAL | N CAN |
    N -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' 
    LT -> min | may
    min -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' 
    may -> 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z' 
""")

parser = nltk.ChartParser(grammarMath)

sentence = input("Sentence: ")

valid_sentence = False
for tree in parser.parse(sentence):
    valid_sentence = True
    tree.pretty_print()
    tree.draw()

if not valid_sentence:
    print('Invalid sentence')