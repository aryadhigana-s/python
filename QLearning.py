import numpy as n
import pandas as p
import random

R = p.read_csv('DataTugasML3.txt', delimiter = '\t', header = None)
R = n.array(R).tolist()


def make_mR(R):
    lenx = len(R)
    leny = len(R[0])
    mtx = p.DataFrame(columns = ['nilai','up','down','right','left'])
    k = 0
    for i in range(leny):
        for j in range(lenx):
            tempR = [R[i][j],float('-inf'), float('-inf'),float('-inf'),float('inf')]
            if i>0: #up
                tempR[1] = R[i-1][j]
            if i<leny-1: #down
                tempR[2] = R[i+1][j]
            if j < lenx - 1: #right
                tempR[3] = R[i][j + 1]
            if j>0: #left
                tempR[4] = R[i][j-1]
            mtx.loc[k]= tempR
            k+=1
    return mtx


def index_mR(R):
    lenx = len(R)
    leny = len(R[0])
    mtx = p.DataFrame(columns=['nilai', 'up', 'down', 'right', 'left'])
    k = 0
    for i in range(leny):
        for j in range(lenx):
            tempR = [k, float(101), float(101), float(101), float(101)]
            if i > 0:  # up
                tempR[1] = k-lenx
            if i < leny - 1:  # down
                tempR[2] = k+lenx
            if j < lenx - 1:  # right
                tempR[3] = k+1
            if j > 0:  # left
                tempR[4] = k-1
            mtx.loc[k] = tempR
            k += 1
    return mtx



hasilR = make_mR(R)
hasilR = n.array(hasilR)

hasilAction = index_mR(R)
hasilAction = n.array(hasilAction)

Q = n.zeros((100,5))

for i in range(len(Q)):
    Q[i][0]= i

g = 0.9
episode = 1000
reward = []
print(hasilAction)
print(hasilR)
for i in range(episode):
    start = 90
    goal = 9
    temp = start
    temp_reward = hasilR[temp][0]

    while temp != goal:
        action = random.randint(1,4)
        while hasilAction[temp][action] == 101:
            action = random.randint(1,4)
        next = hasilAction[temp][action]
        next = int(next)

        satu = Q[next][1]
        dua = Q[next][2]
        tiga = Q[next][3]
        empat = Q[next][4]
        nmax = max(satu,dua,tiga,empat)
        hasil = hasilR[temp][action] + g*nmax
        Q[temp][action] = hasil

        temp = next
        temp_reward += hasilR[temp][0]
        if (temp==goal):
            print("Episode-",i," score: ",temp_reward)
            reward.append(temp_reward)

print(reward)
print(max(reward))
#print(max(reward))

# while y[0][action] > 100 :
#     action = random.randint(1,4)
# print(y[0][action])