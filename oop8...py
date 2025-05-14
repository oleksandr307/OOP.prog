import turtle
from datetime import datetime

class Digit:
    def __init__(self, turtle_obj, angle, radius, text):
        self.t = turtle_obj
        self.angle = angle
        self.radius = radius
        self.text = text
    def draw(self):
        self.t.penup()
        self.t.goto(0, 0)
        self.t.setheading(90 - self.angle)
        self.t.forward(self.radius)
        self.t.write(self.text, align="center", font=("Arial", 14, "normal"))

class ClockFace:
    def __init__(self, radius=200):
        self.radius = radius
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
    def draw(self):
        self.t.penup()
        self.t.goto(0, -self.radius)
        self.t.pendown()
        self.t.circle(self.radius)
        for i in range(12):
            angle = i * 30  # 360 degrees / 12 hours
            text = str(i if i != 0 else 12)
            Digit(self.t, angle, self.radius * 0.85, text).draw()

class Hand:
    def __init__(self, length, thickness, color):
        self.length = length
        self.color = color
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.pensize(thickness)
        self.t.color(color)
    def draw(self, angle):
        self.t.clear()
        self.t.penup()
        self.t.goto(0, 0)
        self.t.setheading(90 - angle)
        self.t.pendown()
        self.t.forward(self.length)

class Watch:
    def update(self):
        raise NotImplementedError

class AnalogWatch(Watch):
    def __init__(self):
        self.face = ClockFace()
        self.face.draw()
        self.sec_hand = Hand(100, 1, "red")
        self.min_hand = Hand(90, 2, "blue")
        self.hour_hand = Hand(60, 4, "black")
    def update(self):
        now = datetime.now()
        second_angle = now.second * 6
        minute_angle = now.minute * 6 + now.second * 0.1
        hour_angle = (now.hour % 12) * 30 + now.minute * 0.5
        self.sec_hand.draw(second_angle)
        self.min_hand.draw(minute_angle)
        self.hour_hand.draw(hour_angle)

class DigitalWatch(Watch):
    def __init__(self, use_24_hour=True):
        self.use_24_hour = use_24_hour
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
    def update(self):
        now = datetime.now()
        self.t.clear()
        if self.use_24_hour:
            time_str = now.strftime("%H:%M:%S")
        else:
            time_str = now.strftime("%I:%M:%S %p")
        self.t.goto(0, 220)
        self.t.write(time_str, align="center", font=("Arial", 18, "bold"))
def main():
    screen = turtle.Screen()
    hour = datetime.now().hour
    screen.bgcolor("lightyellow" if 6 <= hour < 18 else "darkslategray")
    screen.title("Turtle Clock")

    analog = AnalogWatch()
    digital = DigitalWatch(use_24_hour=False)
    def update_all():
        analog.update()
        digital.update()
        screen.ontimer(update_all, 1000)
    update_all()
    turtle.done()

if __name__ == "__main__":
    main()