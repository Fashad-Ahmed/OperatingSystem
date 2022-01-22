from re import M

def LRU(frameLength, pages):
    memory = [None]*frameLength
    halEnd = {}
    hit = 0
    miss = 0
    i = 0
    char = 0
    virtualMemory = []

    for j in pages:
        if j in memory:
            hit = hit + 1
            halEnd[j] = hit
            continue
        elif i < frameLength:
            miss = miss + 1
            memory[i] = j
            i = i + 1
        else:
            miss = miss + 1
            char = 1
            for iter in memory:
                if iter in halEnd.keys():
                    char = char + 1
                    continue
                else:
                    var = memory[iter]
                    virtualMemory.append(iter)
                    memory[var] = j
                if frameLength == char:
                    sns = {}
                    lowestHit = min(halEnd.values())
                    for key, val in halEnd.items():
                        if lowestHit == val:
                            sns[key] = val
                    if len(sns) == 1:
                        virtualMemory.append(sns.keys())
                        virtualMemory[sns.keys()]
                        memory[var] = j
                    else:
                        mnm = frameLength
                        for itert in sns:
                            z = memory[itert]
                            if mnm > z:
                                z = mnm
                        virtualMemory.append(memory[mnm])
                        memory[mnm] = j
    print(hit, miss, memory, virtualMemory)

if __name__ == "__main__":

    frameLength = int(input('Enter the size of frame: '))
    page = int(input('Enter the size of pages: '))
    pages = []
    for i in range(page):
        page = int(input('Enter page number: '))
        pages.append(page)
    LRU(frameLength, pages)
