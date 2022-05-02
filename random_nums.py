import psutil
import os
import time

def get_random_num(range_lim):
    info = psutil.sensors_temperatures()
    sum_temps = 0
    for item in info['coretemp']:
        sum_temps += item[1]
    salt = 0
    temp = -1
    for i in range(10):
        temp = os.fork()
        if temp != 0:
            salt += float(temp)
        else:
            exit()
    return int(str(float(sum_temps / salt)%range_lim)[-2])