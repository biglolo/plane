import pygame
from plane_sprites import *


SCREEN_RECT = pygame.Rect(0, 0, 420, 700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class PlaneGame(object):
    def __init__(self):
        print("游戏初始化")
        #  创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #  创建游戏的时钟
        self.clock = pygame.time.Clock()
        #  调用私有方法创建精灵和精灵组
        self.__create_sprites()
        #  设置定时器
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(isalt=True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("启动游戏")
        while True:
            # 设置刷新率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新绘制精灵族
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy1 = Enemy()
                self.enemy_group.add(enemy1)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keys_press = pygame.key.get_pressed()
        if keys_press[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_press[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        enemies = pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True, True)
        if len(enemies) > 0:
            self.hero.kill
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    #  创建游戏对象
    game = PlaneGame()
    #  启动游戏
    game.start_game()
