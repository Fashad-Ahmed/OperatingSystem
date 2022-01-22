from concurrent.futures import process


def MFT(n, partitionSize, portionBlock):
    memory = {"OS": 40}
    totalSize = (n * partitionSize) + memory['OS']

    for i in range(len(portionBlock)):
        processVal = partitionSize - portionBlock[i]
        if (processVal > 0):
            memory['P' + str(i+1)] = processVal

    print(f"Memory Size: {totalSize}")
    print(f"Partition Size Reserved for OS: {memory['OS']}")
    internalFragmentation = 0
    for i, j in memory.items():
        if (i != 'os' or i != 'OS'):
            internalFragmentation += j
            print(f"{i} \t\t {j}")
    print(f"Total Internal Fragmentation: {internalFragmentation}")


if __name__ == "__main__":

    n = 6
    partitionSize = 150
    portionBlock = [40, 30, 60, 55, 90]

    MFT(n, partitionSize, portionBlock)
