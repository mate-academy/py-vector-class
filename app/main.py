import math


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        vax = self.x + other.x
        vay = self.y + other.y
        return Vector(vax, vay)

    def __sub__(self, other):
        vsx = self.x - other.x
        vsy = self.y - other.y
        return Vector(vsx, vsy)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            vmx = self.x * other
            vmy = self.y * other
            return Vector(vmx, vmy)
        else:
            vmv = self.x * other.x + self.y * other.y
            return vmv

    def create_vector_by_two_points(start_point, end_point):
        vx = end_point[0] - start_point[0]
        vy = end_point[1] - start_point[1]
        return Vector(vx, vy)

    def get_length(self):
        lenv = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        return lenv

    def get_normalized(self):
        x = self.x / self.get_length()
        y = self.y / self.get_length()
        return Vector(x, y)

    def angle_between(vec1, vec2):
        scalar = vec1.x * vec2.x + vec1.y * vec2.y
        modul1 = Vector.get_length(vec1)
        modul2 = Vector.get_length(vec2)
        corner = scalar / (modul1 * modul2)
        return round(math.degrees(math.acos(corner)))

    def get_angle(self):
        ve = Vector(0, 1)
        yaxis = ve.angle_between(self)
        return yaxis

    def rotate(self, degrees):
        xnew = math.cos(
            math.radians(degrees)
        ) * self.x - math.sin(math.radians(degrees)) * self.y
        ynew = math.sin(
            math.radians(degrees)
        ) * self.x + math.cos(math.radians(degrees)) * self.y
        return Vector(xnew, ynew)
