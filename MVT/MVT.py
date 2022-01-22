def MVT(memorySize, portionBlock):
    memory = {"OS": 50}
    unprocessedArr = []
    externalFragmentation = 0
    print(f"Total Memory Size Before: {memorySize}")

    for i in range(len(portionBlock)):
        if (memorySize > portionBlock[i] and memorySize >= 0):
            memorySize = memorySize - portionBlock[i]
            memory['P' + str(i+1)] = portionBlock[i]
        else:
            unprocessedArr.append(f'P {str(i)}')
            externalFragmentation = memorySize

    print(f"Total Memory Size After: {memorySize}")
    print(f"Partition Size Reserved for OS: {memory['OS']}")

    for i, j in memory.items():
        if (i != 'os' or i != 'OS'):
            externalFragmentation += j
            print(f"{i} \t\t {j}")
    print(f"Total External Fragmentation: {externalFragmentation}")


if __name__ == "__main__":

    memorySize = 500
    portionBlock = [40, 30, 60, 55, 90]

    MVT(memorySize, portionBlock)
