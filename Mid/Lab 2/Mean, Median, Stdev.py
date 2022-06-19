from os import stat
import statistics

data = [4, 6, 8, 9, 9, 10, 23, 24, 25, 27]
#print(statistics.mean(data))
print("The mean value is: ", statistics.mean(data))
print("The median value is: ", statistics.median(data))
print("The standard deviation is: ", statistics.stdev(data))