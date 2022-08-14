reversed_s = ''
s= 'reverse this string'
for i in range(len(s)-1, -1, -1):
 reversed_s += s[i] # 빈 문자열에 역을 거슬러서 하나씩 더하기


list_s = list(s)
for idx in range(len(s)//2):
  list_s[idx], list_s[-idx-1] = list_s[-idx-1], list_s[idx]
result = ''.join(list_s) # 앞에 하나와 뒤의 하나를 리스트상에서 교환환 뒤, 다시 문자열로 만들어주기
