
import random
# matrix_A  训练集
matrix_A = [[1,4], [2,5], [5,1], [4,2]]
Matrix_y = [19,26,19,20]
theta = [2,5]
#学习速率
leraing_rate = 0.005
loss = 50
iters = 1
Eps = 0.0001
#随机梯度下降
while loss>Eps and iters <1000 :
    loss = 0
    i = random.randint(0, 3)
    h = theta[0]*matrix_A[i][0] + theta[1]*matrix_A[i][1] 
    theta[0] = theta[0] + leraing_rate*(Matrix_y[i]-h)*matrix_A[i][0]
    theta[1] = theta[1] + leraing_rate*(Matrix_y[i]-h)*matrix_A[i][1]
    Error = 0
    Error = theta[0]*matrix_A[i][0] + theta[1]*matrix_A[i][1] - Matrix_y[i]
    Error = Error*Error
    loss = loss +Error
    iters = iters +1
print ('theta=',theta)
print ('iters=',iters)

#梯度下降
while loss>Eps and iters <1000 :
    loss = 0
    for i in range(4):
        h = theta[0]*matrix_A[i][0] + theta[1]*matrix_A[i][1] 
        theta[0] = theta[0] + leraing_rate*(Matrix_y[i]-h)*matrix_A[i][0]
        theta[1] = theta[1] + leraing_rate*(Matrix_y[i]-h)*matrix_A[i][1]
    for i in range(4):
        Error = 0
        Error = theta[0]*matrix_A[i][0] + theta[1]*matrix_A[i][1] - Matrix_y[i]
        Error = Error*Error
        loss = loss +Error
    iters = iters +1
print ('theta=',theta)
print ('iters=',iters)


#批量梯度下降
while loss>Eps and iters <1000 :
    loss = 0
    sampleindex =  random.sample([0,1,2,3],2)
    for i in sampleindex :
        h = theta[0]*matrix_A[i][0] + theta[1]*matrix_A[i][1] 
        theta[0] = theta[0] + leraing_rate*(Matrix_y[i]-h)*matrix_A[i][0]
        theta[1] = theta[1] + leraing_rate*(Matrix_y[i]-h)*matrix_A[i][1]
    for i in sampleindex :
        Error = 0
        Error = theta[0]*matrix_A[i][0] + theta[1]*matrix_A[i][1] - Matrix_y[i]
        Error = Error*Error
        loss = loss +Error
    iters = iters +1
print ('theta=',theta)
print ('iters=',iters)
