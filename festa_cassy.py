# ================================================
# PROGRAMA DA FESTA PRONTO - Cassy e amigos
# ================================================

# Cassy dança
cassy_dancando = True
print("Cassy está pronta para dançar! 💃\n")

# Lista de pessoas e seus passos de dança (pré-definidos)
pessoas_na_festa = ["Alice", "Bob", "Carlos", "Diana", "Eva"]
passos = {
    "Alice": "samba",
    "Bob": "rock",
    "Carlos": "hip hop",
    "Diana": "freestyle",
    "Eva": "forró"
}

print("--- A FESTA COMEÇA! ---\n")

# Cassy dançando
if cassy_dancando:
    print("Cassy está dançando moonwalk e contagiando a todos!\n")

# Cada pessoa na festa com seu próprio passo de dança
for pessoa in pessoas_na_festa:
    print(f"{pessoa} está dançando {passos[pessoa]}!")

# Condições divertidas
if "Alice" in pessoas_na_festa and cassy_dancando:
    print("\nAlice está seguindo o ritmo da Cassy!")

if len(pessoas_na_festa) > 3:
    print("\nA festa está cheia! Cassy faz uma coreografia especial para animar todo mundo!")

# Final divertido
print("\nA festa continua! Todo mundo dançando e se divertindo! 🎉🕺💃")
