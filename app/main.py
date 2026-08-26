import math


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        # Round the coordinates to two decimal places
        self.x = round(x, 2)  # noqa: VNE001
        self.y = round(y, 2)  # noqa: VNE001

    def __add__(self, other: "Vector") -> "Vector":
        # Add two vectors component-wise
        return Vector(self.x + other.x, self.y + other.y)  # noqa: VNE001

    def __sub__(self, other: "Vector") -> "Vector":
        # Subtract two vectors component-wise
        return Vector(self.x - other.x, self.y - other.y)  # noqa: VNE001

    def __mul__(self, other: float or "Vector") -> "Vector" or float:
        if isinstance(other, (int, float)):
            # Scalar multiplication: multiply each component by the scalar
            return Vector(self.x * other, self.y * other)  # noqa: VNE001
        elif isinstance(other, Vector):
            # Dot product: sum of the products of the components
            return self.x * other.x + self.y * other.y  # noqa: VNE001
        else:
            raise TypeError("Unsupported operand type for multiplication")

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        # Calculate the vector from two points
        x = end_point[0] - start_point[0]  # noqa: VNE001
        y = end_point[1] - start_point[1]  # noqa: VNE001
        return cls(x, y)  # noqa: VNE001

    def get_length(self) -> float:
        # Calculate the length of the vector using the Pythagorean theorem
        return math.hypot(self.x, self.y)  # noqa: VNE001

    def get_normalized(self) -> "Vector":
        # Normalize the vector by dividing each component by its length
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)  # noqa: VNE001
        return Vector(self.x / length, self.y / length)  # noqa: VNE001

    def angle_between(self, other: "Vector") -> int:
        # Calculate the angle between two vectors using the dot product formula
        dot_product = self * other
        magnitude_product = self.get_length() * other.get_length()
        if magnitude_product == 0:
            return 0
        cos_a = dot_product / magnitude_product
        # Clamp cos_a to avoid floating-point inaccuracies
        cos_a = max(-1, min(1, cos_a))
        angle_radians = math.acos(cos_a)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        # Calculate the angle between the vector and the positive Y-axis
        # The positive Y-axis is represented by the vector (0, 1)
        y_axis = Vector(0, 1)  # noqa: VNE001
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        # Rotate the vector by the given degrees
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        x_rotated = self.x * cos_a - self.y * sin_a  # noqa: VNE001
        y_rotated = self.x * sin_a + self.y * cos_a  # noqa: VNE001
        return Vector(x_rotated, y_rotated)  # noqa: VNE001
