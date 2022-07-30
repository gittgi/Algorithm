tc = int(input())
 
week_list = ['MON','TUE','WED','THU','FRI','SAT','SUN']
for i in range(tc):
    today = input()
    today_index = week_list.index(today)
    if 6 - today_index == 0:
        please_sunday = 7
    else:
        please_sunday = 6 - today_index
    print(f'#{i+1} {please_sunday}')