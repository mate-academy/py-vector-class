from __future__ import annotations
#%%
class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x,2)
        self.y = round(y,2)

    def __add__(self, other: 'Vector'):
        if not isinstance(other, Vector):
            raise ValueError("Add Vector to Vector or go drink coffee")
        return Vector(self.x + other.x, self.y + other.y)

    def create_vector_by_two_points(start_point: tuple, end_point: tuple) -> None:
        pass
#%%
vector = Vector(-2.343, 8.008)

# %%
vector.x
vector.y