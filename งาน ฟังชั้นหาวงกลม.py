def calculated_circle(radius):
    pi = 22/7
    area = pi*(radius**2)
    return area

radius = float(input("รัศมี : "))
area = calculated_circle(radius)

print(f"พื้นที่ของวงกลม : {area:.2f}")