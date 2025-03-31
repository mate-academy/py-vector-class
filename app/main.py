import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError("Unsupported operand type for *")

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length1 = self.get_length()
        length2 = other.get_length()
        if length1 == 0 or length2 == 0:
            return 0
        cosine_angle = dot_product / (length1 * length2)
        return round(math.degrees(math.acos(cosine_angle)))

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.y, self.x)  # Кут відносно осі OX
        angle_degrees = round(math.degrees(angle_radians))  # В градуси

        # Коригуємо так, щоб 0° був на осі OY вгору
        corrected_angle = (90 - angle_degrees) % 360

        # Повертаємо лише додатні кути у діапазоні [0, 180]
        if corrected_angle > 180:
            corrected_angle = 360 - corrected_angle

        return corrected_angle

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_val = math.cos(radians)
        sin_val = math.sin(radians)
        new_x = self.x * cos_val - self.y * sin_val
        new_y = self.x * sin_val + self.y * cos_val
        return Vector(new_x, new_y)
