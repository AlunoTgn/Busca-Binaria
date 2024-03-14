def busca_sequencial(vetor, chave):
  """
  Realiza a busca sequencial em uma lista.

  Parâmetros:
      vetor: A lista a ser pesquisada.
      chave: A chave a ser buscada.

  Retorno:
      O índice da chave na lista se encontrada, -1 caso contrário.
  """
  for i, elemento in enumerate(vetor):
    if elemento == chave:
      return i
  return -1


def busca_sequencial_otimizada(vetor, chave):
  """
  Realiza a busca sequencial otimizada em uma lista ordenada.

  Parâmetros:
      vetor: A lista ordenada a ser pesquisada.
      chave: A chave a ser buscada.

  Retorno:
      O índice da chave na lista se encontrada, -1 caso contrário.
  """
  for i, elemento in enumerate(vetor):
    if elemento == chave:
      return i
    elif elemento > chave:
      return -1
  return -1


def busca_binaria(vetor, chave):
  """
  Realiza a busca binária em uma lista ordenada.

  Parâmetros:
      vetor: A lista ordenada a ser pesquisada.
      chave: A chave a ser buscada.

  Retorno:
      O índice da chave na lista se encontrada, -1 caso contrário.
  """
  baixo = 0
  alto = len(vetor) - 1
  while baixo <= alto:
    meio = (baixo + alto) // 2
    if vetor[meio] == chave:
      return meio
    elif vetor[meio] < chave:
      baixo = meio + 1
    else:
      alto = meio - 1
  return -1


# Exemplo de uso (não incluso no código original C)
vetor = [10, 20, 30, 40, 50]
chave = 30

resultado_sequencial = busca_sequencial(vetor, chave)
resultado_sequencial_otimizada = busca_sequencial_otimizada(vetor.copy(), chave)  # Cria cópia para não modificar
resultado_binaria = busca_binaria(sorted(vetor.copy()), chave)  # Ordena e cria cópia para não modificar

print("Busca sequencial:", resultado_sequencial)
print("Busca sequencial otimizada:", resultado_sequencial_otimizada)
print("Busca binária:", resultado_binaria)