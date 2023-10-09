# bounce.py
#
# Exercise 1.5
height = 100
drop_height= height * 0.6
num_bounce = 1 


while drop_height > 1:
  print(num_bounce, round(drop_height, ndigits=4))
  num_bounce = num_bounce + 1
  drop_height = drop_height * 0.6

print('Number of bounces', num_bounce)
print('Final air', round(drop_height)) 
