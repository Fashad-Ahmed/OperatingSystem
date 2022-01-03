
def displayBlock(processSize, segments):
    print()
    print("Process No. Process Size")
    for i in range(len(processSize)):
        print(i + 1, "         ", processSize[i],
              end="         ")
        if segments[i] != -1:
            print(segments[i] + 1)
        else:
            print("Not Allocated")


def firstFit(blockSize, processSize):
    segments = [-1] * len(processSize)
    for i in range(len(processSize)):
        for j in range(len(blockSize)):
            if blockSize[j] >= processSize[i]:
                segments[i] = j
                blockSize[j] -= processSize[j]
    displayBlock(processSize, segments)


def bestFit(blockSize, processSize):
    segments = [-1] * len(processSize)
    for i in range(len(processSize)):
        bestIndex = -1
        for j in range(len(blockSize)):
            if blockSize[j] >= processSize[i]:
                if bestIndex == -1:
                    bestIndex = j
                elif blockSize[bestIndex] > blockSize[j]:
                    bestIndex = j
        if bestIndex != -1:
            segments[i] = bestIndex
            blockSize[bestIndex] -= processSize[i]
    displayBlock(processSize, segments)


def worstFit(blockSize, processSize):
    segments = [-1] * len(processSize)
    for i in range(len(processSize)):
        worstIndex = -1
        for j in range(len(blockSize)):
            if blockSize[j] >= processSize[i]:
                if worstIndex == -1:
                    worstIndex = j
                elif blockSize[worstIndex] < blockSize[j]:
                    worstIndex = j
        if worstIndex != -1:
            segments[i] = worstIndex
            blockSize[worstIndex] -= processSize[i]
    displayBlock(processSize, segments)


def sizeBlock(blockSize, processSize):
    if (processSize >= 0):
        print(blockSize)
        blcSize = [0]*blockSize
        prcSize = [0]*processSize

        for i in range(blockSize):
            val = int(input(f"Enter block item for segment {i+1}: "))
            blcSize[i] = val

        for i in range(processSize):
            val = int(input(f"Enter process size for segment {i+1}: "))
            prcSize.append(val)

        bestFit(blcSize, prcSize)
        firstFit(blcSize, prcSize)
        worstFit(blcSize, prcSize)

    else:
        print("Not possible!")


if __name__ == "__main__":

    blockSize = int(input('Enter block size: '))
    processSize = int(input('Enter Number of Process: '))
    sizeBlock(blockSize, processSize)
