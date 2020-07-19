#a = [3, 1, 3, 2, 5]
#b = []

#for i in a:
#    line = []
#    for j in range(i):
#        line.append(0)
#    b.append(line)

#print(b)

#a = [[0] * i for i in [3, 1, 3, 2, 5]]

#print(a)



#students = [
#    ['john', 'C', 19],
#    ['maria', 'A', 25],
#    ['andrew', 'B', 7]
#]

#print(sorted(students, key=lambda student: student[1]))  # 안쪽 리스트의 인덱스 1을 기준으로 정렬
#print(sorted(students, key=lambda student: student[2]))  # 안쪽 리스트의 인덱스 2를 기준으로 정렬




a = [[10, 20], [30, 40]]
import copy
b = copy.deepcopy(a)
b[0][0] = 500
print(a)
print(b)


#높이 2, 세로 크기 4, 가로 크기 3인 3차원 리스트
c = []
c = [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
print(c)