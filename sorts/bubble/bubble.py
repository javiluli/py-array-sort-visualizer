import time

def bubble_sort(data, drawData=None, timeTick=0):
    for _ in range(len(data)):
        for j in range(len(data) - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            if drawData != None:
                drawData(data, ['limegreen' if x == j + 1 else "steelblue" for x in range(len(data))])
            time.sleep(timeTick)
    if drawData != None:
        drawData(data, ['limegreen' for x in range(len(data))])
    return data
