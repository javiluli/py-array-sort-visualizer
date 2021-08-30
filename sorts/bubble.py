import time

def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data)):
        for j in range(len(data) - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['limegreen' if x == j + 1 else "steelblue" for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data, ['limegreen' for x in range(len(data))])
