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



    def create_vector_by_two_points(start_point: tuple, end_point: tuple) -> None:
        pass

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
isinstance(vector2, Vector)
vector2.x
vector2.y