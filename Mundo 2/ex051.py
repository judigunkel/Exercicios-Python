"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final
mostre os 10 primeiros termos dessa progressão.
"""
print('=' * 26)
print('   10 TERMOS DE UMA PA   ')
print('=' * 26)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for n in range(primeiro, decimo + razao, razao):
    print(n, ' -> ', end=' ')
print('ACABOU!')

