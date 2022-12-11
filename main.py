from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_size, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), sprite_size)
        
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        
        self.speed = sprite_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 0:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - ship_width:
           self.rect.x += self.speed

#константы
win_height = 500
win_width = 700

racket_height = 80
racket_width = 40

racket_start_x = win_width / 2
racket_start_y = win_height - racket_height - 5

bullet_group = sprite.Group()

#fps
clock = time.Clock()
FPS = 60 

#шрифты 
font.init() 
fonts1 = font.Font(None, 66)


# окно
window = display.set_mode((win_width, win_height))
display.set_caption("Ping pong")
#картинки 
fonts = "assets/Fon.jpg"
fonts = transform.scale(image.load(fonts), (win_width, win_height))
ball = "assets/ball.jpg"
rackets = "assets/racket.png"

#спрайты 
space_racket = Player(rackets, racket_start_x, racket_start_y, (racket_width, racket_height), 5)



run = True
finish = False

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish: 
        space_racket.update()
        window.blit(fonts,(0, 0))






    display.update()
    clock.tick(FPS)