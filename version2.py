"""
Uses recursive function to expand the maximum distance in a direction
Optimized codes
Uses image as visited sets

"""

import cv2
import copy
import numpy as np

vessel = cv2.imread("vessel.png")
paint = vessel.copy()

print(paint.shape)

map = vessel[:,:,0]
visited = np.zeros_like(map)
ret,map=cv2.threshold(map,100,255,cv2.THRESH_BINARY)

# # Find the initial point
# init_point = None
# for i in range(0, len(map)):
#     for j in range(0, len(map[0]), 2):
#         if map[i][j] > 0:
#             cv2.circle(paint, (j,i), 1, (255,0,0), 1)
#             init_point = [i, j]
#             print(init_point)

init_point = (700, 230)
print(init_point)
cv2.circle(paint, (init_point[1],init_point[0]), 10, (255,0,0), 2)
cv2.imshow("vessel", paint)
cv2.waitKey(0)

def distance(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

step = 1
# visited = set()
father = dict()
waitList = [init_point]
father[init_point] = init_point
while len(waitList) > 0:

    print(waitList)
    i, j = waitList[0][0], waitList[0][1]

    # if waitList[0] in visited:
    #     waitList.pop(0)
    #     continue

    # visited.add(waitList[0])
    paint[i][j] = (0, 0, 255)
    # cv2.circle(paint, (j,i), 3, (0, 255, 0), 2)
    if not waitList[0] in father:
        waitList.pop(0)
        continue
    father_i, father_j = father[waitList[0]][0], father[waitList[0]][1]
    cv2.line(paint, (father_j,father_i), (j,i), (0,255,0), 2)

    unit_vector = ((i-father_i)/(i**2+father_i**2)**0.5,(j-father_j)/(j**2+father_j**2)**0.5)
    # cv2.line(visited, (int(father_j+20*unit_vector[1]),int(father_i+20*unit_vector[0])), (j,i), (255,255,255), 3)
    cv2.line(visited, (father_j,father_i), (j,i), (255,255,255), 1)

    # cv2.circle(visited, (father_j, father_i), 3, (0, 0, 0), -1)
    # cv2.circle(visited, (j, i), 3, (0, 0, 0), -1)

    del father[waitList[0]]

    cv2.imshow("vessel", paint)
    # cv2.imshow("vessel", visited)
    cv2.waitKey(1)

    branch = 0

    def expand(i, j, di, dj):
        if visited[i+di][j+dj] > 0:
            # print("********************")
            return None
        if not (0 <= i+di < len(map) and 0<= j+dj <len(map[0])):
            return None
        if map[i+di][j+dj] > 0 and visited[i+di][j+dj] == 0:
            # visited.add((i+di,j+dj))
            return expand(i+di, j+dj, di, dj)
        else:
            return (i, j)


    for direction in [(-step, -step), (-step, 0), (-step, step), (0, -step), (0, step), (step, -step), (step, 0), (step, step)]:
        print(direction)
        end = expand(i, j, direction[0], direction[1])
        if end != None and end != (i, j):
            if distance(i,j,end[0],end[1]) < 10:
                continue
            father[end] = (i, j)
            waitList.append(end)
            branch += 1


    # end1 = expand(i, j, -step, -step)
    # if end1 != None and end1 != (i,j):
    #     father[end1] = (i,j)
    #     waitList.append(end1)
    #     branch += 1
    # end2 = expand(i, j, -step, 0)
    # if end2 != None and end2 != (i,j):
    #     father[end2] = (i,j)
    #     waitList.append(end2)
    #     branch += 1
    # end3 = expand(i, j, -step, step)
    # if end3 != None and end3 != (i,j):
    #     father[end3] = (i,j)
    #     waitList.append(end3)
    #     branch += 1
    # end4 = expand(i, j, 0, -step)
    # if end4 != None and end4 != (i,j):
    #     father[end4] = (i,j)
    #     waitList.append(end4)
    #     branch += 1
    # end5 = expand(i, j, 0, step)
    # if end5 != None and end5 != (i,j):
    #     father[end5] = (i,j)
    #     waitList.append(end5)
    #     branch += 1
    # end6 = expand(i, j, step, -step)
    # if end6 != None and end6 != (i,j):
    #     father[end6] = (i,j)
    #     waitList.append(end6)
    #     branch += 1
    # end7 = expand(i, j, step, 0)
    # if end7 != None and end7 != (i,j):
    #     father[end7] = (i,j)
    #     waitList.append(end7)
    #     branch += 1
    # end8 = expand(i, j, step, +step)
    # if end8 != None and end8 != (i,j):
    #     father[end8] = (i,j)
    #     waitList.append(end8)
    #     branch += 1
    print(branch)
    # if branch > 5:
    #     cv2.circle(paint, (j, i), 3, (0, 0, 255), 2)

    waitList.pop(0)








cv2.imshow("vessel", paint)
cv2.waitKey(0)