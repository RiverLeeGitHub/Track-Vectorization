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
cv2.circle(paint, (init_point[1],init_point[0]), 6, (0,0,255), -1)
# cv2.imshow("vessel", paint)
# cv2.waitKey(0)





def distance(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2


# 1. Generate octagon centered on the initial point
def octagon(center, radius):
    """
    Generate octagon centered on the initial point
    :param center: point in the i-th row and j-th column
    :param radius:
    :return: a list of points in the octagon margin
    """
    ci, cj = center[0], center[1]
    r = radius
    points = []

    i = int(ci - r)
    j = int(cj - r/2.0)
    while j > cj - r:
        points.append((i,j))
        i += 1
        j -= 1
    while i < ci + r/2.0:
        points.append((i,j))
        i += 1
    while j < cj - r/2.0:
        points.append((i,j))
        i += 1
        j += 1
    while j < cj + r/2.0:
        points.append((i,j))
        j += 1
    while j < cj + r:
        points.append((i,j))
        i -= 1
        j += 1
    while i > ci - r/2.0:
        points.append((i,j))
        i -= 1
    while j > cj + r/2.0:
        points.append((i,j))
        i -= 1
        j -= 1
    while j > cj - r/2.0:
        points.append((i,j))
        j -= 1
    return points

# 2. Detect the center point of each trajectory on the margin, and get the directions of each trajectory
def get_directions(img, margin, visited):
    state_count = []

    for i in range(len(margin)):
        if img[margin[i][0]][margin[i][1]] > 0 and visited[margin[i][0]][margin[i][1]] == 0:
            state = 1 # has trajectory
        else:
            state = 0
        if len(state_count) == 0:
            state_count.append([state, i, 1]) # state is 1 and count is 1, with continuous state starting from index i
        else:
            if state_count[-1][0] == state: # if the state is the same as previous one, count++
                state_count[-1][2] += 1
            else:
                state_count.append([state, i, 1])
    continuous_state_middle_indices = set()
    for i in range(1, len(state_count)):
        [state, index, length] = state_count[i]
        if state == 1:
            continuous_state_middle_indices.add(index+length//2)
    if state_count[0][0] == state_count[-1][0] == 1:
        [state, index, length] = state_count[-1]
        length += state_count[0][2]
        mid_index = (index+length//2)%len(margin)
        continuous_state_middle_indices.add(mid_index)
    else:
        [state, index, length] = state_count[0]
        if state == 1:
            continuous_state_middle_indices.add(index+length//2)
        [state, index, length] = state_count[-1]
        if state == 1:
            continuous_state_middle_indices.add(index+length//2)
    return sorted(list(continuous_state_middle_indices))

def set_visited(visited, center, margin):
    left_points = margin[:len(margin)//3+1]
    for l in left_points:
        i = l[0]
        for j in range(l[1],l[1]+(center[1]-l[1])*2):
            visited[i][j] = 255
            # paint[i][j][2] = 255
    return visited



# ?. Determine the unique connected area that contains this center point in the octagon
def connected_area(img, center, margin):
    """
    Determine the unique connected area that contains this center point in the octagon
    :param img: 2 dimensions numpy array, binary image, object in white
    :param margin: a list of points in the octagon margin
    :return:
    """
    min_i, min_j, max_i, max_j = float('inf'), float('inf'), -float('inf'), -float('inf')
    for x in margin:
        i, j = x[0], x[1]
        min_i = min(min_i, i)
        min_j = min(min_j, j)
        max_i = max(max_i, i)
        max_j = max(max_j, j)
    min_i = max(min_i, 0)
    min_j = max(min_j, 0)
    max_i = min(max_i, len(img)-1)
    max_j = min(max_j, len(img[0])-1)


    bfs_waitlist = [center]
    visited = set()
    while len(bfs_waitlist) > 0:
        print(bfs_waitlist[0])
        if bfs_waitlist[0] in visited:
            bfs_waitlist.pop(0)
            continue
        i, j = bfs_waitlist[0][0], bfs_waitlist[0][1]
        if (not (min_i<=i<=max_i and min_j<=j<max_j)) or img[i][j] == 0:
            bfs_waitlist.pop(0)
            continue
        visited.add(bfs_waitlist[0])
        bfs_waitlist += [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        bfs_waitlist.pop(0)

        # paint[i][j][0],paint[i][j][1],paint[i][j][2] = 0,0,255

        cv2.imshow("vessel", paint)
        cv2.waitKey(1)

    return visited



init_point = (700, 230)

wait_list = [init_point]
while len(wait_list) > 0:
    point = wait_list[0]
    margin = octagon(center= point, radius= 15)
    # for i in range(len(margin)):
    #     cv2.circle(paint, (margin[i][1], margin[i][0]), 2, (255, 0, 0), 1)
    # print(connected_area(map, (700,230), margin))
    directions = get_directions(map, margin, visited)
    for d in directions:
        [i,j] = margin[d][0], margin[d][1]
        cv2.line(paint, (point[1],point[0]), (j, i), (0, 255, 0), 3)

    visited = set_visited(visited, point, margin)

    wait_list += [margin[d] for d in directions]
    # print(wait_list)
    wait_list.pop(0)

    cv2.imshow("vessel", paint)
    cv2.waitKey(0)


















