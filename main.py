import pygame as pg
from sys import exit

# Classes
class Unit_Deployer(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((32,32), pg.SRCALPHA)


class Unit(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('graphics/Orin03_128x128.png').convert()
        self.rect = self.image.get_rect()

    def deselect(self):
        self.remove(selected)
        print('you deselected a unit')
        print(selected)

    def select(self):
        self.add(selected)
        print('you selected a unit')
        print(selected)

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

unit_group = pg.sprite.Group()

selected = pg.sprite.GroupSingle()

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
        #if event.type == pg.MOUSEBUTTONDOWN:
            # Unit Selection
            #if pg.sprite.collide_rect(cursor, unit):
                #unit.select()
            #else:
                #unit.deselect()

    # Draw graphics
    screen.fill((25,200,146))
    unit_group.draw(screen)
    unit_group.update()
    cursor_group.draw(screen)
    cursor_group.update()

    # Print Messages

    # Update entire screen
    pg.display.flip()

    # Set frame rate
    clock.tick(60)

pg.quit()