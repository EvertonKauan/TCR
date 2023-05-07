from funcoes import calculaM, calculaMzao, calculaMbarra, calculaInversos, calculaSomatorio_aMy, saoPrimosRelativos
import math

print("Teorema do Chinês -  FMCC II")
print('-' * 50)
qntd_equacoes = input('Qual a quantidade de equações? ')
qntd_equacoes_int = int(qntd_equacoes)

valores_de_m = []
valores_de_a = []
sao_positivos = True

# Inserindo os valores de 'a' e 'm'
for i in range(qntd_equacoes_int):
    print('-' * 50)
    print('\nSeja a equação do tipo x ≡ a (mod m)')
    print(f'Para a equação {i + 1}')
    a = int(input('Digite o valor de a: '))
    valores_de_a.append(a)
    m = int(input('Digite o valor de m: '))
    if m <= 1:
        sao_positivos = False
        break
    valores_de_m.append(m)

# Função para ver se são primos relativos
sao_primos_relativos = saoPrimosRelativos(valores_de_m)

if sao_primos_relativos and sao_positivos:
    # Calculando o valor de m = m1 * m2 * ... * mn
    m = calculaM(valores_de_m)
    # Listando os valores de Mn = m/mn
    lista_mzao = calculaMzao(valores_de_m, m)
    # Listando os valores de Mbarra = Mn / mn
    lista_m_barra = calculaMbarra(qntd_equacoes_int, lista_mzao, valores_de_m)
    # Calculado os inversos: Yn
    inversos = calculaInversos(qntd_equacoes_int, lista_m_barra, valores_de_m)
    # Somatório dos inversos
    somatorio_aMy = calculaSomatorio_aMy(qntd_equacoes_int, valores_de_a, lista_mzao, inversos)
    # Resultado do menor número
    resultado = somatorio_aMy % m

    print('-' * 50)
    print(f'\nLogo, {somatorio_aMy} ≡ {resultado} (mod {m})')
    print(f'N = {resultado} + {m} * n')
else:
    print('O Teorema se aplica apenas onde m1, m2 ... mn sejam inteiros positivos primos relativos maiores que 1.')
