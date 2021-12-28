import math


def processId(NumberOfProcess):
    process = []
    for i in range(NumberOfProcess):
        process.append(int(i + 1))
    return process


def arrivalTime(NumberOfProcess):
    arr_time = [0]*NumberOfProcess
    for i in range(NumberOfProcess):
        arrivalTime = int(
            input('Enter arrivalTime of Process {}:     '.format(i+1)))
        arr_time[i] = arrivalTime
    return arr_time


def burstTime(NumberOfProcess):
    bur_time = [0]*NumberOfProcess
    for i in range(NumberOfProcess):
        burstTime = int(
            input('Enter burstTime of Process {}:     '.format(i+1)))
        bur_time[i] = burstTime
    return bur_time


def completionTime(NumberOfProcess, burstTime):
    comp_time = [0]*NumberOfProcess
    for i in range(1, NumberOfProcess+1):
        comp_time[i-1] = comp_time[NumberOfProcess-1] + \
            burstTime[NumberOfProcess-1]
    return comp_time


def priorityScheduling(NumberOfProcess, processId, arrivalTime, burstTime):
    priority = [0]*NumberOfProcess
    for i in range(NumberOfProcess):
        priority.append(
            int(input('Enter Priority of the Process {}:     '.format(i+1))))
    for i in range(NumberOfProcess):
        processId[i] = i
        for j in range(NumberOfProcess):
            for k in range(NumberOfProcess):
                if (priority[j] > priority[k]):
                    temp = priority[j]
                    priority[j] = priority[k]
                    priority[k] = temp
                    temp = burstTime[j]
                    burstTime[j] = burstTime[k]
                    burstTime[k] = temp
                    temp = arrivalTime[j]
                    arrivalTime[j] = arrivalTime[k]
                    arrivalTime[k] = temp
                    temp = processId[j]
                    processId[j] = processId[k]
                    processId[k] = temp

        processId.reverse()
        burstTime.reverse()
        arrivalTime.reverse()
        priority.reverse()
        return processId, burstTime, arrivalTime, priority


def waitingTime(NumberOfProcess, burstTime):
    wait_time = [0] * NumberOfProcess
    for i in range(1, NumberOfProcess):
        wait_time[i] = wait_time[i-1] + burstTime[i-1]
    return wait_time


def turnaroundTime(NumberOfProcess, burstTime, waitingTime):
    turnaround_time = [0] * NumberOfProcess
    for index in range(NumberOfProcess):
        turnaround_time[index] = burstTime[index] + waitingTime[index]
    return turnaround_time


def throughPut(NumberOfProcess, completionTime, arrivalTime):
    throughput = 0
    throughPut = completionTime[NumberOfProcess-1] + arrivalTime[0]
    throughput = throughput/NumberOfProcess
    print("Throughput:   ", throughput)


def displayTable(NumberOfProcess, arr_time, bur_time, wait_time, turnaround_time, priority):
    print('Process\t\tArrival time\t\tBurst Time\t\tWaiting Time\t\tTurnaround Time\t\tpriority')
    for i in range(len(NumberOfProcess)):
        print(str(NumberOfProcess[i]) + '\t\t\t\t' + str(arr_time[i]) + '\t\t\t\t'
              + str(bur_time[i]) + '\t\t\t\t' + str(wait_time[i]
                                                    ) + '\t\t\t\t' + str(turnaround_time[i])
              + str(priority[i]))


if __name__ == "__main__":
    NumberOfProcess = int(input('Enter Number of Process:     '))
    processId = processId(NumberOfProcess)
    arrivalTime = arrivalTime(NumberOfProcess)
    burstTime = burstTime(NumberOfProcess)
    Priority = priorityScheduling(
        NumberOfProcess, processId, arrivalTime, burstTime)
    completionTime = completionTime(NumberOfProcess, burstTime)
    waitingTime = waitingTime(NumberOfProcess, burstTime)
    turnaroundTime = turnaroundTime(NumberOfProcess, burstTime, waitingTime)
    displayTable(processId, arrivalTime, burstTime,
                 waitingTime, turnaroundTime, Priority)
    print('Average Waiting Time:    ', sum(waitingTime)/len(waitingTime))
    print('Average Turnaround Time:    ', sum(
        turnaroundTime)/len(turnaroundTime))

    throughPut = throughPut(NumberOfProcess, completionTime, arrivalTime)
