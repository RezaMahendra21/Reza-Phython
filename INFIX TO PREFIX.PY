class Stack:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def peek(self):
         return self.items[len(self.items)-1]
     def size(self):
         return len(self.items)
     def showList(self):
          return self.items
# No 1
def infixToPrefix(infixexpr):
    
    prec = {'*':3, '/':3 , '+':2, '-':2 , '(':1}
    opStack = Stack()
    prefixList = []
    tokenList = infixexpr.split()
    tokenList.reverse()
    for i in range(len(tokenList)):
         if tokenList[i] == '(':
              tokenList[i]=')'
         elif tokenList[i] == ')':
              tokenList[i]='('
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            prefixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            
            while topToken != '(':
                prefixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  prefixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        prefixList.append(opStack.pop())
    prefixList = prefixList[::-1]
    return " ".join(prefixList)

print('No 1')
print(infixToPrefix("A * B - C * D"))
print(infixToPrefix("( A + B ) * C - ( D - E ) * ( F + G )"))