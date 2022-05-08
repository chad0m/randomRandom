from random_nums import get_random_num
  
def main():
#check for uniform distribution
    f = open("log.txt", 'w')
    random_values = []
    distribution = {}
    number_limit = 100
    for i in range(number_limit):
        distribution[i] = 0
    for i in range(number_limit*10000):
        num = get_random_num(number_limit)
        random_values.append(num)
        distribution[num] += 1
    f.write("Random values: \n")
    f.write(str(random_values) + '\n')
    f.write("Distribution: \n")
    key_string = ""
    values = ""
    for key in distribution.keys():
        key_string += str(key) + ','
        values += str(distribution[key]) + ','
    key_string = key_string[:-1]
    values = values[:-1]
    f.write(key_string + '\n')
    f.write(values + '\n')
#Calculate median
    sorted_random_values = random_values.copy()
    sorted_random_values.sort()
    f.write("Median: \n")
    middle = len(random_values)//2
    f.write(str((sorted_random_values[middle] + sorted_random_values[middle+1])/2) +'\n')


#Calculate mean
    mean_sum = 0
    for i in range(len(random_values)):
        mean_sum += random_values[i]
        mean = mean_sum/(len(random_values))
    f.write("Mean: \n")
    f.write(str(mean) + '\n')

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
    f.write("Variance: \n")
    f.write(str(variance) +'\n')
    f.write("Standard deviation: \n")
    f.write(str(std_deviation) +'\n')

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
    f.write("Ascending runs: \n")
    f.write(str(ascending_runs) + '\n')
    f.write("Descending runs: \n")
    f.write(str(descending_runs) + '\n')
main()
