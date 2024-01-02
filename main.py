import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
move_increment = 5
# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
#player setup
player = Player()
player.listen()
player.move()
# foundational game info
game_is_on = True
cars_list = []
car_manager = CarManager()
cars_list.append(car_manager)
fake_time = 0
fake_time_level = 1
scoreboard = Scoreboard()
scoreboard.update_score()
# gameplay code
while game_is_on:
    for car in cars_list:
        car.drive(move_increment)
        # Detect Collision
        if player.distance(car) < 22:
            # print("Nooooooooo")
            scoreboard.game_over()
            game_is_on = False
    time.sleep(0.1)
    screen.update()
    fake_time += fake_time_level
    # if fake_time % 10 == 0:
    if car_manager.more_cars():
        new_car = CarManager()
        cars_list.append(new_car)
    # LEVEL UP
    if player.ycor() > 280:
        for car in cars_list:
            car.goto(1000,1000)
        cars_list = []
        fake_time = 0
        fake_time_level += 1
        scoreboard.level_up()
        player.level_up()
        move_increment += 3


screen.exitonclick()



