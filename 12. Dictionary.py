lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
print(lux1) # 키=값 형식으로 딕셔너리 만듦

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], 
[490, 334, 550, 18.72])) 
print(lux2) #키 리스트와 값 리스트를 묶음

lux3 = dict([('health', 490), ('mana', 334), ('melee', 550),
('armor', 18.72)])
print(lux3) # (키, 값) 형식의 튜플로 딕셔너리를 만듦

print(lux3['health']) # Dic key에 접근하기

lux3['health'] = 2037 # Dic 값 할당
lux3['mana_ragen'] = 3.28 # Dic 없는 키에 값 할당
print(lux3) 

print('health' in lux3) # Dic에 특정 키 있는지 확인
print('health' not in lux3) # 특정 값 없는지 확인

print(len(lux3)) # 길이 = key의 갯수 구하기