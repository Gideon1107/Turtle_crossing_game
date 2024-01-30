import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkeypress(player.move_up, "Up")



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move()

    #Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Detect when player reaches the other side
    if player.ycor() >= 280:

        #Resetting the player position and increasing the car speed
        player.reset_pos()
        car_manager.increase_speed()

        #Increasing the level number and updating to the screen
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
screen.exitonclick()


