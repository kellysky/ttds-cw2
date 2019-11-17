import sys
# map=[]
# content_grid=[]
# parameter=sys.stdin.readline()
# #print(parameter)
# parameter=parameter.split()
# #print(para)
# num=0
# for i in range(0,int(parameter[0])):
#      temp_list=[]
#      for j in range(0,int(parameter[0])):
#         num=num+1
#         temp_list.append(num)
#      map.append(temp_list)
# print(map)
# new_map=[]
# for i in range(0,int(parameter[0])):
#     temp_list=[]
#     for j in range(0,int(parameter[0])):
#         num=map[j]
#         #print(num[i])
#         temp_list.append(num[i])
#     new_map.append(temp_list)
# print(new_map)
# circus_point=[int(parameter[1]),int(parameter[2])]
# circus_r=int(parameter[3])
#
# count=0
# flag=0
# position=[(circus_point[0]-circus_r),(circus_point[0]+circus_r),(circus_point[1]-circus_r),(circus_point[1]+circus_r)]
# for item in position:
#     if item >= 1 | item <=int(parameter[0]):
#         flag=1
#     elif item < 1| item > int(parameter[0]):
#         count=count+1

#
# print(position)
# print(map)

#
# if flag==0 & count<4:
#     print('not enter into map')
# else:
#     print('enter into map')
#
# if count==4:
#     content_grid=map
# else:
#     #print(len(map))
#     for i in range(0,int(parameter[0])):
#         #i=len(map)-1-i
#         for j in range(0,int(parameter[0])):
#             temp_list=[[i,j],[i+1,j],[i,j+1],[i+1,j+1]]
#             #print(temp_list)
#             num=0
#             flag=0
#             for item in temp_list:
#                 x=item[0]
#                 y=item[1]
#                 distance=(x-circus_point[0])*(x-circus_point[0])+(y-circus_point[1])*(y-circus_point[1])
#                 if distance < circus_r*circus_r:
#                     #print('distant')
#                     #print(distance)
#                     flag=1
#                     num=num+1
#             if flag==1:
#                 if num < 4:
#                     print(temp_list[0])
#                     content_grid.append(new_map[i][j])
#
# content_grid=sorted(content_grid)
# print(content_grid)
#
# if len(content_grid)==0:
#     print('-1')
#
#
#

from scipy import stats
import numpy as np
s3=[0.733,0.897,0.24,0.704,0.233,0.449,0,0.78,0.584,0.488]
s6=[0.719,0.759,0.24,0.652,0.233,0.449,0,0.722,0.641,0.488]
print(stats.ttest_rel(s3,s6))


#
# def findLCS(s1,s2):
#     m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
#     mmax = 0
#     p = 0
#     for i in range(len(s1)):
#         for j in range(len(s2)):
#             if s1[i] == s2[j]:
#                 m[i + 1][j + 1] = m[i][j] + 1
#                 if m[i + 1][j + 1] > mmax:
#                     mmax = m[i + 1][j + 1]
#                     p = i + 1
#     return s1[p - mmax:p], mmax
#
# print(findLCS('1234','234567'))
#
#
#
