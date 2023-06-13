from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.turtles = []

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            cars = Turtle()
            cars.shape("square")
            cars.color(random.choice(COLORS))
            cars.penup()
            cars.setheading(90)
            cars.shapesize(stretch_wid=2, stretch_len=1)
            random_y = random.randint(-230, 230)
            cars.goto(300, random_y)
            self.turtles.append(cars)

    def car_move(self):
        for car in self.turtles:
            x_cor = -car.xcor() + STARTING_MOVE_DISTANCE
            car.goto(-x_cor, car.ycor())

