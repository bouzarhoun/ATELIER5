class Point:

        def __init__(self, x=0.0, y=0.0):
                self.x = x
                self.y = y

class Segment:
        def __init__(self, x1, y1, x2, y2):
                self.origin = Point(x1, y1)
                self.extreme = Point(x2, y2)

        def __str__(self):
                return ("Segment : [(%.1f, %.1f), (%.1f, %.1f)]" %(self.origin.x, self.origin.y, self.extreme.x, self.extreme.y))

s = Segment(1, 2, 3, 4)
print(s)