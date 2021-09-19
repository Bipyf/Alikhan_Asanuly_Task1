def permutate(arr, i, j):
    if i==j:
        print (arr)
    else:
        for k in range(i, j+1):
            temp = arr[i]
            arr[i] = arr[k]
            arr[k] = temp
            permutate(arr, i+1, j)
            temp = arr[i]
            arr[i] = arr[k]
            arr[k] = temp

def main():
    st = input()
    j = len(st)
    arr = list(st)
    permutate(arr, 0, j-1)
main()
