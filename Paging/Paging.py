
def Paging(processSize, memorySize, processPages, memoryPages):

    pages = []
    for i in range(memoryPages):
        pages.append(i)
    print(f"\nPages: {pages}")

    physicalMemory = []
    x = 0
    for i in range(memoryPages):
        L = []
        for j in range(2):
            L.append(x)
            x += 1
        physicalMemory.append(L)
    print(f"Physical Memory: {physicalMemory}")

    process = []
    x = 0
    for i in range(processPages):
        L = []
        for j in range(2):
            L.append(x)
            x += 1
        process.append(L)
    print(f"\nProcess has {processPages} pages: {process}")

    memory = [[1, 1], [1, 1], [0, 0], [1, 1], [0, 0], [0, 0], [0, 0], [0, 0]]
    print(f"\nMemory before the processes are stored: {memory}")
    print("Here, 0 represents empty slots, 1 represents filled spots")

    pageTable = []
    for i in range(len(memory)):
        count = 0
        for j in range(2):
            if memory[i][j] == 1:
                break
            else:
                memory[i][j] = 1
                count += 1
        if count == 2:
            pageTable.append(i)
        if len(pageTable) == processPages:
            break
    print(f"\nPage Table storing frames: {pageTable}")

    byte = int(input("\nWHICH BYTE DO YOU WANT TO ACCESS? "))

    def DecimalToBinary(num):
        binaryByte = []
        if num >= 1:
            DecimalToBinary(num // 2)
            binaryByte.append(num % 2)
            DecimalToBinary(byte)

        for i in binaryByte:
            if binaryByte[0] == 0:
                binaryByte.pop(0)

        logicalAddress = ""
        for i in binaryByte:
            logicalAddress += str(i)
            physicalAddress = int(logicalAddress)
            print(f"\nLogical Address: {logicalAddress}")

        offset = binaryByte[len(binaryByte) - 1]
        binaryByte.pop()
        pageNo = ""
        for i in binaryByte:
            pageNo += str(i)
            binaryPageNo = pageNo
            pageNo = int(pageNo, 2)
            print(
                f"Where, page number is {binaryPageNo} and offset is {offset}.")

        frameNo = pageTable[int(pageNo)]
        binaryByte = []
        DecimalToBinary(frameNo)

        for i in binaryByte:
            if binaryByte[0] == 0:
                binaryByte.pop(0)

        frameNo = ""
        for i in binaryByte:
            frameNo += str(i)
            binaryByte.append(offset)

        binary = ""
        for i in binaryByte:
            binary += str(i)
            physicalAddress = int(binary)
            print(f"\nPhysical Address: {physicalAddress}")
            print(f"Where, frame number is {frameNo} and offset is {offset}.")

    def binaryToDecimal(binary):
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while (binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary // 10
            i += 1
        print(f"\n{byte} IS STORED AT LOCATION {decimal} IN MEMORY.")
        binaryToDecimal(physicalAddress)
        print(f"\nMemory after the processes are stored: {memory}")


if __name__ == "__main__":
    processSize = int(input("Enter process size: "))
    memorySize = int(input("Enter size of memory: "))
    processPages = processSize//2
    memoryPages = memorySize//2
    Paging(processSize, memorySize, processPages, memoryPages)
