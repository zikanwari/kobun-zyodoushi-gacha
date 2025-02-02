import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="助動詞ガチャ")

# タイトルと説明
st.title('助動詞ガチャ')

st.write('助動詞をランダムに表示します。')
st.write('エンドレステスト頑張りましょう！')

# Load the data
@st.cache
def load_data():
    return pd.read_excel("助動詞.xlsx")

words_df = load_data()

# ガチャ機能
if st.button('ガチャを引く！'):
    selected_word = words_df.sample().iloc[0]
    
    # セッションステートに選択された単語を保存
    st.session_state.selected_word = selected_word
    st.session_state.display_meaning = False

if 'selected_word' in st.session_state:
    st.header(f"単語名: {st.session_state.selected_word['単語名']}")

    # 意味を確認するボタンを追加
    if st.button('意味を確認する'):
        st.session_state.display_meaning = True

    if st.session_state.display_meaning:
        st.write(f"意味: {st.session_state.selected_word['意味']}")
