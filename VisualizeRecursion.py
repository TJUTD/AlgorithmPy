import turtle



def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len-5)

# my_turtle = turtle.Turtle()
# my_win = turtle.Screen()
# draw_spiral(my_turtle, 100)
# my_win.exitonclick()

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len-10, t)
        t.left(40)
        tree(branch_len-10, t)
        t.right(20)
        t.backward(branch_len)

my_turtle = turtle.Turtle()
my_win = turtle.Screen()
my_turtle.left(90)
my_turtle.up()
my_turtle.backward(100)
my_turtle.down()
my_turtle.color("green")
tree(75, my_turtle)
my_win.exitonclick()