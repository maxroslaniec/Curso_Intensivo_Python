# Cria a lista de convidados
convidados = ["Emily", "Mia", "Vo Nara"]

# Envia a mensagem para o primeiro convidado
print("Ola " + convidados[0].title() + ", quer jantar comigo essa noite? \n")

# Envia a mensagem para o segundo convidado
print("Ola " + convidados[1].title() + ", quer jantar comigo essa noite? \n")

# Envia a mensagem para o terceiro convidado
print("Ola " + convidados[2].title() + ", quer jantar comigo essa noite? \n")

# Remove o primeiro convidado da lista
convidados_ausentes = convidados.pop(0)

# Informa que o primeiro convidado não poderá comparecer
print("O convidado: " + convidados_ausentes.title() + ", nao podera comparecer. \n")

# Informa que os outros convidados confirmaram presença
print("Os convidados: " + ", ".join(convidados) + ", confirmaram presença. \n")

# Adiciona um novo convidado na primeira posição da lista
convidados.insert(0, "Juju")

# Envia a mensagem para o novo convidado
print("Ola " + convidados[0].title() + ", quer jantar comigo essa noite? \n")

# Informa que uma mesa maior foi encontrada e que três novos convidados serão adicionados
print("Ola, encontramos um mesa maior e vamos adicionar 3 novos convidados ao nosso jantar. \n")

# Adiciona o novo convidado "Catia" na primeira posição da lista
convidados.insert(0, "Catia")

# Adiciona o novo convidado "Luciana" na terceira posição da lista
convidados.insert(2, "Luciana")

# Adiciona o novo convidado "Antonio" no final da lista
convidados.append("Antonio")

# Imprime a lista de convidados separando os itens por vírgula
print(", ".join(convidados) + "\n")

# Envia a mensagem para todos os convidados
for convidado in convidados:
    print("Olá, " + convidado + "! Gostaria de jantar comigo? \n")

# Informa que a mesa será reduzida para apenas 4 convidados
print("Teremos que reduzir a nossa mesa para apenas 4 convidados. \n")

# Percorre a lista de convidados e remove os quatro últimos da lista
for i in range(4):
  convidado = convidados.pop()
  print("Ola " + convidado + ", sinto muito por ter cancelado o convite. \n")

# Envia a mensagem para os convidados restantes
for i in convidados:
    print("Ola " + i + ", sua reservada esta confirmada! \n")

# Remove todos os elementos da lista
del convidados[:]

# Imprime a lista de convidados
print(convidados)



