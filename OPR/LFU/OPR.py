def OPR(frameLength, pages):
    memory = [None]*frameLength
    hit = 0
    miss = 0
    i = 0
    char = 0
    virtualMemory = []

    for j in pages:
        if j in memory:
            hit = hit + 1
            continue
        elif i < frameLength:
            miss = miss + 1
            memory[i] = j
            i = i + 1
        else:
            miss = miss + 1
            while char > frameLength:
                if memory[char] not in pages[j]:
                    virtualMemory.append(memory[char])
                    memory[char] = j
                    char = char + 1
                    break
                else:
                    char = char + 1
            char = 0 if char == frameLength else print(char)
    print(hit, miss, virtualMemory, memory)

if __name__ == "__main__":

    frameLength = int(input('Enter the size of frame: '))
    page = int(input('Enter the size of pages: '))
    pages = []
    for i in range(page):
        page = int(input('Enter page number: '))
        pages.append(page)
    OPR(frameLength, pages)
