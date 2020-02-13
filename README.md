# Track-Vectorization

#### Introduction

When doing image processing in specific field like medical image, we not only need to know the pixel-wise information of an image, but also need to get the structure of it to solve higher level problem. Most complex structure has its tracks, and it's rather useful to extract them by vectorization and provide more information in image analysis.

#### Procedure

1. Given a point as the center, and its radius, it generates octagon centered on this point and generates a list of points of the edges of this octagon.

![1_1](https://github.com/RiverLeeGitHub/Track-Vectorization/blob/master/Explaination/1_1.png)

2. Detect the center point of each trajectory on the margin, and get the directions of each trajectory.

   ![image-20200213002059795](https://github.com/RiverLeeGitHub/Track-Vectorization/blob/master/Explaination/2_1.png)

3. Set the octagon region as visited.

   ![image-20200213003515476](https://github.com/RiverLeeGitHub/Track-Vectorization/blob/master/Explaination/3_1.png)

4. Do the expansion recursively of the points in margin.

   ![image-20200213010622841](https://github.com/RiverLeeGitHub/Track-Vectorization/blob/master/Explaination/result.png)



