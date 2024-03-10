from pygame import*
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load('e11ab25751594474d037708b6a958697.jpg'),(win_width, win_height))
game = True
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65)) #dslh
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 3:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 70:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x  <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

player = Player('Picsart_24-03-03_16-20-54-518.png', 5, win_height - 80, 4) #xyspeed
monster = Enemy('Picsart_24-03-10_13-47-07-589.png', win_width - 80, 280, 3)


goal = GameSprite('Picsart_24-03-10_13-48-25-689.png', 600, 390, 0)


#music
#mixer.init()
#mixer_music.load('#mp3')
#mixer_music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    player.update()
    monster.update()
    goal.reset()
    player.reset()
    monster.reset()
    display.update()
    clock.tick(FPS)
