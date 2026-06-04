import math


class Vector:
    def __init__(self, coord_x: int | float, coord_y: int | float) -> None:
        self.x: float = round(float(coord_x), 2)
        self.y: float = round(float(coord_y), 2)

    def __repr__(self) -> str:
        return f"Vector({self.x:.2f}, {self.y:.2f})"

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            coord_x=self.x + other.x,
            coord_y=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            coord_x=self.x - other.x,
            coord_y=self.y - other.y,
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        if isinstance(other, (int, float)):
            return Vector(
                coord_x=self.x * other,
                coord_y=self.y * other,
            )

        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[int | float, int | float],
        end_point: tuple[int | float, int | float],
    ) -> Vector:
        return cls(
            coord_x=end_point[0] - start_point[0],
            coord_y=end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        vector_length: float = self.get_length()

        if vector_length == 0:
            raise ValueError("Cannot normalize zero vector")

        return Vector(
            coord_x=self.x / vector_length,
            coord_y=self.y / vector_length,
        )

    def angle_between(self, vector: Vector) -> int:
        self_length: float = self.get_length()
        vector_length: float = vector.get_length()

        if self_length == 0 or vector_length == 0:
            raise ValueError("Angle with zero vector is undefined")

        dot_product: float = self * vector

        cosine: float = dot_product / (self_length * vector_length)

        cosine = max(-1.0, min(1.0, cosine))

        return round(math.degrees(math.acos(cosine)))

    def get_angle(self) -> int:
        vector: Vector = Vector(0, 1)
        return self.angle_between(vector)

    def rotate(self, degrees: int) -> Vector:
        radians: float = math.radians(degrees)

        new_x: float = self.x * math.cos(radians) - self.y * math.sin(radians)

        new_y: float = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(
            coord_x=new_x,
            coord_y=new_y,
        )
