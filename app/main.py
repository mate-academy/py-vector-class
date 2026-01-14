import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        x_component = end_point[0] - start_point[0]
        y_component = end_point[1] - start_point[1]
        return cls(x_component, y_component)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        cos_angle = dot_product / (self.get_length() * other.get_length())
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)


# Example usage:
vector1 = Vector(2, 4)
vector2 = Vector(-1, 3)

# Addition
vector3 = vector1 + vector2
print(vector3.x, vector3.y)  # Output: 1 7

# Subtraction
vector4 = vector1 - vector2
print(vector4.x, vector4.y)  # Output: 3 1

# Multiplication by scalar
vector5 = vector1 * 3.743
print(vector5.x, vector5.y)  # Output: 7.49 14.97

# Dot product
dot_product = vector1 * vector2
print(dot_product)  # Output: 14

# Create vector by two points
start_point = (5.2, 2.6)
end_point = (10.7, 6)
vector6 = Vector.create_vector_by_two_points(start_point, end_point)
print(vector6.x, vector6.y)  # Output: 5.5 3.4

# Length
vector7 = Vector(2, 4)
print(vector7.get_length())

# Normalized vector
vector8 = Vector(13, -4)
normalized_vector = vector8.get_normalized()
print(normalized_vector.x, normalized_vector.y)

# Angle between vectors
vector9 = Vector(13, -4)
vector10 = Vector(-6, -11)
print(vector9.angle_between(vector10))

# Angle with positive Y axis
vector11 = Vector(33, 8)
print(vector11.get_angle())

# Rotate vector
vector12 = Vector(33, 8)
vector13 = vector12.rotate(45)
print(vector13.x, vector13.y)
