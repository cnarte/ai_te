def printJobScheduling(arr, t):
    arr = sorted(arr,key = lambda x: x[2],reverse = True)
    result = [False] * t
    job = ['-1'] * t
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break
    print(job)
# Job scheduling
if __name__ == '__main__':
    N = int(input("enter number of jobs : "))
    arr = []
    default = raw_input("use all default?[y/n] ")
    if default in ["Y","y"]:
        arr = [["a",3,89],["b",1,32],["c",3,76],["d",6,54],["e",2,4]]
    else:
        for i in range(N):
            name,deadline,profit  = raw_input().split()
            deadline,profit = int(deadline),int(profit)

   
printJobScheduling(arr, 5 if default in ["Y","y"] else N)
 