from pathlib import Path
import sys

import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent))
from integrated_db import add_product, all_products, initialize


st.set_page_config(page_title="Produtos Integrados", page_icon="🧩", layout="wide")
initialize()
st.title("🧩 Aplicação Integrada de Produtos")
st.caption("SQLite + FastAPI + Streamlit")

with st.expander("Adicionar produto"):
    with st.form("add_product"):
        produto = st.text_input("Produto")
        categoria = st.text_input("Categoria")
        preco = st.number_input("Preço", min_value=0.0, step=0.01)
        quantidade = st.number_input("Itens vendidos", min_value=0, step=1)
        if st.form_submit_button("Salvar"):
            if produto.strip() and categoria.strip():
                add_product(produto.strip(), categoria.strip(), preco, quantidade)
                st.success("Produto salvo no SQLite.")
                st.rerun()
            st.error("Produto e categoria são obrigatórios.")

data = pd.DataFrame(all_products())
if data.empty:
    st.info("Cadastre o primeiro produto para visualizar os indicadores.")
else:
    col1, col2, col3 = st.columns(3)
    col1.metric("Produtos", len(data))
    col2.metric("Preço médio", f"R$ {data['preco'].mean():,.2f}")
    col3.metric("Itens vendidos", int(data["quantidade_vendida"].sum()))
    st.dataframe(data, use_container_width=True, hide_index=True)

