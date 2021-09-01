import pygame as pg
from sys import exit

# Dynamic Groups
selectables = pg.sprite.Group()

unit_deployers = pg.sprite.Group()

units = pg.sprite.Group()

selected = pg.sprite.GroupSingle()

# Classes


class Selectable(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.add(selectables)

    def select(self):
        self.add(selected)

    def is_selected(self):
        if self in selected:
            self.image.fill('purple')
        else:
            self.image.fill('red3')

    def update(self):
        self.is_selected()


class Unit_Deployer(Selectable):
    def __init__(self):
        super().__init__()

        self.image = pg.Surface((32, 32), pg.SRCALPHA)
        self.image.fill('red3')
        self.rect = self.image.get_rect()

        self.add(unit_deployers)
        self.rect.center = pg.mouse.get_pos()

    def deploy_unit(self):
        if self in selected:
            units.add(Unit((self.rect.x, self.rect.y)))

    def update(self):
        super().update()


class Unit(Selectable):
    def __init__(self, starting_pos):
        super().__init__()

        self.image = pg.Surface((32, 32), pg.SRCALPHA)
        self.image.fill('gray')
        self.rect = self.image.get_rect(center=starting_pos)

        self.add(units)


class Cursor(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((32, 32), pg.SRCALPHA)
        self.rect = pg.draw.polygon(
            self.image, (255, 255, 255), [(0, 0), (16, 32), (32, 16)]
        )
        self.rect = pg.Rect(0, 0, 1, 1)

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

# Static Groups
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
            if pg.mouse.get_pressed()[0]:
                selected.empty()
                if pg.sprite.spritecollide(cursor, selectables, False):
                    pg.sprite.spritecollide(
                        cursor, selectables, False
                    )[-1].select()
                print(selected.sprites())

            if pg.mouse.get_pressed()[1]:
                unit_deployers.add(Unit_Deployer())

            if pg.mouse.get_pressed()[2]:
                if selected.sprites():
                    if selected.sprites()[0] in unit_deployers:
                        selected.sprites()[0].deploy_unit()

    # Draw graphics
    screen.fill((25, 200, 146))
    unit_deployers.draw(screen)
    unit_deployers.update()
    units.draw(screen)
    units.update()
    cursor_group.draw(screen)
    cursor_group.update()

    # Print Messages

    # Update entire screen
    pg.display.flip()

    # Set frame rate
    clock.tick(60)

pg.quit()
