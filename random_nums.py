import psutil
import os
import time

#print(psutil.virtual_memory())
def get_random_num(range_lim):
    info = psutil.sensors_temperatures()
    sum_temps = 0
    for item in info['coretemp']:
        sum_temps += item[1]
    salt = 0

    temp = -1
    for i in range(2):
        temp = os.fork()
        if temp != 0:
            salt += float(temp)
            waitpid(temp, 0)
        else:
            exit()

    extra_seasoning = float(str(psutil.virtual_memory()[1])[-3:-1])
    return int((float(sum_temps + salt)+extra_seasoning)%range_lim)
