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
# 먼저 이미지를 띄운다
# circle함수를 만들어본다.
# 컴파일하고 syntx오류가 나지않으면 커밋을 한다.
# 테스트 리드 타임 = 내가 어떤 버그나 테스트를 하기위해서 걸리는 사간
# 최대한 테스트 리드 타임을 줄여야한다.
# 컴파일 시간도 테스트 리드 타임으로 들어감
# 즉 여기서는 원을 그리는 것을 확인했는데 원그리는 것을 안보면 된다.
# circle함수를 주석 처리하자
x = 0
y = 90


def render():
    clear_canvas()
    character.draw(x, y)
    grass.draw(400, 30)
    update_canvas()
    delay(0.01)
def run_bottom():
    global x
    global y
    while x < get_canvas_width():
        render()
        x+=2

def run_top():
    global x
    global y
    while x > 0:
        render()
        x -= 2
def run_right():
    global x
    global y
    while y < get_canvas_height():
        render()
        y+=2

def run_left():
    global x
    global y
    while y > 90:
        render()
        y-=2
    pass

def run_rectangle():
    global x
    global y
    run_bottom()
    run_right()
    run_top()
    run_left()



    pass
def run_circle():
    global x
    global y
    cx = get_canvas_width()//2
    cy = get_canvas_height()//2
    r = 300
    for d in range(360):
        render()
        x = cx + r * math.cos(math.radians(d))
        y = cy + r * math.sin(math.radians(d))
    x=0
    y=90
    pass


while True:

    run_rectangle()
    #run_circle()


close_canvas()
