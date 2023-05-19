import re

variable_pattern = r'^[a-zA-Z][a-zA-Z0-9_]*$'
integer_pattern = r'^\d+$'
decimal_pattern = r'^\d+(\.\d+)?$'

sentence = input("Ingrese la estructura a analizar: ").replace(" ", "")

def is_variable(string):
    return re.match(variable_pattern, string) is not None

def is_integer(string):
    return re.match(integer_pattern, string) is not None

def is_decimal(string):
    return re.match(decimal_pattern, string) is not None

def is_valid_expression(string):
    tokens = re.findall(r'[a-zA-Z][a-zA-Z0-9_]*|\d+(\.\d+)?|[-+*/()]', string)

    for token in tokens:
        if not (is_variable(token) or is_integer(token) or is_decimal(token) or token in ['+', '-', '*', '/', '(', ')']):
            return False

    if any(token in ['+', '-', '*', '/'] for token in tokens[:1]):
        return False
    if any(token in ['+', '-', '*', '/'] for token in tokens[-1:]):
        return False
    if any(tokens[i] in ['+', '-', '*', '/'] and tokens[i + 1] in ['+', '-', '*', '/'] for i in range(len(tokens) - 1)):
        return False

    stack = []
    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            if not stack:
                return False
            stack.pop()
    if stack:
        return False

    return True

if is_variable(sentence):
    print('Variable válida')
elif is_integer(sentence):
    print('Constante entera válida')
elif is_decimal(sentence):
    print('Constante decimal válida')
elif is_valid_expression(sentence):
    print('Expresión aritmética válida')
else:
    print('Cadena no válida')