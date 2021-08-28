import pygame as pg
from sys import exit

# Classes
class Unit(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('graphics/Orin03_128x128.png').convert()
        self.rect = self.image.get_rect()

    def select(self):
        print('you selected a unit')

    #def update(self):


class Cursor(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((32,32), pg.SRCALPHA)
        self.rect = pg.draw.polygon(
            self.image, (255,255,255), [(0,0),(16,32),(32,16)]
            )

    def update(self):
        self.rect.topleft = pg.mouse.get_pos()


# Setup

pg.init()
clock = pg.time.Clock()

screen_width = 800
screen_height = 400
screen = pg.display.set_mode((screen_width, screen_height))

pg.display.set_caption('OB_like')

pg.mouse.set_visible(False)

# Groups

unit = Unit()
unit_group = pg.sprite.Group()
unit_group.add(unit)

cursor = Cursor()
cursor_group = pg.sprite.GroupSingle()
cursor_group.add(cursor)

# Main Program Loop

while True:
    # Main event loop
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            # Check if the mouse button was pressed while over a unit
            # Might just want to do this by making a sprite that follows mouse
            # That way we can use pygame.sprite.spritecollide()? IDK
            if pg.sprite.collide_rect(cursor, unit):
                unit.select()

    # Draw graphics
    screen.fill((25,200,146))
    unit_group.draw(screen)
    unit_group.update()
    cursor_group.draw(screen)
    cursor_group.update()

    # Update entire screen
    pg.display.flip()

    # Set frame rate
    clock.tick(60)

pg.quit()