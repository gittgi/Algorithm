num = int(input())
for i in range(num):
    pupil, student_idx = tuple(map(int, input().split()))
    student_total_score = []
    for j in range(pupil):
        result = list(map(int, input().split()))
        total = result[0] * 0.35 + result[1] * 0.45 + result[2] * 0.2
        student_total_score.append(total)
    
    target = student_total_score[student_idx - 1]
    ranking_list = sorted(student_total_score)
    for k in enumerate(ranking_list, start=1):
        if target == k[1]:
            if k[0] <= pupil/10 * 1:
                grade = 'D0'
            elif k[0] <= pupil/10 * 2:
                grade = 'C-'
            elif k[0] <= pupil/10 * 3:
                grade = 'C0'
            elif k[0] <= pupil/10 * 4:
                grade = 'C+'
            elif k[0] <= pupil/10 * 5:
                grade = 'B-'
            elif k[0] <= pupil/10 * 6:
                grade = 'B0'
            elif k[0] <= pupil/10 * 7:
                grade = 'B+'
            elif k[0] <= pupil/10 * 8:
                grade = 'A-'
            elif k[0] <= pupil/10 * 9:
                grade = 'A0'
            else:
                grade = 'A+'

        print(f'#{i + 1} {grade}')



