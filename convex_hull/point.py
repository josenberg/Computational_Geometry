def most_left(points):
  most_left_point = points[0]
  min_x = most_left_point.x
  for p in points[1:]:
    if p.x < min_x:
      min_x = p.x
      most_left_point = p
  return most_left_point; 

def most_right(points):
  most_right_point = points[0]
  max_x = most_right_point.x
  for p in points[1:]:
    if p.x > max_x:
      max_x = p.x
      most_right_point = p
  return most_right_point; 

def most_bottom(points):
  most_bottom_point = points[0]
  min_y = start.y
  for p in points[1:]:
    if p.y < min_y:
      min_y = p.y
      most_bottom_point = p
  return most_bottom_point; 

def most_top(points):
  most_top_point = points[0]
  max_y = start.y
  for p in points[1:]:
    if p.y > max_y:
      max_y = p.y
      most_top_point = p
  return most_top_point; 


