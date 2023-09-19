import streamlit as st
from PIL import Image
import datetime

st.title("アプリだよ")
st.caption("これはアプリだよ！")
st.subheader("自己紹介")
st.text("よろしくお願いします")
code = '''
include<stdio.h>
int main(){
	int x = 0;
	printf("%d", x);
	return 0;
}
'''
st.code(code, language='c')

# 画像
image = Image.open("card_joker.png")
st.image(image, width=200)

with st.form(key='profile_form') :
	# テキストボックス
	name = st.text_input('名前')
	print(name)

	# セレクトボックス
	age_category = st.selectbox("年齢層", ("子ども", "大人"))

	# ラジオボタン
	age_category = st.radio("年齢層", ("子ども", "大人"))
	
	# 複数選択
	hobby = st.multiselect("趣味", ("スポーツ", "読書", "アニメ", "釣り"))

	# チェックボックス
	st.checkbox("メールマガジンを購読する")

	# スライダー
	height = st.slider('身長', min_value = 110, max_value = 210)

	# 日付
	start_date = st.date_input("開始日", datetime.date(2023, 9, 19))

	# カラーピッカー
	color = st.color_picker("テーマカラー", "#FFFFFF")

	# ボタン
	submit_btn = st.form_submit_button('送信')
	if submit_btn == True:
		st.text('ようこそ！' + name + "さん")