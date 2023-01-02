from __future__ import annotations
import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: tuple) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: tuple) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: tuple) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x=self.x * other,
            y=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        x_coordinate = (end_point[0]) - (start_point[0])
        y_coordinate = (end_point[1]) - (start_point[1])
        return Vector(
            x=x_coordinate,
            y=y_coordinate
        )

    def get_length(self) -> float:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return length

    def get_normalized(self) -> Vector:
        unit_vector = self.get_length()
        result_normalized_vector = Vector(
            x=round(self.x / unit_vector, 2),
            y=round(self.y / unit_vector, 2)
        )
        return result_normalized_vector

    def angle_between(self, other: Vector) -> int:
        dot_product_of_vectors = self.x * other.x + self.y * other.y
        angle_between = math.degrees(
            math.acos(
                dot_product_of_vectors / (self.get_length() * other.get_length())
            )
        )
        return round(angle_between)

    def get_angle(self) -> int:
        default_y_vector = Vector(0, 10)
        return default_y_vector.angle_between(self)

    def rotate(self, degrees: int) -> Vector:
        rotated_x = (
            math.cos(math.radians(degrees)) * self.x
            - math.sin(math.radians(degrees)) * self.y)
        rotated_y = (
            math.sin(math.radians(degrees)) * self.x
            + math.cos(math.radians(degrees)) * self.y)
        return Vector(
            x=rotated_x,
            y=rotated_y
        )

#################################################
class RockBand:

    def __init__(self, name: str, members: list) -> None:
        self.name = name
        self.members = members

    def add_new_member(self, new_member: str) -> None:
        if new_member in self.members:
            print(f"{new_member} is already in the band!")
        else:
            return self.members.append(new_member)

    def __add__(self, other: None) -> None:
        united_bands = RockBand(
            name=f"{self.name} {other.name} United",
            members=self.members + other.members
        )
        updated_members = []
        for band_member in united_bands.members:
            if band_member not in updated_members:
                updated_members.append(band_member)
        united_bands.members = updated_members
        return united_bands
