class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector" | int | float) -> "Vector":
        if isinstance(other, Vector):
            result_x = self.x * other.x 
            result_y = self.y * other.y
            return result_x + result_y
        return Vector(self.x * other, self.y * other)
