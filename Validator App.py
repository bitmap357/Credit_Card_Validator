card_no = "5610591081018250"
odd_sum = 0
double_list = []
number = list(card_no)
for (idx, val) in enumerate(number):
    if idx % 2 != 0:
        odd_sum += int(val)
    else:
        double_list.append(int(val)*2)

# converting the list into a string
