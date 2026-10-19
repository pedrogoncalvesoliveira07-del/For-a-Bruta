import hashlib
import itertools
import string
import time

# Função que gera o hash de uma senha
def calcula_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


# Senha de teste criada para este projeto
senha_teste = "mar"
hash_teste = calcula_hash(senha_teste)

# Caracteres utilizados no experimento
caracteres = string.ascii_lowercase

print("Estudo de ataque de força bruta")
print("Testando combinações de uma senha fictícia...")
inicio = time.time()

# Testa combinações apenas para a senha de demonstração
for combinacao in itertools.product(
    caracteres, repeat=len(senha_teste)
):
    tentativa = "".join(combinacao)

    if calcula_hash(tentativa) == hash_teste:
        print("Senha de teste encontrada:", tentativa)
        break

fim = time.time()

print("Tempo de execução:", round(fim - inicio, 4), "segundos")
print("Experimento finalizado.")