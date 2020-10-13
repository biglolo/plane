import pygame
from plane_sprites import *

pygame.init()
interface = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
interface.blit(bg, (0, 0))
pygame.display.update()

hero = pygame.image.load("./images/me1.png")
interface.blit(hero, (200, 500))
pygame.display.update()

clock = pygame.time.Clock()
hero_rect = pygame.Rect(200, 500, 102, 126)

#  创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")

#  创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy)

i = 0
while True:
    #  指定内部代码执行频率
    clock.tick(60)
    #  捕获事件
    eventlist = pygame.event.get()
    for event in eventlist:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #  修改飞机位置
    hero_rect.y -= 1
    #  判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700
    #  把背景图和飞机加载到屏幕中
    interface.blit(bg, (0, 0))
    interface.blit(hero, hero_rect)
    #  把敌机加载到屏幕中
    enemy_group.update()
    enemy_group.draw(interface)
    #  刷新屏幕
    pygame.display.update()




pygame.quit()
