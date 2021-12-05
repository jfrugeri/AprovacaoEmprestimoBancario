'''
------------ AUTORIZAÇÃO DE EMPRESTIMO -----------------------

A autorização de emprestimo só é liberada caso
o valor pago mensalmente seja menor que 30% do salario da pessoa.

'''

nome = str(input('Ola, qual o seu nome? '))
salario = float(input('{} qual é o seu salário bruto? '.format(nome)))
vlimovel = float(input('{} agora me diz o valor do imóvel que você deseja comprar '.format(nome)))
anos = int(input('Beleza, {}. Em quantos anos você deseja concluir o pagamento? '.format(nome)))

prestacao = vlimovel / (12 * anos)

trinta100 = salario * 0.30


if prestacao > trinta100:
    print('{}- EMPRÉSTIMO NÃO AUTORIZADO{} {}. Pois R${:.2f} é maior que 30% do seu salário.'.format('\033[1;31m','\033[m', nome, prestacao))
else:
    print('{}- EMPRÉSTIMO AUTORIZADO{} {}. {}Parcelas de R${:.2f} em {} Meses.{}'.format('\033[1;32m', '\033[m', nome,'\033[1;32m', prestacao, (12*anos),'\033[m'))
