from ursina import *

from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

import random

camera.orthographic = True
camera.fov = 40
#카메라를 직교로 설치
#카메라가 수직으로 볼 수 있는 단위 수를 설정 fov(field of view = 시야각)

ground = Entity(
    model='cube',
    color=color.green,
    z=0.1,
    y=-8,
    scale=(100, 15, 10),
    collider='box'
)

player = PlatformerController2d(
    position=(-30, 0),
    texture='monster_4925777.png',
    color=color.white,
    scale=(1.5),
    max_jumps=2,
    collider='box'
)

background = Entity(
    model='cube',
    texture='background.png',
    scale=(80, 40, 1),
    z=2
)

obstacles = []
for i in range(10):
    obstacle = Entity(
        position=(random.randint(-25, 30), 0),
        model='cube',
        color=color.red,
        texture='spike (3).png',
        scale=1.7,
        collider='sphere'
    )
    obstacles.append(obstacle)

wall= Entity(
    model='cube',
    collider='box',
    color=color.green,
    position=(20,6),
    scale=(5,1)
)

wall2= Entity(
    model='cube',
    collider='box',
    color=color.green,
    position=(-20,6),
    scale=(5,1)
)

wall3= Entity(
    model='cube',
    collider='box',
    color=color.green,
    position=(0,8),
    scale=(3,1)
)

wall4= Entity(
    model='cube',
    collider='box',
    color=color.green,
    position=(-10,7),
    scale=(5,1)
)

wall5= Entity(
    model='cube',
    collider='box',
    color=color.green,
    position=(10,7),
    scale=(5,1)
)

class Exit(Entity):
    def __init__(self, x, z):
        super().__init__(
            model='cube',
            color=color.black,
            scale=(1, 0.5, 1),
            position=(x, -0.5, z),
            collider = 'box'
        )

exit_entity = Exit(33, 0)

def game_over():
     print("도착지점에 도달했습니다. 게임 종료!")
     application.quit()

def reset_player():
    player.position = (-30, 0)

def update():
   for obstacle in obstacles:
        if player.intersects(obstacle).hit:
            print("장애물에 닿았습니다! 시작지점으로 돌아갑니다.")
            reset_player()
   if player.intersects(exit_entity).hit:
      game_over()

app.run()
