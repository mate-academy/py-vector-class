import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=round(self.x + other.x, 2),
            y_coord=round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=round(self.x - other.x, 2),
            y_coord=round(self.y - other.y, 2)
        )

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(
                x_coord=round(self.x * other, 2),
                y_coord=round(self.y * other, 2)
            )
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        return Vector(
            x_coord=self.x / self.get_length(),
            y_coord=self.y / self.get_length()
        )

    def angle_between(self, vector: Vector) -> float:
        scalar = (self.x * vector.x) + (self.y * vector.y)
        sub_length = self.get_length() * vector.get_length()
        return round(math.degrees(math.acos(scalar / sub_length)))

    def get_angle(self) -> float:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: float) -> Vector:
        rad = math.radians(degrees)
        return Vector(
            x_coord=round((self.x * math.cos(rad))
                          - (self.y * math.sin(rad)), 2),
            y_coord=round((self.x * math.sin(rad))
                          + (self.y * math.cos(rad)), 2)
        )
