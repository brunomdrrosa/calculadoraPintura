from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

comodo = Comodo(
    input('Qual a largura do cômodo em metros? '),
    input('Qual a profundidade do cômodo em metros? ')
)

print(
    "A área das paredes em m² é:",
    calc.calcular_area_paredes(
        comodo
    )
)

print(
    'A área do teto em m² é:',
    calc.calcular_area_teto(
        comodo
    )
)

print(
    'A litragem de tinta necessária é:',
    calc.calcular_litragem_necessaria()
)