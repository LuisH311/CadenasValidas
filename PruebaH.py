import nltk
from nltk import CFG


# Definir la gramática
grammarMath = CFG.fromstring("""
    S -> FUNCTION ' ' NF '(' VAR ')'
    NF -> INF CSLNF | INF LT CSLNF FNF
    INF -> LT CNFL | '_' CNFG 
    CNFL -> N CNFN | '_' CNFG |
    CNFN -> LT CNFL | '_' CNFG | N CNFN |
    CNFG -> LT CNFL | N CNFN | 
    CSLNF -> LT CSLNF |
    FNF -> N CNFN | '_' CNFG 
    VAR -> CA VAR | '(' CA VAR ')' |
    CA -> LT CAL | N CAN 
    CAL -> LT CAL | N CAN | '_' CAG |
    CAN -> LT CAL | '_' CAG |
    CAG -> LT CAL | N CAN |
    N -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' 
    LT -> "min" | "may"
    FUNCTION -> 'FUNCTION'
    min -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' 
    may -> 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z' 
""")

parser = nltk.ChartParser(grammarMath)

sentence = "FUNCTION Reset_02(num,cod2)"

# Dividir la oración en palabras
words = sentence.split()

# Intentar analizar la oración
try:
    for tree in parser.parse(words):
        print(tree)
        tree.pretty_print()
        tree.draw()
    print("La cadena es válida.")

except ValueError as e:
    print("La cadena no es válida:", str(e))