# TrabalhoLFA
Este é um trabalho da faculdade que fiz no 5° periodo para a matéria de Linguagens Formais e Automatos, onde nós deveriamos construir um automato que reconhece-se a gramática a seguir

```
V = { x, y, z, +, -, *, (, ) }
Σ = ( S, T )
P = {
  T -> x,
  T -> y,
  T -> z,
  S -> S + T,
  S -> S - T,
  S -> S * T,
  S -> S / T,
  T -> ( S ),
  S -> T
}
```

## Como utilizar
para se utilizar o projeto você deve realizar o import da classe AutomatoDePilha dentro do arquivo app/__init__ e utilizar o método verificaGramatica como mostrado a seguir e tambem no arquivo __main__

``` py
  from trabalhoLFA.app import AutomatoDePilha

  resultado: bool = AutomatoDePilha.verificaGramatica('z*y+x-(z/x)')
```
