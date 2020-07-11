words = input().split() # 단어들(key) 입력 받기
numbers = input().split() # 값 입력 받기

numbers = list(map(float, numbers)) # 값을 float 형의 리스트로 변환
results = dict(zip(words, numbers)) # Dic 생성

print(results)