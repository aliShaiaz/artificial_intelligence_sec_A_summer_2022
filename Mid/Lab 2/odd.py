n = input("Please enter an integer: ")
sum = 0;
for i in range(1, 151):
  if i % 2 != 0:
    sum+=i

print("The sum is: ", sum)