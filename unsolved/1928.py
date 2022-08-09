letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']


test_case = int(input())

for i in range(test_case):
    original_list = list((input()))
    encoded_list = []
    for j in original_list:
        encoded_list.append(str(letter_list.index(j)))
    new_encoded_list = list(''.join(encoded_list))
    binary_list = []
    for j in new_encoded_list:
        binary_list.append(bin(int(j))[2:].zfill(6))
    new_binary_list = list(''.join(binary_list))
    eight_digit_list = []
    for j in range(int(len(new_binary_list)/8)):
        eight_digit_list.append(new_binary_list[8 * j : 8*(j+1)])
    new_word = ''
    for j in eight_digit_list:
        new_number_list = []
        
        for k in range(len(j)):
            new_number_list.append(int(j[k]) * (2**(7-k)))
        new_word += chr(sum(new_number_list))

    print(new_word)
    
    
   

    


        
        

    

