import pandas as pd # type: ignore
import json

# Ler o Excel
df = pd.read_excel("produtos.xlsx")

# Converter para lista de dicionários
produtos = df.to_dict(orient="records")

# Adicionar o caminho da pasta 'imagens' para cada produto
for produto in produtos:
    if "imagem" in produto:
        produto["imagem"] = f"imagens/{produto['imagem']}"

# Salvar em JSON
with open("produtos.json", "w", encoding="utf-8") as f:
    json.dump(produtos, f, ensure_ascii=False, indent=2)

print("✅ produtos.json gerado com sucesso!")

