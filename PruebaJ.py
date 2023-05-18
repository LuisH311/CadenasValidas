import nltk

# Definir la gramática
grammar = nltk.CFG.fromstring("""
    statement -> switch variable cases otherwise END
    cases -> case value statement cases | case value statement | ε
    value -> INTEGER
    variable -> LETTER LETTER_DIGIT_UNDERSCORE*
    expression -> term | term '+' expression | term '-' expression
    term -> factor | factor '*' term | factor '/' term
    factor -> variable | constant | '(' expression ')'
    constant -> INTEGER | DECIMAL
    LETTER -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z'
    INTEGER -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    DECIMAL -> INTEGER '.' INTEGER
    LETTER_DIGIT_UNDERSCORE -> LETTER | INTEGER | '_'
""")

# Crear el objeto de análisis sintáctico
parser = nltk.ChartParser(grammar)


def parse_input(input_string):
    tokens = input_string.split()
    try:
        for tree in parser.parse(tokens):
            print('Cadena válida.')
            print(tree)
            tree.pretty_print()
        return True
    except Exception:
        print('Cadena no válida.')
        return False


# Llamar a la función parse_input() con la cadena de entrada
input_string = "..."  # Coloca aquí tu cadena de entrada
parse_input(input_string)