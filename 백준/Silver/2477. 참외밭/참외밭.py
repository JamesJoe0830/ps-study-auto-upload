import sys
from collections import deque
input = sys.stdin.readline
melon = int(input())
arr = []
x,y = 0,0
except_x,except_y = 0,0
for i in range(6):
  direction, len = map(int,input().split())
  arr.append((direction,len))
  if direction == 3 or direction == 4:
    y = max(y,len)
  elif direction == 1 or direction == 2:
    x = max(x,len)
arr = deque(arr)
start_index = 0
start_axis = ''
for i in range(-1,5):
  direction = arr[i][0]
  length = arr[i][1]
  if direction == 1 or direction == 2:
    if length == x and arr[i+1][1] == y:
      start_index = i
      start_axis = 'x'
      break
  elif direction == 3 or direction == 4:
    if length == y and arr[i+1][1] == x:
      start_index = i
      start_axis = 'y'
      break
arr.rotate(-start_index)
if start_axis == 'x':
  cnt_x = 0
  cnt_y = 0
  for direction, length in arr:
    if direction == 1 or direction == 2:
      if length < x :
        cnt_x +=1 
      if cnt_x == 2:
        except_x = length
    elif direction == 3 or direction == 4:
      if length < y :
        cnt_y +=1 
      if cnt_y == 1:
        except_y = length
else : 
  cnt_x = 0
  cnt_y = 0
  for direction, length in arr:
    if direction == 1 or direction == 2:
      if length < x :
        cnt_x +=1 
      if cnt_x == 1:
        except_x = length
    elif direction == 3 or direction == 4:
      if length < y :
        cnt_y +=1 
      if cnt_y == 2:
        except_y = length
print((x*y-except_x*except_y)*melon)

