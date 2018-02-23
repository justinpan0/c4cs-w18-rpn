#!/usr/bin/env python3
import operator

ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv
        }

def eval_arg(tokens, stack):
    for token in tokens:
        if set(token).issubset(set("0123456789.")):
            stack.append(int(token))
        elif token in ops:
            if len(stack) < 2:
                raise ValueError('Less than two parameters')
            x = stack.pop()
            y = stack.pop()
            op = ops[token]
            stack.append(op(y, x))
        else:
            raise ValueError('Unrecognizable symbol: %s' % token)
    return stack[0]

def calculate(arg):
    stack = []
    if arg in ['quit', 'q', 'exit']:
        exit();
    elif len(arg) != 0:
        return eval_arg(arg.split(), stack)

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()
