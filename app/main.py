# Create from two points
v = Vector.create_vector_by_two_points((5.2, 2.6), (10.7, 6))
assert isinstance(v, Vector)
assert v.x == 5.5
assert v.y == 3.4

# Get length
v = Vector(2, 4)
assert round(v.get_length(), 5) == 4.47214

# Normalize
v1 = Vector(13, -4)
v2 = v1.get_normalized()
assert round(v2.get_length(), 1) == 1.0
assert v2.x == 0.96
assert v2.y == -0.29

# Angle between
v1 = Vector(13, -4)
v2 = Vector(-6, -11)
assert v1.angle_between(v2) == 102

# Get angle with positive Y-axis
v = Vector(33, 8)
assert v.get_angle() == 76

# Rotate
v = Vector(33, 8)
v_rotated = v.rotate(45)
assert v_rotated.x == 17.68
assert v_rotated.y == 28.99
