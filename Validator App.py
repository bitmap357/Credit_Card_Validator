# card_no = "5610591081018250"
# Declarations
odd_sum = 0
even_sum = 0
double_list = []

# Checking card number
card_num = input("Please input your card number(There should be up to 16 digits):")
number = list(card_num)
for (idx, val) in enumerate(number):
    if idx % 2 != 0:
        odd_sum += int(val)
    else:
        double_list.append(int(val)*2)

# converting the list into a string
double_string = ""
for x in double_list:
    double_string += str(x)

# converting the string into a list
double_list = list(double_string)

# adding even numbers
for x in double_list:
    even_sum += int(x)

# Adding sum and validation
net_sum = odd_sum + even_sum
if net_sum % 10 == 0:
    print('This is a valid card')
else:
    print('Invalid card')
