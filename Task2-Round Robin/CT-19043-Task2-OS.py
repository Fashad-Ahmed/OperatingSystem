import math

def completionTime(NumberOfProcess, arr_time, bur_time, quantamTime):
    temp_arr = [index for index in arr_time]
    temp_arr.sort()
    temp_arr_two = [0] * NumberOfProcess
    temp_arr_three = [0] * NumberOfProcess
    comp_time = [0] * NumberOfProcess

    for i in temp_arr:
        temp_arr_two.append(arr_time.index(i))
    for j in temp_arr_two:
        temp_arr_three.append(bur_time[j])
    print(temp_arr[0])
    count = 0
    if temp_arr[0] != 0:
        count += temp_arr[0]

    value = True
    while value is True:
        for index in range(NumberOfProcess):
            value = False
            if temp_arr_three[index] >= quantamTime:
                count += quantamTime
                temp_arr_three[index] -= quantamTime
            else:
                count += temp_arr_three[index]
                temp_arr_three[index] = 0
            if temp_arr_three[index] == 0:
                comp_time[index] += count
        if value is True:
            break
    # print(comp_time)
    return comp_time, temp_arr


def turnaroundTime(NumberOfProcess, arr_time, comp_time):
    turnaround_time = [0] * NumberOfProcess
    for index in range(NumberOfProcess):
        turnaround_time[index] = comp_time[index] + arr_time[index]
    return turnaround_time


def waitingTime(NumberOfProcess, turnaround_time, bur_time):
    wait_time = [0] * NumberOfProcess
    for index in range(NumberOfProcess):
        wait_time[index] = turnaround_time[index] - bur_time[index]
    return wait_time


def throughPut(NumberOfProcess, bur_time, arr_time):
    throughput = 0
    for i in range(NumberOfProcess):
        throughput += abs(bur_time[i] - arr_time[i])
    throughput = throughput / NumberOfProcess
    print("Throughput:   ", throughput)


def displayTable(NumberOfProcess, arr_time, bur_time, wait_time, turnaround_time, comp_time):
    print('Process\t\tArrival time\t\tBurst Time\t\tWaiting Time\t\tTurnaround Time')
    for i in range(NumberOfProcess):
        print(
            str(i + 1) + '\t\t' + str(arr_time[i]) + '\t\t\t\t'
            + str(bur_time[i]) + '\t\t' + str(wait_time[i]) +
            '\t\t\t' + str(turnaround_time[i])
        )

def roundRobin(NumberOfProcess, quantamTime):
    arr_time = [0] * NumberOfProcess
    bur_time = [0] * NumberOfProcess

    for i in range(NumberOfProcess):
        arrivalTime = int(input('Enter arrivalTime of Process {}:     '.format(i + 1)))
        arr_time[i] = arrivalTime

        burstTime = int(input('Enter burstTime of Process {}:     '.format(i + 1)))
        bur_time[i] = burstTime

    completionTime(NumberOfProcess, arr_time, bur_time, quantamTime)
    comp_time = completionTime(NumberOfProcess, arr_time, bur_time, quantamTime)
    turnaroundTime(NumberOfProcess, arr_time, comp_time[0])
    turnaround_time = turnaroundTime(NumberOfProcess, arr_time, comp_time[0])
    waitingTime(NumberOfProcess, turnaround_time, bur_time)
    wait_time = waitingTime(NumberOfProcess, turnaround_time, bur_time)
    displayTable(NumberOfProcess, arr_time, bur_time, wait_time, turnaround_time, comp_time[0])
    print('Quantam Time:        ', quantamTime)
    throughPut(NumberOfProcess, bur_time, arr_time)

    print('Average Waiting Time:    ', sum(wait_time) / len(wait_time))
    print('Average Turnaround Time:    ', sum(turnaround_time) / len(turnaround_time))


if __name__ == "__main__":
    NumberOfProcess = int(input('Enter Number of Process:     '))
    quantamTime = 43
    roundRobin(NumberOfProcess, quantamTime)
