import csv

#class DSASort():
    #def __init__(self, maxSize):
        #self.array = [None] * maxSize
        #for i in range(maxSize):
            #self.array[i] = DSASort.DSASortEntry(None, None)
        #self.count = 0

    #def insertData(self, name, value):
        #self.array[self.count].name = name
        #self.array[self.count].value = value
        #self.count += 1

def bubbleSort(array):
    #array = self.array
    for i in range(len(array)-1):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
    return array

def insertionSort(array):
    #array = self.array
    for nn in range(len(array)):
        ii = nn
        temp = array[ii]
        while ii > 0 and array[ii-1] > temp:
            array[ii] = array[ii-1]
            ii -= 1
        array[ii] = temp
    return array

def selectionSort(array):
    #array = self.array
    for i in range(0, len(array)):
        minIdx = i  
        for j in range(i+1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j
        temp = array[minIdx]
        array[minIdx] = array[i]
        array[i] = temp
    return array

def mergeSort(array):
    #array = self.array
    leftIdx = 0
    rightIdx = len(array) - 1
    mergeSortRec(array, leftIdx, rightIdx)
    return array

def mergeSortRec(array, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        midIdx = (leftIdx +rightIdx) // 2
        mergeSortRec(array, leftIdx, midIdx)
        mergeSortRec(array, midIdx+1, rightIdx)
        merge(array, leftIdx, midIdx, rightIdx)

    return array

def merge(array, leftIdx, midIdx, rightIdx):
    tempArr = [None] * (rightIdx - leftIdx + 1)
    ii = leftIdx
    jj = midIdx + 1
    kk = 0
    while ii <= midIdx and jj <= rightIdx:
        if array[ii] <= array[jj]:
            tempArr[kk] = array[ii]
            ii += 1
        else:
            tempArr[kk] = array[jj]
            jj += 1
        kk += 1
    for ii in range(ii, midIdx+1):
        tempArr[kk] = array[ii]
        kk += 1
    for jj in range(jj, rightIdx+1):
        tempArr[kk] = array[jj]
        kk += 1
    for kk in range(leftIdx, rightIdx+1):
        array[kk] = tempArr[kk-leftIdx]
        
    return array
    
def quickSort(array):
    #leftIdx = 0
    #rightIdx = len(array) - 1
    #quickSortRec(array, leftIdx, rightIdx)
    ###########
    leftIdx = array[0]
    rightIdx = array[len(array) - 1]
    midIdx = array[(leftIdx+rightIdx)//2]
    average = (leftIdx + rightIdx + midIdx)/3
    quickSortRec(array, average, average)

def quickSortRec(array, leftIdx, rightIdx):
    if rightIdx > leftIdx:
      pivotIdx = (leftIdx + rightIdx) // 2
      newPivotIdx = doPartitioning(array, leftIdx, rightIdx, pivotIdx)
      
      quickSortRec(array, leftIdx, newPivotIdx-1)
      quickSortRec(array, newPivotIdx+1, rightIdx)
    return array

def doPartitioning(array, leftIdx, rightIdx, pivIdx):
    pivotVal = array[pivIdx] #######
    array[pivIdx] = array[rightIdx]
    array[rightIdx] = pivotVal
    currIdx = leftIdx
    for ii in range(leftIdx, rightIdx):
        if array[ii] < pivotVal:
            temp = array[ii]
            array[ii] = array[currIdx]
            array[currIdx] = temp
            currIdx += 1
    newPivIdx = currIdx
    array[rightIdx] = array[newPivIdx]
    array[newPivIdx] = pivotVal
    return newPivIdx

def printArray(array):
    for i in range(len(array)):
        print(array[i], " == ", array[i])

def prints(array):
    print(len(array))

    #class DSASortEntry():
        #def __init__(self, inName, inValue):
            #self.name = inName
            #self.value = inValue


