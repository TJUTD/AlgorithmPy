import turtle



def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len-5)

def f1():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    draw_spiral(my_turtle, 100)
    my_win.exitonclick()

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len-10, t)
        t.left(40)
        tree(branch_len-10, t)
        t.right(20)
        t.backward(branch_len)

def f2():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(100)
    my_turtle.down()
    my_turtle.color("green")
    tree(75, my_turtle)
    my_win.exitonclick()

def draw_triangle(points, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()

def get_mid(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def sierpinski(points, degree, t):
    color_map = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, color_map[degree], t)
    if degree > 0:
        sierpinski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree-1, t)
        sierpinski([points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])], degree - 1, t)
        sierpinski([points[2], get_mid(points[1], points[2]), get_mid(points[0], points[2])], degree - 1, t)

def f3():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-200,-100], [0,200], [200,-100]]
    sierpinski(my_points, 5, my_turtle)
    my_win.exitonclick()

# f1()
# f2()
# f3()

def move_tower(height, from_pole, to_pole, aux_pole):
    if height >= 1:
        move_tower(height-1, from_pole, aux_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, aux_pole, to_pole, from_pole)

def move_disk(fp, tp):
    print("Move disk from", fp, "to", tp)

def TowerOfHanoi(n , from_pole, to_pole, aux_pole):
    if n == 1:
        print("Move disk 1 from", from_pole, "to", to_pole)
        return
    TowerOfHanoi(n-1, from_pole, aux_pole, to_pole)
    print("Move disk", n,"from", from_pole, "to", to_pole)
    TowerOfHanoi(n-1, aux_pole, to_pole, from_pole)

move_tower(3, "A", "B", "C")
TowerOfHanoi(3, "A", "B", "C")

