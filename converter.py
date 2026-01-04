import pandas as pd
import json

# Ler o Excel
df = pd.read_excel("produtos.xlsx")

# Renomear colunas para combinar com o HTML
df = df.rename(columns={
    "Título": "nome",     # nome do produto
    "Tamanho": "tamanho",   # tamanho
    "Gênero": "genero",     # gênero
    "Imagem": "imagem",     # imagem
    "Preço": "preco"        # preço
})

# Criar uma coluna "meta" combinando tamanho e gênero
df["meta"] = df["tamanho"].astype(str) + " | " + df["genero"].astype(str)

# Converter para lista de dicionários
produtos = df.to_dict(orient="records")

# Salvar em JSON
with open("produtos.json", "w", encoding="utf-8") as f:
    json.dump(produtos, f, ensure_ascii=False, indent=2)

print("✅ produtos.json gerado com sucesso!")
