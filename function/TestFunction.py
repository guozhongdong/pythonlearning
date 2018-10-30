import math

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

# ax2 + bx + c = 0
def quadratic(a,b,c):
    if a == 0:
        print("该方程不是一个一元二次方程！")
        n = (-c)/b
        return n
    else:
        delta = b*b - 4*a*c
        if delta > 0:
            print("该方程有两个解！")
            n1 = math.sqrt(delta)
            x1 = ((-b)+n1)/2*a
            x2 = ((-b)-n1)/2*a
            return x1,x2
        elif delta == 0:
            print("该方程有一个解！")
            x = (-b)/2*a
            return x
        else:
            print("该方程无解！")

print(quadratic(1,2,1))