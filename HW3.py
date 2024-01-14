# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.top == None

    def __len__(self): 
        # YOUR CODE STARTS HERE
        count = 0
        current = self.top
        # loop through stack
        while current:
            count += 1
            current = current.next

        return count

    def push(self,value):
        # YOUR CODE STARTS HERE
        newNode = Node(value)
        if self.__len__() == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

     
    def pop(self):
        # YOUR CODE STARTS HERE
        if len(self) == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            return temp.value

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.top:
            return self.top.value
        else:
            return None


#=============================================== Part II ==============================================

# helper function
def is_balanced(expr):
  '''
    Determines if an expression has balanced parentheses
    The parameters are:
    # expr -> str: an arithmetic expression
    Returns:
    # bool: True if expression is balanced, False otherwise
  '''
  s = Stack()
  is_open = {'(': 1, '[': 2, '{': 3,'<':4}
  is_close = {')': 1, ']': 2, '}': 3,'>':4}
  balanced = True
  size = len(expr)
  i = 0
  while balanced and i < size:
    current = expr[i]
    if current in is_open:
      s.push(current)
    elif current in is_close:
      if s.isEmpty():
        balanced = False
        # check if closing pair is correct
      else:
        top_parenthesis = s.pop()
        balanced = is_open[top_parenthesis] == is_close[current]
    i += 1
    # s.isEmpty() ensure every bracket has a pair
  return s.isEmpty() and balanced

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        if txt == "0" or txt == "0.0":
            return True
        try:
            return bool(float(txt))
        except:
            return False

    

    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack object for expression processing

            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix('( 2 { 5.0 } )')
            '2.0 5.0 *'
            >>> x._getPostfix(' 5 ( 2 + { 5 + 3.5 } )')
            '5.0 2.0 5.0 3.5 + + *'
            >>> x._getPostfix ('( { 2 } )')
            '2.0'
            >>> x._getPostfix ('2 * ( [ 5 + -3 ] ^ 2 + { 1 + 4 } )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('[ 2 * ( < 5 + 3 > ^ 2 + ( 1 + 4 ) ) ]')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( { 2 * { { 5 + 3 } ^ 2 + ( 1 + 4 ) } } )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * < -5 + 3 > ^ 2 + < 1 + 4 >')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ]')
            >>> x._getPostfix(' ( 2 * { 5 + 3 ) ^ 2 + ( 1 + 4 ] }')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
        '''

        # YOUR CODE STARTS HERE
        priority = {
            '^':3,
            '*':2,
            '/':2,
            '-':1,
            '+':1
        }
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        cleaned_txt = txt.split()
        open_brackets = ['<','(','{','[']
        close_brackets = ['>',')','}',']']
        outputList = []
        # check parantheses
        if not is_balanced(txt):
            return None
        # first and last character must not be operator
        if cleaned_txt[0] in priority or cleaned_txt[-1] in priority:
            return None
        try:
            for i in range(len(cleaned_txt)):
                if self._isNumber(cleaned_txt[i]):
                    # error: digit cannot be back to back
                    if i > 0 and self._isNumber(cleaned_txt[i-1]):
                        return None
                    outputList.append(str(float(cleaned_txt[i])))
                elif cleaned_txt[i] in open_brackets :
                    # for a(b) or (a)(b), push *
                    if i > 0 and self._isNumber(cleaned_txt[i-1]) or (i > 0 and cleaned_txt[i-1] in close_brackets):
                        postfixStack.push('*')
                    postfixStack.push(cleaned_txt[i])
                elif cleaned_txt[i] in close_brackets:
                    while len(postfixStack) > 0 and postfixStack.peek() not in open_brackets:
                        # take every operator out until open bracket is found
                        outputList.append(postfixStack.pop())
                    postfixStack.pop()
                # ^ has right associative. 
                elif postfixStack.peek() == "^" and cleaned_txt[i] == "^":
                        postfixStack.push(cleaned_txt[i])
                else:
                    # error: if operator back to back
                    if i > 0 and cleaned_txt[i-1] in priority:
                        return None
                    
                    # take every operator out until open bracket is found
                    while len(postfixStack) > 0 and postfixStack.peek() not in open_brackets and priority[postfixStack.peek()] >= priority[cleaned_txt[i]]:
                        outputList.append(postfixStack.pop())
                    postfixStack.push(cleaned_txt[i])

            while len(postfixStack) > 0:
                outputList.append(postfixStack.pop())

            return " ".join(outputList)
        except:
            return "None"
        

    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack object to compute the final result as shown in the video lectures
            

            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( [ ( 10 - 2 * 3 ) ] )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * { 3 - 2.45 * [ 4 - 2 ^ 3 ] } + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * [ 4 + 2 * < 5 - 3 ^ 2 > + 1 ] + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + { 3.0 } * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * < 4 > ) * [ 2 / 8 + 2 * ( 3 - 1 / 3 ) ] - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            >>> x.setExpr('( 3.5 ) [ 15 ]') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 { 5 } - 15 + 85 [ 12 ]') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 { ( 9.4 ) } )") 
            >>> x.calculate
            46.666666666666664
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( ( 2 ) * 10 - 3 * [ 2 - 3 * 2 ) ]')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        # YOUR CODE STARTS HERE
        postFixExp = self._getPostfix(self.getExpr)
        if not postFixExp:
            return None
        else:
            postFixExp = postFixExp.split()
            for i in postFixExp:
                if self._isNumber(i):
                    calcStack.push((float(i)))
                else:
                    operand1 = calcStack.pop()
                    operand2 = calcStack.pop()
                    if i == "+":
                        result = operand2 + operand1
                        calcStack.push(result)
                    elif i == "-":
                        result = operand2 - operand1
                        calcStack.push(result)
                    elif i == "*":
                        result = operand2 * operand1
                        calcStack.push(result)
                    elif i == "^":
                        result = operand2 ** operand1
                        calcStack.push(result)
                    else:
                        result = operand2 / operand1
                        calcStack.push(result)
                
            return calcStack.pop()




#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 [ x1 - 1 ];x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * { x1 / 2 };x1 = x2 * 7 / x1;return x1 ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * { x1 / 2 }': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        # variable is valid if not empty string, first letter is letter and only contains letter and number
        return word and word[0].isalpha() and word.isalnum() 
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 ( x1 - 1 )')
            '7 ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        exprList = expr.split()
        expValid = True
        for i in range(len(exprList)):
            if self._isVariable(exprList[i]):
                if exprList[i] in self.states:
                    exprList[i] = str(self.states[exprList[i]])
                else:
                    expValid = False
        if expValid:
            return " ".join(exprList)
    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        # dictionary to be displayed
        processing = {}
        exp = self.expressions.split(';')
        for i in exp:
            if i.split()[0] == "return":
                # slice everything after "return"
                mathExp = " ".join(i.split()[1:])
                cleaned_exp = self._replaceVariables(mathExp)
                calcObj.setExpr(cleaned_exp)
                processing["_return_"] = calcObj.calculate
            else:   
                # slice everything after "="
                mathExp = i.split("=")[1].strip()
                cleaned_exp = self._replaceVariables(mathExp)
                calcObj.setExpr(cleaned_exp)
                # store current states in temporary variable
                copy_state = self.states.copy()
                # get the key
                var = i.split('=')[0].strip()
                if not self._isVariable(var):
                    self.states = {}
                    return None
                copy_state[var] = calcObj.calculate
                processing[i] = copy_state 
                # update state
                self.states = copy_state
                
        return processing




def run_tests():
    import doctest

    #- Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    #- Run tests per class - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    # doctest.run_docstring_examples(Calculator, globals(), name='HW3',verbose=True)   

if __name__ == "__main__":
    run_tests()