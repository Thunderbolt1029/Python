import sys, pygame
pygame.init()

size = width, height = 750, 500
speed = [0, 0]
black = 0, 0, 0
bounce = False

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball/ball.gif")
ballrect = ball.get_rect()
ballrect.top, ballrect.left = (height/2-((ballrect.top+ballrect.bottom)/2)), (width/2-((ballrect.left+ballrect.right)/2))

background = pygame.image.load("ball/background.gif")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: sys.exit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP: speed[1]+=-1
        elif event.type == pygame.KEYUP and event.key == pygame.K_UP: speed[1]=0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN: speed[1]+=1
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN: speed[1]=0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT: speed[0]+=-1
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT: speed[0]=0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT: speed[0]+=1
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT: speed[0]=0

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
            if bounce: bounce = False
            else: bounce = True
    
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width: 
        if bounce: speed[0] = -speed[0]
        else: speed[0]=0
    if ballrect.top < 0 or ballrect.bottom > height: 
        if bounce: speed[1] = -speed[1]
        else: speed[1]=0

    screen.blit(background, (0,0))
    screen.blit(ball, ballrect)
    pygame.display.flip()