from typing import List

class AutomatoDePilha:
    def __init__(self):
        self.transitions = [
            ('S', ['S', '+', 'T']),
            ('S', ['S', '-', 'T']),
            ('S', ['S', '*', 'T']),
            ('S', ['S', '/', 'T']),
            ('S', ['T']),
            ('T', ['x']),
            ('T', ['y']),
            ('T', ['z']),
            ('T', ['(', 'S', ')']) 
        ]

        self.terminais = ['S', 'T']

    def verificaGramatica(self, input_string, stack : List[str] = ['S']) -> bool:
        con = True
        finalizado = False
        while con:

            if len(stack) > len(input_string):
                return False

            if not self.verificaFalso(stack, input_string):
                return False


            if stack[len(stack) - 1] in self.terminais:
                lastInStack = stack.pop()
                possible : List[List]= self.setPossibleTransitions(lastInStack)
                for i in possible:
                    stackTemp = stack.copy()
                    temp = i.copy()
                    temp.reverse()
                    stackTemp.extend(temp)
                    finalizado = self.verificaGramatica(input_string, stackTemp)
                    if finalizado:
                        return finalizado

            if not self.verificaFalso(stack, input_string):
                return False

            if input_string[0] == stack[len(stack) - 1]:
                stack.pop()
                input_string = input_string[1:]
            else:
                return False


            if len(stack) == 0 and len(input_string) == 0:
                return True

        return finalizado
    
    def setPossibleTransitions(self, input):
        temp = []
        for i in self.transitions:
            value = i[0]
            if value == input:
                temp.append(i[1])
        return temp
    
    def verificaFalso(self, stack, input):
        if len(stack) == 0 and len(input) != 0:
            return False
        return True
    
__all__ = ['AutomatoDePilha']