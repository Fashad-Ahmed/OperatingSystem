import math

def waitingTime(NumberOfProcess, arr_time, bur_time):
    wait_time = [0] * NumberOfProcess
    service_time = [0] * NumberOfProcess
    service_time[0] = 0

    for i in range(1, NumberOfProcess):
        service_time[i] = service_time[i-1] + bur_time[i-1]

    for index in range(NumberOfProcess):
        wait_time[index] = abs(service_time[index] - arr_time[index])
    return wait_time

def turnaroundTime(NumberOfProcess, bur_time, wait_time):
    turnaround_time = [0] * NumberOfProcess
    for index in range(NumberOfProcess):
        turnaround_time[index] = bur_time[index] + wait_time[index]
    return turnaround_time

def throughPut(NumberOfProcess, bur_time, arr_time):
    throughput = 0
    for i in range(NumberOfProcess):
        throughput += abs(bur_time[i]) - abs(arr_time[i])
    throughput = throughput/NumberOfProcess
    print("Throughput:   ", throughput)

def fcfsSript(NumberOfProcess):
    arr_time = [0]*NumberOfProcess
    bur_time = [0]*NumberOfProcess

    for i in range(NumberOfProcess):
        arrivalTime = int(input('Enter arrivalTime of Process {}:     '.format(i+1)))
        arr_time[i] = arrivalTime

        burstTime = int(input('Enter burstTime of Process {}:     '.format(i+1)))
        bur_time[i] = burstTime

    waitingTime(NumberOfProcess, arr_time, bur_time); wait_time = waitingTime(NumberOfProcess, arr_time, bur_time)
    turnaroundTime(NumberOfProcess, bur_time, wait_time); turnaround_time = turnaroundTime(NumberOfProcess, bur_time, wait_time)
    displayTable(NumberOfProcess, arr_time, bur_time, wait_time, turnaround_time)
    throughPut(NumberOfProcess, bur_time, arr_time)

    print('Average Waiting Time:    ', sum(wait_time)/len(wait_time))
    print('Average Turnaround Time:    ', sum(turnaround_time)/len(turnaround_time))

def displayTable(NumberOfProcess, arr_time, bur_time, wait_time, turnaround_time):
    print('Process\t\tArrival time\t\tBurst Time\t\tWaiting Time\t\tTurnaround Time')
    for i in range(NumberOfProcess):
        print(str(i+1) + '\t\t\t\t' + str(arr_time[i]) + '\t\t\t\t'
              + str(bur_time[i]) + '\t\t\t\t' + str(wait_time[i]) + '\t\t\t\t' + str(turnaround_time[i]))

if __name__ == "__main__":
    NumberOfProcess = int(input('Enter Number of Process:     '))
    fcfsSript(NumberOfProcess)