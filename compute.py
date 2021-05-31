class polygons:
    def __init__(self, number, name, area):
        self.number = number
        self.name = name
        self.area = area
        print(number,'-',name,'with area size',area)
info = [
            {"type": "Square", "area": 150.5},
            {"type": "Rectangle", "area": 80},
            {"type": "Rectangle", "area": 660},
            {"type": "Circle", "area": 68.2},
            {"type": "Triangle", "area": 20}
        ]
number=1
for z in info:
    polygons(str(number), z["type"], z["area"])
    number+=1
