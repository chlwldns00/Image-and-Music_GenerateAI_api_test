import requests
import json
import io
import base64
from PIL import Image
import googletrans

# [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
REST_API_KEY = '${2ee17a13580700b2a0c01b457103a706}'

# 이미지 생성하기 요청
def t2i(text, batch_size=1):
    r = requests.post(
        'https://api.kakaobrain.com/v1/inference/karlo/t2i',
        json = {
            'prompt': {
                'text': text,
                'batch_size': batch_size
            }
        },
        headers = {
            'Authorization': f'KakaoAK2ee17a13580700b2a0c01b457103a706',
            'Content-Type': 'application/json'
        }
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    return response

# Base64 디코딩 및 변환
def stringToImage(base64_string, mode='RGBA'):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata)).convert(mode)
    return img

# 프롬프트에 사용할 제시어
text=input("AI로 생성할 이미지에대한 설명을 입력해주세요:")
translator=googletrans.Translator()
tex=translator.translate(text, dest='en',src='ko')
print(tex.text)

# 이미지 생성하기 REST API 호출
response = t2i(tex.text, 4)

#4번 루프를 돌면서 json 값중 이미지 배열에 있는 이미지값(저장되어있는 형태는 string) 을 이미지로 변환
for i in range(0,4):
    result = stringToImage(response.get("images")[i].get("image"), mode='RGB')
    print(result)
    result.show()


b=int(input("몇번째 사진으로 하시겠습니까?:"))
result = stringToImage(response.get("images")[b-1].get("image"), mode='RGB')
result.show()
