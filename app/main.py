import math

class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y  # Dot product
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        x = round(end_point[0] - start_point[0], 2)
        y = round(end_point[1] - start_point[1], 2)
        return cls(x, y)

    def get_length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self):
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other):
        if isinstance(other, Vector):
            dot_product = self * other
            length_product = self.get_length() * other.get_length()
            cos_angle = dot_product / length_product
            cos_angle = max(min(cos_angle, 1), -1)  # Clamp cos_angle to avoid rounding errors
            angle_rad = math.acos(cos_angle)
            return round(math.degrees(angle_rad))
        return NotImplemented

    def get_angle(self):
        # Corrected angle calculation
        return round(math.degrees(math.atan2(-self.x, self.y)))

    def rotate(self, degrees):
        radians = math.radians(degrees)
        new_x = round(self.x * math.cos(radians) - self.y * math.sin(radians), 2)
        new_y = round(self.x * math.sin(radians) + self.y * math.cos(radians), 2)
        return Vector(new_x, new_y)
