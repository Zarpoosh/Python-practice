class ExpressionEvaluator:
    def __init__(self):
        self.operators = set(['+', '-', '*', '/', '(', ')', '^'])  # Collection of Operators
        self.priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # Dictionary having priorities of Operators
    
    def infix_to_postfix(self, expression):
        stack = []
        output = ''
    
        for character in expression:
            if character not in self.operators:
                output += character
            elif character == '(':
                stack.append('(')
            elif character == ')':
                while stack and stack[-1] != '(':
                    output += stack.pop()
                stack.pop()
            else:
                while stack and stack[-1] != '(' and self.priority.get(character, 0) <= self.priority.get(stack[-1], 0):
                    output += stack.pop()
                stack.append(character)
    
        while stack:
            output += stack.pop()
    
        return output
    
    def evaluate_postfix(self, postfix_expression):
        stack = []
    
        for character in postfix_expression:
            if character not in self.operators:
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
        
        result = stack.pop()  # Assign the final result here
    
        return result

# Usage
expression = input('Enter infix expression: ')
print('Infix notation:', expression)

evaluator = ExpressionEvaluator()
postfix_expression = evaluator.infix_to_postfix(expression)
print('Postfix notation:', postfix_expression)

result = evaluator.evaluate_postfix(postfix_expression)
print('Result:', result)