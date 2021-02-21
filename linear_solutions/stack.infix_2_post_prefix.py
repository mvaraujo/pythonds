from linear import Stack


def infix_2_postfix(expression):
    precedence = {
        "**": 4,
        "*": 3, "/": 3,
        "+": 2, "-": 2,
        "(": 1
    }

    op_stack = Stack()

    postfix_list = []

    for token in expression.split():
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()

            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while not op_stack.is_empty() and \
                    precedence[op_stack.peek()] >= precedence[token]:
                postfix_list.append(op_stack.pop())

            op_stack.push(token)

    postfix_list.extend(op_stack.items[::-1])

    return " ".join(postfix_list)


test = "A * B + C * D"
print(test, " -- ", infix_2_postfix(test))

test = "( A + B ) * C - ( D - E ) * ( F + G )"
print(test, " -- ", infix_2_postfix(test))

test = "5 * 3 ** ( 4 - 2 )"
print(test, " -- ", infix_2_postfix(test))
