# coding=utf-8
# stack
from sys import argv
from decimal import *

class Stack(object):
    def __init__(self,limit):
        self.stack=[]
        self.limit=limit  # 设置栈的最大容量

    def stack_length(self):
        return len(self.stack)

    def is_empty(self):
        return self.stack_length() == 0

    def get_top(self):
        return self.stack[-1]

    def push(self,item):
        if self.stack_length() >= self.limit:
            raise StackOverflowError
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')

    def clearstack(self):
        self.stack = []


class StackOverflowError(BaseException):
    pass
# s=Stack()
# s.stack=[1,2,3]
# print(s.stack_length(),s.is_empty())
# s.pop()
# s.pop()
# s.pop()
# print(s.stack)
# s.push(4)
# s.push(5)


# 括号匹配的检验
def balanced_parentheses(parentheses):
    """ Use a stack to check if a string of parentheses is balanced."""
    print(parentheses)
    stack = Stack(len(parentheses))
    for parenthesis in parentheses:
        print(parenthesis)
        if parenthesis == '(' or parentheses == '[':
            stack.push(parenthesis)
        elif parenthesis == ')' or parentheses == ']':
            if stack.is_empty():
                return False
            stack.pop()
        print(stack.stack)
    return stack.is_empty()
# if __name__ == '__main__':
#     # examples = ['((()))', '((())', '(()))', '[([][))]']
#     examples=['[([][))]']
#     # print('Balanced parentheses demonstration:\n')
#     for example in examples:
#         print(example + ': ' + str(balanced_parentheses(example)))

# 表达式求值，中缀表达式转换为后缀表达式求值
def delBlank(str):
    """
    Delete all blanks in the str
    """
    ans = ""
    for e in str:
        if e != " ":
            ans += e
    return ans

def precede(a, b):
    # 比较栈顶运算符a和当前运算符b的优先级
    """
    Compare the prior of operator a and b
    """
    # the prior of operator 优先级
    prior = (
        #   '+'  '-'  '*'  '/'  '('  ')'  '^'  '#'
           ('>', '>', '<', '<', '<', '>', '<', '>'),  # '+'
           ('>', '>', '<', '<', '<', '>', '<', '>'),  # '-'
           ('>', '>', '>', '>', '<', '>', '<', '>'),  # '*'
           ('>', '>', '>', '>', '<', '>', '<', '>'),  # '/'
           ('<', '<', '<', '<', '<', '=', '<', ' '),  # '('
           ('>', '>', '>', '>', ' ', '>', '>', '>'),  # ')'
           ('>', '>', '>', '>', '<', '>', '>', '>'),  # '^'
           ('<', '<', '<', '<', '<', ' ', '<', '=')   # '#'
        )

    # operator to index of prior[8][8]
    char2num = {
        '+': 0,
        '-': 1,
        '*': 2,
        '/': 3,
        '(': 4,
        ')': 5,
        '^': 6,
        '#': 7
        }

    return prior[char2num[a]][char2num[b]]

def operate(a, b, operator):
    """
    Operate [a operator b]
    """
    if operator == '+':
        ans = a + b
    elif operator == '-':
        ans = a - b
    elif operator == '*':
        ans = a * b
    elif operator == '/':
        if b == 0:
            ans = "VALUE ERROR"
        else:
            ans = a / b
    elif operator == '^':
        if a == 0 and b == 0:
            ans = "VALUE ERROR"
        else:
            ans = a ** b

    return ans

def calc(exp):
    """
    Calculate the ans of exp
    """
    exp += '#'
    operSet = "+-*/^()#"
    stackOfOperator, stackOfNum = ['#'], []  # 运算符栈和操作数栈
    pos, ans, index, length = 0, 0, 0, len(exp)
    while index < length:
        e = exp[index]
        if e in operSet:
            # calc according to the prior
            topOperator = stackOfOperator.pop()
            compare = precede(topOperator, e)
            if compare == '>':
                try:
                    b = stackOfNum.pop()
                    a = stackOfNum.pop()
                except:
                    return "FORMAT ERROR"
                ans = operate(a, b, topOperator)
                if ans == "VALUE ERROR":
                    return ans
                else:
                    stackOfNum.append(ans)
            elif compare == '<':
                stackOfOperator.append(topOperator)
                stackOfOperator.append(e)
                index += 1

            elif compare == '=':
                index += 1
            elif compare == ' ':
                return "FORMAT ERROR"
        else:
            # get the next num
            pos = index
            while not exp[index] in operSet:
                index += 1
            temp = exp[pos:index]

            # delete all 0 of float in the end
            last = index - 1
            if '.' in temp:
                while exp[last] == '0':
                    last -= 1
                temp = exp[pos:last + 1]

            try:
                temp = Decimal(temp)
            except:
                return "INPUT ERROR"
            stackOfNum.append(temp)

    if len(stackOfNum) == 1 and stackOfOperator == []:
        return stackOfNum.pop()
    else:
        return "INPUT ERROR"

if __name__ == "__main__":
    # get the exp
    exp = argv[1]

    # set the precision
    getcontext().prec = 10

    # delete blanks
    exp = delBlank(exp)

    # calc and print the ans
    ans = calc(exp)
    print(ans)
