import streamlit as st
from random import randint
#from PIL import Image

st.title("ガチャシミュレーションアプリだよ")
st.caption("10連ガチャが引けるよ！")

prob = [87, 10, 3]
#prob = [7, 2, 1]#
sum_prob = sum(prob)

# 画像
#image_money = Image.open("card_joker.png")
#st.image(image, width=200)
#image = Image.open("card_joker.png")
#st.image(image, width=200)
#image = Image.open("card_joker.png")
#st.image(image, width=200)

with st.form(key='gacha') :
	# ボタン
	gacha_btn = st.form_submit_button('ガチャを引く')
	if gacha_btn == True:
		st.text('ガチャを引きます')
		for i in range(10):
			value = randint(1, sum_prob)
			rare = 1
			sum_p = 0
			for p in prob:
			#for p in range(len(prob)):#
				sum_p += p
				if value <= sum_p:
					st.text("レア度" + ("☆" * rare) + "を引いた！")
					#prob[p] = prob - 1#
					#sum_prob = sum(prob)#
					break;
				rare += 1