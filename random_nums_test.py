from random_nums import get_random_num
  
def main():
#check for uniform distribution
    random_values = []
    distribution = {}
    number_limit = 100
    for i in range(number_limit):
        distribution[i] = 0
    for i in range(number_limit*1000):
        num = get_random_num(number_limit)
        random_values.append(num)
        distribution[num] += 1
    print("Random values:")
    print(random_values)
    print("Distribution:")
    print(distribution)
#Calculate median
    sorted_random_values = random_values.copy()
    sorted_random_values.sort()
    print("Median: ")
    middle = len(random_values)//2
    print((sorted_random_values[middle] + sorted_random_values[middle+1])/2)


#Calculate mean
    mean_sum = 0
    for i in range(len(random_values)):
        mean_sum += random_values[i]
        mean = mean_sum/(len(random_values))
    print("Mean: ")
    print(mean)

#Calculate variance and standard deviation
    squared_difference_total = 0
    squared_difference = 0
    variance = 0
    for i in range(len(random_values)):
        squared_difference = random_values[i] - mean
        squared_difference = squared_difference ** 2
        squared_difference_total += squared_difference
    variance = squared_difference_total/(len(random_values))
    std_deviation = variance ** 0.5
    print("Variance: ")
    print(variance)
    print("Standard deviation: ")
    print(std_deviation)

#Runs test
    ascending_runs = 0
    descending_runs = 0
    ascending = False
    descending = False
    last_val = random_values[0]
    for i in range(1,len(random_values)):
        current_val = random_values[i]
        if(current_val >= last_val):
            ascending = True
            if(descending):
                descending_runs +=1
                descending = False
        elif(current_val < last_val):
            descending = True
            if(ascending):
                ascending_runs +=1
                ascending = False
        last_val = current_val
    print("Ascending runs: ")
    print(ascending_runs)
    print("Descending runs: ")
    print(descending_runs)
main()

