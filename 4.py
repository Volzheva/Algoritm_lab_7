import time
import os, psutil
import random


def find_max_subsequence(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    p = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                p[i][j] = (i - 1, j - 1, arr1[i - 1])
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    p[i][j] = (i - 1, j, "") # первые 2 элемента кортежа - ссылки на предыдущий, третий - значение предыдущего
                else:
                    dp[i][j] = dp[i][j - 1]
                    p[i][j] = (i, j - 1, "")

    ans = []
    cur = p[n][m]
    while cur is not None:
        if len(cur[2]) > 0:
            ans.append(int(cur[2]))
        cur = p[cur[0]][cur[1]]
    print(dp)
    print(p)
    return ans[::-1]


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("4_input.txt")
m = open("4_output.txt", "w")

count1 = int(f.readline())
string1 = f.readline()
elements1 = list(map(str, string1.split()))

count2 = int(f.readline())
string2 = f.readline()
elements2 = list(map(str, string2.split()))

# # for tests:
# elements1 = []
# elements2 = []
# for i in range(100):
#     elements1.append(str(random.randint(-1000000000, 1000000000)))
# for i in range(100):
#     elements2.append(str(random.randint(-1000000000, 1000000000)))

m.write(str(len(find_max_subsequence(elements1, elements2))))


f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
