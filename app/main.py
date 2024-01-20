#%%
from __future__ import annotations
import math


#%%
class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x,2)
        self.y = round(y,2)

    def __add__(self, other: "Vector"):
        if not isinstance(other, Vector):
            raise ValueError("Add Vector to Vector or go drink coffee")
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise ValueError ("Substract error")
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> None:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Something with numbers")


    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> 'Vector':
        x_diff = end_point[0] - start_point[0]
        y_diff = end_point[1] - start_point[1]
        return cls(round(x_diff,2), round(y_diff,2))

    def get_length(self) -> float:
        return math.sqrt(self.x **2 + self.y **2)
    
    def get_normalized(self) -> 'Vector':
        length = self.get_length()
        if length == 0:
            raise ValueError("Can't norm because of zero")
        return Vector(self.x / length, self.y / length)
    
    def angle_between (self, other: Vector) -> float:
        if not isinstance(other, Vector):
            raise ValueError("something wrong, drink coffee")

        dot_prod = self.x * other.x + self.y * other.y
        mag_self = self.get_length()
        mag_other = other.get_length()

        if mag_self == 0 or mag_other == 0:
            raise ValueError("Can't calculate  = zero ")

        cos_angle = dot_prod / (mag_self * mag_other)
        cos_angle = min(1, max(cos_angle, -1))
        angle_res = math.degrees(math.acos(cos_angle))
        return round(angle_res)

    def get_angle(self) -> float:
       
        # Calculate the angle in radians between the positive X-axis and the vector
        angle_radians = math.atan2(self.y, self.x)
        
        # Convert the angle to degrees
        angle_degrees = math.degrees(angle_radians)
        
        # Adjust the angle to measure it from the positive Y-axis, clockwise
        if self.x >= 0:
            # First or fourth quadrant
            angle_from_y = (90 - angle_degrees) % 360
        else:
            # Second or third quadrant
            angle_from_y = (90 - angle_degrees) % 360
        
        # Return the positive angle less than 360 degrees
        return angle_from_y if angle_from_y >= 0 else angle_from_y + 360
    
    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(new_x, new_y)
# %%
vector = Vector(2, 4)
vector.get_length()
# %%
