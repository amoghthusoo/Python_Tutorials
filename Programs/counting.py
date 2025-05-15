l1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
l2 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
l3 = ['ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred']
num = int(input("Enter the number : "))
if (num >= 1 and num <= 9):
    print(l1[num - 1])
elif (num >= 11 and num <= 19):
    print(l2[num % 10 - 1])
elif (num % 10 == 0):
    print(l3[num // 10 - 1])
else:
    print(l3[int(str(num)[0]) - 1] + " " + l1[int(str(num)[1]) - 1])