import os
import openai
import googletrans
import webbrowser
openai.api_key = "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"
text=input("AI로 생성할 이미지에대한 설명을 입력해주세요:")
translator=googletrans.Translator()
tex=translator.translate(text, dest='en',src='ko')
print(tex.text)
k=int(input("몇장을 예시로 생성할까요?:"))
images = openai.Image.create(
  prompt=tex.text,
  n=k,
  size="1024x1024"
)

for i in range(0,k):
    u=images.data[i].url
    webbrowser.open(u)


p=int(input("몇번쨰 사진을 선택할까요?:"))
u=images.data[p-1].url
webbrowser.open(u)


