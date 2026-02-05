num=int(input("Enter a number"))
if num<0:
    print("Number Should be Greater Than Zero!")
else:
    temp = num
    order = len(str(num))
    result_sum=0
    while temp > 0:
        digit = temp % 10          
        result_sum += digit ** order 
        temp //= 10               
if num == result_sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is NOT an Armstrong number")

