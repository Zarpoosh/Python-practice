class InfixToPostfix:
    def __init__(self):
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    
    def infix_to_postfix(self, expression):
        postfix = []
        stack = []
        
        for char in expression:
            if char.isalnum():
                postfix.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while stack and self.precedence.get(stack[-1], 0) >= self.precedence.get(char, 0):
                    postfix.append(stack.pop())
                stack.append(char)
        
        while stack:
            postfix.append(stack.pop())
        
        return ''.join(postfix)
    
    def evaluate_postfix(self, postfix_expression):
        stack = []
        
        for char in postfix_expression:
            if char.isalnum():
                stack.append(char)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = str(eval(operand1 + char + operand2))
                stack.append(result)
        
        return int(stack.pop())


infix_expression = input("Enter the infix expression: ")
infix_to_postfix_converter = InfixToPostfix()
postfix_expression = infix_to_postfix_converter.infix_to_postfix(infix_expression)
result = infix_to_postfix_converter.evaluate_postfix(postfix_expression)

print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)
print("Result:", result)