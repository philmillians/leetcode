class Solution:
    def duplicateZeros(self, arr):
        zerosFound = 0
        length = len(arr) - 1
        for item in range(length + 1):
            if item > length - zerosFound:
                break
            if arr[item] == 0: 
                if item == length - zerosFound:
                    arr[length] = 0 
                    length -= 1
                    break
                zerosFound += 1
              
        last = length - zerosFound
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + zerosFound] = 0
                zerosFound -= 1
                arr[i + zerosFound] = 0
            else:
                arr[i + zerosFound] = arr[i]
        return arr
