from pico2d import *
import math
open_canvas()
character = load_image('character.png')
grass = load_image('grass.png')
#뼈대를 잡아라->무한루프가 필요->그안에 사각형 운동과 원운동하는 것이 필요함
#함수를 호출을 하고 함수를 정의하자
#함수정의를pass하고
#git에 커밋을 한다 git은 개발 일지이다.
#코딩을 할때 조그맣게 시작 조각을 만들어서 붙이고붙이면서 굴리면서 코딩한다.

x=400
y=90
degree = 0

def render():
    clear_canvas()
    character.draw(x, y)
    grass.draw(400, 30)
    update_canvas()
    delay(0.01)


def run_rectangle():
    pass
def run_circle():
    global x
    global y
    global degree
    x = x + math.cos(degree / 360 * 2 * math.pi)
    y = y + math.sin(degree / 360 * 2 * math.pi)
    degree = degree + 1
    if degree == 360:
        degree = 0
    render()
    pass


while True:
    run_rectangle()
    run_circle()


close_canvas()
