def Segementation(processSegment, memorySize, mem):

    def find(pred, itr):
        for element in itr:
            if pred(element):
                return element
        return None

    for i in processSegment:
        print(i["no"], "\t", i["size"])

    for i in mem:
        print(i["address"], "\t\t", i["status"])

    print(f'\nMemory Size: {memorySize}')

    segTab = []
    for i in range(len(processSegment)):
        for j in range(len(mem)):
            if mem[j]['status'] == 'free':
                space = memorySize-mem[j]['address']\
                    if j == len(mem)-1 else mem[j+1]['address']-mem[j]['address']
                if space == processSegment[i]['size']:
                    mem[j]['status'] = f"{processSegment[i]['no']}"
                    segTab.append({'segment_no': i,
                                   'limit': processSegment[i]['size'],
                                   'base_address': mem[j]['address']})

    for i in mem:
        print(i["address"], "\t\t", i["status"])

    for i in segTab:
        print(i["segment_no"], "\t\t", i["limit"], "\t\t", i["base_address"])

    requested_segment = int(input('From which segment you want to read byte?'))
    requested_byte = int(
        input(f"which byte of segment:{requested_segment} you want to read?"))

    print(f"Requested Segment: {requested_segment}")
    print(f"Requested Byte of Requested Segment: {requested_byte}")

    segment_no = bin(int(requested_segment))
    segment_offset = bin(int(requested_byte))
    logical_address = f"{segment_no}{segment_offset}"

    print(f"Segment No: {segment_no}")
    print(f"Segment Offset: {segment_offset}")
    print(f"Logical Address: {logical_address}")

    entry = find(lambda object: object.get(
        "segment_no") == int(segment_no, 2), segTab)
    print(f"Concerned Entry of Segment Table: {entry}")

    if entry['limit'] < int(segment_offset, 2):
        print("Invalid Address")

    physical_address = bin(
        (entry["base_address"] + int(segment_offset, 2)))[2:]
    loc = int(physical_address, 2)

    print(f"Physical Address: {physical_address}")
    print(f"Location in Memory: {loc}")


if __name__ == "__main__":

    processSegment = [
        {'no': 0, 'size': 300},
        {'no': 1, 'size': 50},
        {'no': 2, 'size': 500},
        {'no': 3, 'size': 100},
        {'no': 4, 'size': 100}
    ]
    memorySize = 2550
    mem = [
        {'address': 0, 'status': 'OS'}, {'address': 1500, 'status': 'free'},
        {'address': 1800, 'status': 'free'},
        {'address': 2300, 'status': 'free'}, {
            'address': 2400, 'status': 'free'},
        {'address': 2500, 'status': 'free'}
    ]
    Segementation(processSegment, memorySize, mem)
