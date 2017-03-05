from pygame.locals import *
import pygame, sys, math

GAME_RESOLUTION = GAME_WIDTH, GAME_HEIGHT = 0,0
FPS = 60
GAME_TITLE = "Carro Test"
sprite = sprite1 = pygame.image.load("sprite\\carro.png")
velocity, angle, _angle = 0, 0, 0

tester = True

def img_rotation(_image, _angle):
    loc = _image.get_rect().center
    rot_sprite = pygame.transform.rotate(_image,_angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

if __name__ == '__main__':
    pygame.init()
    game_window = pygame.display.set_mode(GAME_RESOLUTION, FULLSCREEN|HWSURFACE|DOUBLEBUF)
    pygame.display.set_caption(GAME_TITLE)
    GAME_RESOLUTION = GAME_WIDTH, GAME_HEIGHT = game_window.get_size()
    x, y = GAME_WIDTH//2, GAME_HEIGHT//2
    clock = pygame.time.Clock()

    pygame.font.init()
    default_font = pygame.font.get_default_font()
    text_render = pygame.font.Font(default_font, 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_F4:
                    pygame.quit()
                    sys.exit()

                if event.key == 276: #sinistra
                    if velocity >= 0:
                        _angle = 1
                    else:
                        _angle = -1

                if event.key == 275: #destra
                    if velocity >= 0:
                        _angle = -1
                    else:
                        _angle = 1

                if event.key == 273: #su
                    if velocity < 5:
                        velocity += 1

                if event.key == 274: #giu
                    if velocity > -5:
                        velocity -= 1

            elif event.type == pygame.KEYUP:
                if event.key in (275,276):
                    _angle = 0

        if angle >= 360:
            angle = 0
        if angle < 0:
            angle = 359

        angle += _angle * 1.5

        x += math.cos(-math.radians(angle)) * velocity
        y += math.sin(-math.radians(angle)) * velocity

        sprite1 = img_rotation(sprite,angle)
        game_window.fill((255,255,255))
        pygame.Surface.blit(game_window, sprite1, (x,y))

        if tester:
            pygame.Surface.blit(game_window, text_render.render(("Angle: " + str(angle) + " Velocity: " + str(velocity)),True,(0,0,0)),(20,20))
            pygame.Surface.blit(game_window, text_render.render(("X: " + str(round(x,2)) + " Y: " + str(round(y,2))),True,(0,0,0)),(20,70))

        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.font.quit()
    pygame.quit()
    sys.exit(0)