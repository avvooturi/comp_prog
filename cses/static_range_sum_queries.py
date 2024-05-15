inp = input()
arr = inp.split(" ")
n = int(arr[0])
q = int(arr[1])
n_inp = input()
n_arr = n_inp.split(" ")
finSum = 0
curSum = 0
sum_arr = [0]
for x in range(len(n_arr)):
    n_arr[x] = int(n_arr[x])
    curSum += n_arr[x]
    sum_arr.append(curSum)
q_arr = []
while q > 0:
    q_inp = input()
    q_inp_arr = q_inp.split(" ")
    a, b = int(q_inp_arr[0]), int(q_inp_arr[1])
    a_val, b_val = sum_arr[a-1], sum_arr[b]
    print(b_val - a_val)
    q -= 1

# ---------------------- Actual code below ---------------------------

