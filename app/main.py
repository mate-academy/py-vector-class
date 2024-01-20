from __future__ import annotations
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


#%%


# %%
vector1 = Vector(2, 4)
vector2 = Vector(-1, 3)
vector3 = vector1 + vector2
#%%
isinstance(vector3, Vector)
#vector3.x
vector3.y
# %%
vector1 = Vector(2, 4)
vector2 = vector1 * 3.743
# %%
start_point = (5.2, 2.6)
end_point = (10.7, 6)
vector = Vector.create_vector_by_two_points(start_point, end_point)
# %%
isinstance(vector, Vector)
vector.x
vector.y