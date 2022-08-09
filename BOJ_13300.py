import sys
sys.stdin = open('input.txt', 'r')

pupil, per_room = tuple(map(int, input().split()))

student_list = []
for i in range(pupil):
    student_info = tuple(map(int, input().split()))
    student_list.append(student_info)               # [성별, 학년] 형태로 리스트에 저장
girls = [0,0,0,0,0,0]                               # 1학년부터 6학년까지 카운트
boys = [0,0,0,0,0,0]                                # 1학년부터 6학년까지 카운트
for i in student_list:
    if i[0] == 0:
        girls[i[1] - 1] += 1                        # 각 학년 인덱스에 맞게 숫자세기
    else:
        boys[i[1] - 1] += 1                         # 각 학년 인덱스에 맞게 숫자세기


room = 0
for i in girls:
    if i % per_room != 0:
        room += ((i // per_room) + 1)               # 정해진 방 제한 인원 수 대로 학년별 인원이 나누어 떨어지지 않으면 나머지끼리 방 하나 더
    else:
        if i != 0:
            room += (i // per_room)                 # 나누어 떨어질 때, 학생 수가 아예 없는 게 아니라면, 나누어 떨어지는 만큼 방 부여

for i in boys: # 남자도 동일
    if i % per_room != 0:
        room += ((i // per_room) + 1)
    else:
        if i != 0:
            room += (i // per_room)

print(room)

