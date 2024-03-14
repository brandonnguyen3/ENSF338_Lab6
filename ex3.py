'''
Exercise 3
'''
import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def shunting_yard(expression_tokens):
    output_queue = []
    operator_stack = []
    operators = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in expression_tokens:
        token = token.strip()
        if token.isdigit():
            output_queue.append(token)
        elif token in operators:
            while operator_stack and operator_stack[-1] in operators and (operators[operator_stack[-1]] >= operators[token]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue



def build_tree(postfix_tokens):
    stack = []

    for token in postfix_tokens:
        if token.isdigit():
            stack.append(Node(int(token)))
        elif token in {'+', '-', '*', '/'}:
            node = Node(token)
            if len(stack) < 2:
                print("Error: Insufficient operands for operator", token)
                sys.exit(1)
            node.right = stack.pop()
            if stack:
                node.left = stack.pop()
            stack.append(node)

    if len(stack) != 1:
        print("Error: Invalid expression")
        sys.exit(1)

    return stack.pop()


def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=' ')

def evaluate_tree(node):
    if isinstance(node.value, int):
        return node.value
    else:
        left_val = evaluate_tree(node.left)
        right_val = evaluate_tree(node.right)
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            return left_val / right_val

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex3.py 'expression'")
        sys.exit(1)

    expression = sys.argv[1]
    expression_tokens = expression.split()
    postfix_tokens = shunting_yard(expression_tokens)
    
    root = build_tree(postfix_tokens)
    print("Post-order traversal:")
    post_order_traversal(root)
    result = evaluate_tree(root)
    print("\nResult:", int(result))






