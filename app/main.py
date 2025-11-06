import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector | float") -> "Vector | float":
        """Scalar multiplication or dot product."""
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError(
            f"Cannot multiply Vector by {type(other).__name__}"
        )

    def __rmul__(self, other: float) -> "Vector":
        """Support scalar * vector."""
        return self.__mul__(other)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple | list | object,
        end_point: tuple | list | object
    ) -> "Vector":
        """Create a vector from start_point to end_point."""
        def extract_coords(
            point: tuple | list | object,
            name: str
        ) -> tuple[float, float]:
            if hasattr(point, "x") and hasattr(point, "y"):
                return float(point.x), float(point.y)
            elif isinstance(point, (tuple, list)):
                try:
                    coord_x, coord_y = point
                    return float(coord_x), float(coord_y)
                except (TypeError, ValueError):
                    raise TypeError(
                        f"{name} must be a tuple, list, or object with x and y"
                    )
            else:
                raise TypeError(
                    f"{name} must be a tuple, list, or object with x and y"
                )

        start_x, start_y = extract_coords(start_point, "start_point")
        end_x, end_y = extract_coords(end_point, "end_point")

        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        """Return the magnitude (length) of the vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        """Return a unit vector in the same direction."""
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        """Return the angle in degrees between this vector and another."""
        dot = self.x * other.x + self.y * other.y
        len_self = self.get_length()
        len_other = other.get_length()

        if len_self == 0 or len_other == 0:
            raise ValueError("Cannot compute angle with zero vector")

        cos_a = dot / (len_self * len_other)
        cos_a = max(-1.0, min(1.0, cos_a))
        angle_deg = math.degrees(math.acos(cos_a))
        return int(round(angle_deg))

    def get_angle(self) -> int:
        """Return angle in degrees from positive y-axis (0-359), clockwise."""
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        angle_norm = int(round((angle_deg + 360) % 360))
        return angle_norm

    def rotate(self, degrees: float) -> "Vector":
        """Return a new vector rotated counterclockwise by given degrees."""
        rad = math.radians(degrees)
        cos_r = math.cos(rad)
        sin_r = math.sin(rad)
        return Vector(
            self.x * cos_r - self.y * sin_r,
            self.x * sin_r + self.y * cos_r
        )


def create_vector_by_two_points(
    start_point: tuple | list | object,
    end_point: tuple | list | object
) -> Vector:
    """Create a vector from start_point to end_point."""
    return Vector.create_vector_by_two_points(start_point, end_point)


if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 0)

    print(f"v1: {v1}, length: {v1.get_length()}")
    print(f"v1 + v2: {v1 + v2}")
    print(f"v1 * 2: {v1 * 2}")
    print(f"v1 · v2 (dot product): {v1 * v2}")
    print(f"Angle between v1 and v2: {v1.angle_between(v2)}°")
    print(f"v1 angle from y-axis: {v1.get_angle()}°")
    print(f"v1 rotated 90°: {v1.rotate(90)}")
