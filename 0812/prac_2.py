def itoa(num):
  if num < 0: # 음수의 경우에는 양수로 취급해서 변환하고, 문자열 앞에 - 기호 붙이기
      new_num = num * (-1)
      new_str = '-' 
  else:
      new_num = num
      new_str = ''

  temp = []

  while True:
      if new_num // 10 == 0: # 마지막 자리까지 완료되면 break
          break
      else:
          temp.append(new_num % 10) # 1의자리부터 잘라서 리스트에 담아두기
          new_num = new_num // 10

  temp = temp[::-1] # 역순으로 배치하기

  for i in temp:
      new_str += chr(i + 48) # 아스키코드에서 찾아서 숫자 맞춰주기

  return(new_str)