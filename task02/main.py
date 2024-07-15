import turtle


def main():
    screen = turtle.Screen()  # Create the screen.
    screen.setup(800, 600)  # Set Window size.
    draw_koch_curve(4)


def koch_curve(t, order, length):
    if order == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, order - 1, length)
        t.left(60)
        koch_curve(t, order - 1, length)
        t.right(120)
        koch_curve(t, order - 1, length)
        t.left(60)
        koch_curve(t, order - 1, length)


def draw_koch_curve(order, length=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, length)
        t.right(120)

    window.mainloop()


if __name__ == '__main__':
    main()
