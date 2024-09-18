nota1 = float(input('digite a primeira nota:'))
nota2 = float(input('digite a segunda nota:'))
nota3 = float(input('digite a terceira nota:'))

#calcular a madia aritmetica
media = (nota1 + nota2 + nota3) / 3

#verificar se o aluno esta aprovado ou reprovado 
if media >= 7.0:

   print('APROVADO')
else:
   print('REPROVADO')