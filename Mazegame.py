from ursina import *

from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()



camera.orthographic = True #카메라를 직교로 설치
camera.fov = 20 #카메라가 수직으로 볼 수 있는 단위 수를 설정 fov(field of view = 시야각)

ground = Entity(
    model='cube',
    color=color.green,
    z=0.1,
    y=-8,
    scale=(100, 5, 10),
    collider='box'
)

player = PlatformerController2d(
    position=(-15, -5),
    texture='monster_4925777.png',
    color=color.white,
    scale=1.5,
    max_jumps=1
)

background = Entity(
    model='cube',
    texture='background.png',
    scale=(40, 20, 1),
    z=2
)



app.run()