def Fifo(frameLength, pages):
    memory = [None]*frameLength
    hit = 0; miss = 0; i = 0; char = 0;
    virtualMemory = []

    for p in pages:
        if p in memory:
            hit = hit + 1
        elif frameLength > i:
            miss = miss + 1
            memory[i] = p
            i = i + 1
        else:
            miss = miss + 1
            virtualMemory.append(memory[char])
            memory[char] = p
            char = char + 1
            char = 0 if char == frameLength else print(char)

if __name__ == "__main__":

    frameLength = int(input('Enter the size of frame: '))
    page = int(input('Enter the size of pages: '))
    pages = []
    for i in range(page):
        page = int(input('Enter page number: '))
        pages.append(page)

    Fifo(frameLength, pages)
