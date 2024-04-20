from pygame import *
 
class GameSprite(sprite.Sprite):
    def __init__(self, x, y, img, w, h, speed=0):
        super().__init__()
        self.w = w
        self.h = h
        self.speed = speed
        self.image = transform.scale(image.load(img), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def render(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
 
class Ball(GameSprite):
    def __init__(self, x, y, img, w, h, speed_x, speed_y):

        self.w = w
        self.h = h
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.image = transform.scale(image.load(img), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.directH = 'r'
        self.directV = 'up'
    def render(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def move(self):
        if self.rect.y >= 440:
            self.directV = 'up'
        if self.rect.y <= 10:
            self.directV = 'down'
        if self.directV == 'up':
            self.rect.y -= self.speed_y
        if self.directV == 'down':
            self.rect.y += self.speed_y    
        self.rect.x += self.speed_x

class Player(GameSprite):
    def moving(self):
        keys = key.get_pressed()
        if keys[K_w]:
            if self.rect.y >= 30:
                self.rect.y -= self.speed
        if keys[K_s]:
            if self.rect.y <= 350:
                self.rect.y += self.speed
    def moving_2(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            if self.rect.y >= 30:
                self.rect.y -= self.speed
        if keys[K_DOWN]:
            if self.rect.y <= 350:
                self.rect.y += self.speed
 
player1 = Player(50,100,'player1.png',40,120,15)
player2 = Player(600,100,'player1.png',40,120,15)
 
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
clock = time.Clock()
 
ball = Ball(130, 100, 'ball.png', 50, 50, 10,5)

bg = transform.scale(image.load('court.jpg'), (700, 500))
 
game = True
 
while game:
    #события
    for ev in event.get():
        if ev.type == QUIT:
            game = False
    #Отрисовка
    window.blit(bg, (0,0))
    ball.render()
    player1.render()
    player2.render()
    #колизия
    if sprite.collide_rect(player1, ball):
        ball.speed_x *= -1
    if sprite.collide_rect(player2, ball):
        ball.speed_x *= -1
    #Вызов методов
    ball.move()
    player1.moving()
    player2.moving_2()
    display.update()
    clock.tick(60)