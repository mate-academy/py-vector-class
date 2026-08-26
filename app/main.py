import math


class Vector:
    def __init__(self, v_x: int | float, v_y: int | float) -> None:
        self.x = round(v_x, 2)
        self.y = round(v_y, 2)

    def __add__(self, other: "Vector") -> "Vector":

        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":

        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | object) -> int | float | object:

        if isinstance(other, Vector):
            scal_x = self.x * other.x
            scal_y = self.y * other.y

            return scal_x + scal_y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point:
                                    tuple[int | float,
                                          int | float],
                                    end_point:
                                    tuple[int | float,
                                          int | float]) -> "Vector":
        point_x = end_point[0] - start_point[0]

        point_y = end_point[1] - start_point[1]

        return cls(point_x, point_y)

    def get_length(self) -> int | float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":

        length = self.get_length()

        return Vector(self.x / length, self.y / length)

    def angle_between_raw(self, other: "Vector") -> float:
        scal_vector = self * other

        a_length = self.get_length()

        b_length = other.get_length()

        res_length = a_length * b_length

        cos_a = 0

        if res_length > 0 or scal_vector > 0:
            cos_a = scal_vector / res_length

            return math.degrees(math.acos(cos_a))

        return 0

    def angle_between(self, other: "Vector") -> int:
        return round(self.angle_between_raw(other))

    def get_angle(self) -> int:

        return self.angle_between(Vector(0, abs(self.x)))

    def rotate(self, degree: int | float) -> "Vector":

        radiant = math.radians(degree)

        vec_length = self.get_length()

        x_angle = self.angle_between_raw(Vector(vec_length, 0))

        if self.x < 0 or self.y < 0:
            x_angle = -x_angle

        alpha_radiant = math.radians(x_angle)

        vec_x = vec_length * math.cos(alpha_radiant + radiant)

        vec_y = vec_length * math.sin(alpha_radiant + radiant)

        return Vector(vec_x, vec_y)
