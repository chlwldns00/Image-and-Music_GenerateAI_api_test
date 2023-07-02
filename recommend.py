import openai
import os

# OpenAI API 키 설정
openai.api_key = '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'

def recommend_music(genre, mood):
    # API 요청 구성
    prompt = f"I want a music recommendation in the {genre} genre with a {mood} mood."
    max_tokens = 100  # 추천 음악의 최대 길이 설정

    # API 호출
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=max_tokens,
        n = 1,  # 추천 음악 개수
        stop=None,  # 응답 중지 토큰 설정
        temperature=0.6  # 다양성 조절을 위한 온도 설정
    )

    # 추천된 음악 출력
    music_recommendation = response.choices[0].text.strip()
    print(response.choices[0])
    print("Recommended Music:")
    print(music_recommendation)

# 예시 실행

recommend_music('jazz', 'bright')
