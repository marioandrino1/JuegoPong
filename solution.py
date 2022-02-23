import pygame
pygame.init()


WIDTH,HEIGHT = 700,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pongo")

FPS = 60


WHITE=(255,255,255)
BLACK=(0,0,0)
PADDLE_HEIGHT,PADDLE_WIDHT=100,20



class Paddle:

    COLOR= WHITE
    VEL = 4
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def draw(self,win):
        pygame.draw.rect(win,self.COLOR,(self.x,self.y,self.width,self.height))

    def move(self,up=True):
        if up:
            self.y -=self.VEL
        else:
            self.y += self.VEL




def draw(win,paddles):
    win.fill(BLACK)
    for a in paddles:
        a.draw(win)
    pygame.display.update()


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w]:
        left_paddle.move(up=True)
    if keys[pygame.K_s]:
        left_paddle.move(up=False)
    if keys[pygame.K_UP]:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN]:
        right_paddle.move(up=False)


def main():
    run = True
    clock = pygame.time.Clock()
    left_paddle=Paddle(10,HEIGHT//2-PADDLE_HEIGHT//2,PADDLE_WIDHT,PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH-10-PADDLE_WIDHT, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDHT, PADDLE_HEIGHT)

    while run:
        clock.tick(FPS)
        draw(WIN,[left_paddle,right_paddle])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys,left_paddle,right_paddle)


    pygame.quit()

if __name__ == '__main__':
    main()

