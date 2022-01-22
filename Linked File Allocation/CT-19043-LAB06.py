import random as r
import math as m


def LinkedFileAllocation(processes_arr, memory_blocks_arr, already_filled):

    filled_blocks_arr = [0]*len(memory_blocks_arr)
    remaining_partitions = memory_blocks-already_filled
    for i in range(processes):
        current_process = processes_arr[i]
        random_partition = pickRandom(memory_blocks)
        isFirstPartition = True
        while (current_process > 0) and (remaining_partitions > 0) and m.ceil(current_process/size_of_partition) <= remaining_partitions:
            while memory_blocks_arr[random_partition] == 0:
                random_partition = pickRandom(memory_blocks)
            if isFirstPartition:
                processes_arr_result[i] = random_partition
            else:
                filled_blocks_arr[prev] = random_partition
            current_process -= size_of_partition
            isFirstPartition = False
            prev = random_partition
            memory_blocks_arr[random_partition] = 0
            remaining_partitions -= 1
        if current_process <= 0:
            filled_blocks_arr[random_partition] = -1
        else:
            processes_arr_result[i] = -1
    fetching_processes(list(processes_arr), list(processes_arr_result), list(
        filled_blocks_arr), list(memory_blocks_arr))


def fetching_processes(processes_arr, processes_arr_result, filled_blocks_arr, memory_blocks_arr):
    remaining_blocks_arr = []
    for i in range(len(processes_arr_result)):
        print(f"Process P{i+1}")
        print(f"\tSize: {processes_arr[i]} kb")

        if processes_arr_result[i] != -1:
            print("\tProcess allocated partitions: ")
        else:
            print("No Space to Accomodate")
        index = processes_arr_result[i]
        print("\t", end="")
        while index != -1:
            print(index, end="")
            index = filled_blocks_arr[index]
            if index != -1:
                print(", ", end="")
        print("\n")
    print("Empty partitions:")

    for i in range(len(memory_blocks_arr)):
        if (memory_blocks_arr[i] == size_of_partition):
            remaining_blocks_arr.append(i)
    if len(remaining_blocks_arr) > 0:
        print(remaining_blocks_arr)
    else:
        print("No remaining partitions avilable\n")


def pickRandom(memory_blocks):
    return r.randrange(0, memory_blocks)


if __name__ == "__main__":

    size_of_partition = int(input('Enter the size of partition: '))
    print("\n")

    memory_blocks = int(input('Enter the size of memory blocks: '))
    print("\n")
    memory_blocks_arr = [size_of_partition]*memory_blocks

    processes = int(input('Enter Number of processes '))
    print('\n')

    processes_arr = []
    for i in range(processes):
        process_val = int(input(f'Enter process {i+1} value '))
        processes_arr.append(process_val)

    processes_arr_result = [0]*processes

    memory_blocks_arr[19] = 0
    memory_blocks_arr[8] = 0
    memory_blocks_arr[5] = 0
    memory_blocks_arr[54] = 0
    already_filled = 5

    print("\n\nSize of single partition:", size_of_partition)
    print("Totalblocks", memory_blocks)
    print("Following blocks are already filled", [2, 6, 12, 24])
    print("Total processes", processes)
    print("\n")

    LinkedFileAllocation(list(processes_arr), list(
        memory_blocks_arr), already_filled)
