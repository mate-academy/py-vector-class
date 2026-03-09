class Vector:
    def __init__(self, point_x: int | float, point_y: int | float) -> None:
        self.point_x = round(point_x, 2)
        self.point_y = round(point_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        point_x = self.point_x + other.point_x
        point_y = self.point_y + other.point_y
        return Vector(point_x, point_y)

    def __sub__(self, other: "Vector") -> "Vector":
        point_x = self.point_x - other.point_x
        point_y = self.point_y - other.point_y
        return Vector(point_x, point_y)

    def __mul__(self, other: "Vector | float | int") -> "Vector | float | int":
        if isinstance(other, (int, float)):
            return Vector(self.point_x * other, self.point_y * other)
        elif isinstance(other, Vector):
            return self.point_x * other.point_x + self.point_y * other.point_y
        else:
            raise TypeError("Unsupported type for multiplication")

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: int | float,
            end_point: int | float) -> "Vector":
        point_x = end_point[0] - start_point[0]
        point_y = end_point[1] - start_point[1]
        return cls(point_x, point_y)
