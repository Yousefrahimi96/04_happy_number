
def happy_number():
    number = input('inter your number: ')
    seen_number = []
    
    while (number != 1) and (number not in seen_number):
        seen_number.append(number)
        number = sum([int(digit)**2 for digit in str(number)])
        
    if number == 1:
        print('is happy number')
    else:
        print('is not happy number')

if __name__ == '__main__':
    happy_number()