Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # Collection of Operators
Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # Dictionary having priorities of Operators

def infix_to_postfix(expression):
    stack = []
    output = ''

    for character in expression:
        if character not in Operators:
            output += character
        elif character == '(':
            stack.append('(')
        elif character == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and Priority.get(character, 0) <= Priority.get(stack[-1], 0):
                output += stack.pop()
            stack.append(character)

    while stack:
        output += stack.pop()

    return output

def evaluate_postfix(postfix_expression):
    stack = []

    for character in postfix_expression:
        if character not in Operators:
            stack.append(character)
        else:
            operand2 = float(stack.pop())
            operand1 = float(stack.pop())
            if character == '+':
                result = operand1 + operand2
            elif character == '-':
                result = operand1 - operand2
            elif character == '*':
                result = operand1 * operand2
            elif character == '/':
                result = operand1 / operand2
            stack.append(result)

    return stack.pop()

expression = input('Enter infix expression: ')
print('Infix notation:', expression)

postfix_expression = infix_to_postfix(expression)
print('Postfix notation:', postfix_expression)

result = evaluate_postfix(postfix_expression)
print('Result:', result)