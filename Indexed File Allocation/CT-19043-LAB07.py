import random as r
import math as m


def IndexedFileAllocation(processes_arr, memory_blocks_arr, already_filled):

    remaining_partitions = len(memory_blocks_arr)-already_filled
    filled_array_blocks = [None]*memory_blocks
    for i in range(processes):
        current_process = processes_arr[i]
        if remaining_partitions >= m.ceil(current_process/size_of_partition):
            indexFile = pickRandom(memory_blocks)
        while memory_blocks_arr[indexFile] == 0:
            indexFile = pickRandom(memory_blocks)
        memory_blocks_arr[indexFile] = 0
        remaining_partitions -= 1

        processes_arr_result[i] = indexFile

        temp_arr = []
        while current_process > 0 and remaining_partitions >= m.ceil(current_process/size_of_partition) and remaining_partitions > 0:
            index = pickRandom(memory_blocks)
            while memory_blocks_arr[index] == 0:
                index = pickRandom(memory_blocks)
                memory_blocks_arr[index] = 0
                temp_arr.append(index)
                current_process -= size_of_partition
                remaining_partitions -= 1
        filled_array_blocks[indexFile] = temp_arr
    for j in range(len(filled_array_blocks)):
        if filled_array_blocks[j] != None:
            memory_blocks_arr[j] = filled_array_blocks[j]

    for i in range(processes):
        print("File size", processes_arr[i], "kb")
        if processes_arr_result[i] != -1:
            print("\tIndex file", processes_arr_result[i])
            print(
                f"\tAllocated blocks\n\t{memory_blocks_arr[processes_arr_result[i]]}")
        else:
            print("\tNo Space left ")
            print("\n\n")

    fetching_processes(processes_arr, processes_arr_result,
                       filled_array_blocks, memory_blocks_arr)


def fetching_processes(processes_arr, processes_arr_result, filled_blocks_arr, memory_blocks_arr):

    remaining_blocks_arr = []
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

    memory_blocks_arr[3] = 0
    memory_blocks_arr[8] = 0
    memory_blocks_arr[13] = 0
    memory_blocks_arr[23] = 0
    already_filled = 4

    print("\n\nSize of single partition:", size_of_partition)
    print("Totalblocks", memory_blocks)
    print("Following blocks are already filled", [2, 6, 12, 24])
    print("Total processes", processes)
    print("\n")

    IndexedFileAllocation(list(processes_arr), list(
        memory_blocks_arr), already_filled)
