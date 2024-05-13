from app import AutomatoDePilha

# Teste
automato = AutomatoDePilha()
# input_string = "x+y*z"
input_string = 'z*y+x-(z/x)'
result = automato.verificaGramatica(input_string)
print("A expressão é válida:", result)
