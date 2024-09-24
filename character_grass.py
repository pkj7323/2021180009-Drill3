from pico2d import *
import math
open_canvas()
character = load_image('character.png')
grass = load_image('grass.png')
#뼈대를 잡아라->무한루프가 필요->그안에 사각형 운동과 원운동하는 것이 필요함
#함수를 호출을 하고 함수를 정의하자

x=0
y=90


def render():
    clear_canvas()
    character.draw(x, y)
    grass.draw(0, 90)
    update_canvas()


def run_rectangle():
    pass
def run_circle():
    global x
    global y
    x = x + math.cos(x)
    y = y + math.sin(x)
    pass


while True:
    run_rectangle()
    run_circle()









close_canvas()
