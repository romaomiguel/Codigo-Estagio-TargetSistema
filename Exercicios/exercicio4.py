# Função para analisar a sequência aritmetica
def analisar_sequencia_aritmetica(sequencia):
    razao = sequencia[1] - sequencia[0]
    proximo_termo = sequencia[-1] + razao
    sequencia.append(proximo_termo)
    return sequencia

# Função para analisar a sequência geométrica
def analisar_sequencia_geometrica(sequencia):
    razao = sequencia[1] / sequencia[0]
    proximo_termo = sequencia[-1] * razao
    sequencia.append(proximo_termo)
    return sequencia

# Função que analisar a sequência dos números inteiros não negativos elevados ao quadrado
def analisar_sequencia_quadrado(sequencia):
    indice_proximo_termo = len(sequencia)
    proximo_termo = indice_proximo_termo ** 2
    sequencia.append(proximo_termo)
    return sequencia

# Função que analisar a sequência dos números pares elevados ao quadrado
def analisar_sequencia_pares_quadrados(sequencia):
    ultimo_numero = int(sequencia[-1] ** 0.5)
    proximo_numero_par = ultimo_numero + 2
    proximo_termo = proximo_numero_par ** 2
    sequencia.append(proximo_termo)
    return sequencia

# Função para analisar a sequência de Fibonacci
def analisar_sequencia_soma(sequencia):
    proximo_termo = sequencia[-1] + sequencia[-2]
    sequencia.append(proximo_termo)
    return sequencia

# Função para analisar a sequência com incremento de 1 em 1
def analisar_sequencia_incremento(sequencia):
    proximo_termo = sequencia[-1] + 1
    sequencia.append(proximo_termo)
    return sequencia

# Sequências fornecidas
sequencia_a = [1, 3, 5, 7]
sequencia_b = [2, 4, 8, 16, 32, 64]
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
sequencia_d = [4, 16, 36, 64]
sequencia_e = [1, 1, 2, 3, 5, 8]
sequencia_f = [2, 10, 12, 16, 17, 18, 19]

# Analisando as sequências
print("Letra A:", analisar_sequencia_aritmetica(sequencia_a))
print("Letra B:", analisar_sequencia_geometrica(sequencia_b))
print("Letra C:", analisar_sequencia_quadrado(sequencia_c))
print("Letra D:", analisar_sequencia_pares_quadrados(sequencia_d))
print("Letra E:", analisar_sequencia_soma(sequencia_e))
print("Letra F:", analisar_sequencia_incremento(sequencia_f))