
number = input('please inter your number or q to quite: ')
step = 1

def happy_number():
    while step < 1000:
        if number == 'q':
            print('good bye')
            break
        
        digit_list = [int(digit) for digit in number]
        digit_sum = sum([i**2 for i in digit_list])
        if digit_sum == 1:
            print(f'{number} is happy number')
            break
        else:
            step =+ 1
            digit_list = str(digit_sum)
            continue
        
if __name__ == '__main__':
    happy_number()