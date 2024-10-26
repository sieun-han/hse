from ursina import *

from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

player = PlatformerController2d()

camera.orthographic = True #카메라를 직교로 설치
camera.fov = 20 #카메라가 수직으로 볼 수 있는 단위 수를 설정 fov(field of view = 시야각)

ground = Entity(
    model='cube',
    color=color.rgb(50, 180, 50),
    z=0,
    y=-8,
    scale=(100, 5, 10),
    collider='box'
)

player = PlatformerController2d(
    position=(-15, -5),
    color=color.white,
    scale=1,
    max_jumps=2
)

app.run()