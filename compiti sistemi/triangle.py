def triangle(l1, l2, l3):

    if l1 <= 0 or l2 <= 0 or l3 <= 0:
        return "It is not a triangle (side <= 0)"

    elif l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
        return "It is not a triangle"

    elif l1 + l2 - l3 == 0 or l1 + l3 - l2 == 0 or l2 + l3 - l1 == 0:
        return "Degenerate triangle"

    elif l1 == l2 and l2 == l3:
        return "Triangle equilateral"
    
    elif l1 != l2 and l1 != l3 and l2 != l3:
        return "Triangle scalene"

    elif l1 == l2 or l1 == l3 or l2 == l3:
        return "Triangle isosceles"

print(triangle(5, 2, 3))