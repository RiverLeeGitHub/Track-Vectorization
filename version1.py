"""
Version 1
Uses normal bfs to traverse valid 8 directions in pixel
Uses dots as visited set
"""


import cv2
import copy

vessel = cv2.imread("vessel.png")
paint = vessel.copy()

print(paint.shape)

map = vessel[:,:,0]
visited = map.copy()
ret,map=cv2.threshold(map,100,255,cv2.THRESH_BINARY)

# # Find the initial point
# init_point = None
# for i in range(0, len(map)):
#     for j in range(0, len(map[0]), 2):
#         if map[i][j] > 0:
#             cv2.circle(paint, (j,i), 1, (255,0,0), 1)
#             init_point = [i, j]
#             print(init_point)

init_point = (700, 220)
print(init_point)
cv2.circle(paint, (init_point[1],init_point[0]), 10, (255,0,0), 2)
cv2.imshow("vessel", paint)
cv2.waitKey(0)

# visited = set()
# def dfs(point):
#
#     if point in visited:
#         return
#
#     i, j = point[0], point[1]
#     print(point)
#     visited.add(point)
#     # paint[i][j] = (0, 0, 255)
#     cv2.circle(visited, (point[1], point[0]), 10, (255, 255, 255), 2)
#     cv2.circle(paint, (point[1], point[0]), 1, (0, 255, 0), 3)
#
#     cv2.imshow("vessel", paint)
#     cv2.waitKey(1)
#
#     if map[i-1][j-1] > 0:
#         dfs((i-1,j-1))
#     if map[i-1][j] > 0:
#         dfs((i-1,j))
#     if map[i-1][j+1] > 0:
#         dfs((i-1,j+1))
#     if map[i][j-1] > 0:
#         dfs((i,j-1))
#     if map[i][j+1] > 0:
#         dfs((i,j+1))
#     if map[i+1][j-1] > 0:
#         dfs((i+1,j-1))
#     if map[i+1][j] > 0:
#         dfs((i+1,j))
#     if map[i+1][j+1] > 0:
#         dfs((i+1,j+1))
# dfs(init_point)









step = 10
visited = set()
father = dict()
waitList = [init_point]
father[init_point] = init_point
while len(waitList) > 0:

    # print(waitList)
    i, j = waitList[0][0], waitList[0][1]

    if waitList[0] in visited:
        waitList.pop(0)
        continue
    visited.add(waitList[0])
    paint[i][j] = (0, 0, 255)
    # cv2.circle(paint, (j,i), 3, (0, 255, 0), 2)

    father_i, father_j = father[waitList[0]][0], father[waitList[0]][1]
    cv2.line(paint, (father_j,father_i), (j,i), (0,255,0), 2)
    del father[waitList[0]]

    cv2.imshow("vessel", paint)
    cv2.waitKey(1)


    if map[i-step][j-step] > 0 and (i-step, j-step) not in visited:
        father[(i - step, j - step)] = (i, j)
        waitList.append((i-step,j-step))
    if map[i-step][j] > 0 and (i-step, j) not in visited:
        father[(i - step, j)] = (i, j)
        waitList.append((i-step,j))
    if map[i-step][j+step] > 0 and (i-step, j+step) not in visited:
        father[(i - step, j + step)] = (i, j)
        waitList.append((i-step,j+step))
    if map[i][j-step] > 0 and (i, j-step) not in visited:
        father[(i, j - step)] = (i, j)
        waitList.append((i,j-step))
    if map[i][j+step] > 0 and (i, j+step) not in visited:
        father[(i, j + step)] = (i, j)
        waitList.append((i,j+step))
    if map[i+step][j-step] > 0 and (i+step, j-step) not in visited:
        father[(i + step, j - step)] = (i, j)
        waitList.append((i+step,j-step))
    if map[i+step][j] > 0 and (i+step, j) not in visited:
        father[(i + step, j)] = (i, j)
        waitList.append((i+step,j))
    if map[i+step][j+step] > 0 and (i+step, j+step) not in visited:
        father[(i + step, j + step)] = (i, j)
        waitList.append((i+step,j+step))

    waitList.pop(0)








# step = 2
# visited = set()
# def bfs(waitList):
#
#     print(waitList)
#     i, j = waitList[0][0], waitList[0][1]
#
#     if waitList[0] in visited:
#         waitList.pop(0)
#         return
#     visited.add(waitList[0])
#     paint[i][j] = (0, 0, 255)
#     cv2.circle(paint, (j,i), 3, (0, 255, 0), 2)
#
#     waitList = []
#
#     cv2.imshow("vessel", paint)
#     cv2.waitKey(0)
#
#     if map[i-step][j-step] > 0 and (i-step, j-step) not in visited:
#         waitList.append((i-step,j-step))
#     if map[i-step][j] > 0 and (i-step, j) not in visited:
#         waitList.append((i-step,j))
#     if map[i-step][j+step] > 0 and (i-step, j+step) not in visited:
#         waitList.append((i-step,j+step))
#     if map[i][j-step] > 0 and (i, j-step) not in visited:
#         waitList.append((i,j-step))
#     if map[i][j+step] > 0 and (i, j+step) not in visited:
#         waitList.append((i,j+step))
#     if map[i+step][j-step] > 0 and (i+step, j-step) not in visited:
#         waitList.append((i+step,j-step))
#     if map[i+step][j] > 0 and (i+step, j) not in visited:
#         waitList.append((i+step,j))
#     if map[i+step][j+step] > 0 and (i+step, j+step) not in visited:
#         waitList.append((i+step,j+step))
#
#     bfs(copy.copy(waitList))
#
# bfs([init_point])




cv2.imshow("vessel", paint)
cv2.waitKey(0)