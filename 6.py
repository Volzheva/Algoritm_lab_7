import time
import os, psutil
import random


def find_max_increasing_subsequence(arr, num):
    ans = [1 for _ in range(num)]
    ans_numbers = [None for _ in range(num)]
    for i in range(1, num):
        for j in range(0, i - 1):
            if arr[i] > arr[j]:
                if (ans[j] + 1) > ans[i]:
                    ans_numbers[i] = (j, arr[i]) # первый элемент кортежа - ссылка на предыдущий, второй - значение предыдущего
                    ans[i] = ans[j] + 1
                else:
                    ans[i] = ans[i]

    final_answer = []
    for i in range(len(ans)):
        if ans[i] == max(ans):
            cur = i
            break

    while ans_numbers[cur] is not None:
        final_answer.append(ans_numbers[cur][1])
        cur = ans_numbers[cur][0]
    final_answer.append(arr[cur]) #добавляем первый элемент

    return final_answer[::-1]


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("6_input.txt")
m = open("6_output.txt", "w")

count = int(f.readline())
string = f.readline()
elements = list(map(int, string.split()))

# # for tests:
# elements = []
# count = 5000
# for i in range(count):
#     elements.append(random.randint(-1000000000, 1000000000))
#
answer = find_max_increasing_subsequence(elements, count)

m.write(str(len(answer)) + "\n" )
for i in answer:
    m.write(str(i) + " ")
f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
