class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return self.x * other, self.y * other



v1 = Vector(2, 6)
v2 = 6
v3 = v1 * v2
print(v3)

# ```
# Multiplying Vector on Vector should return their dot product.
# ```python
# vector1 = Vector(2.11, 4.55)
# vector2 = Vector(-3.51, 10.33)
# dot_product = vector1 * vector2
# dot_product == 39.5954
