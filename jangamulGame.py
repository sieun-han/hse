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

for i in range(10):
    obstacle = Entity(
        position=(random.randint(-10, 10), -5),
        model='cube',
        color=color.white,
        scale=1
    )

class Exit(Entity):
    def __init__(self, x, z):
        super().__init__(
            model='cube',
            color=color.green,
            scale=(0.1, 0.1, 0.1),
            position=(x, 0, z)
            )
self.player = player #외부 플레이어의 정보를 Exit 클래스의 self.player 변수에 저장

def update(self):
    self.playerCollision()

def playerCollision(self, player):
 if player.intersects(self).hit:
            return True  # 충돌함
            return False  # 충돌하지 않음

def update(self):
        if player.intersects(self).hit:
            print("게임 오버! 장애물에 닿았습니다.")
            Text(text="게임 오버", origin=(0, 0), scale=2)
            invoke(application.quit, delay=2)  # 2초 뒤에 게임 종료


app.run()
