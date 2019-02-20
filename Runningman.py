import pygame
import sys
from SpriteSheetCreator import SpriteSheet
from Img_Loader import load_img

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
"""set teh caption"""
pygame.display.set_caption("WHY are you running?!")


class Player:
    def __init__(self):
        self.sheet = SpriteSheet("data/img/run.png")
        self.img_list = []

        """loading every sprite sheet image in self.list"""
        image = self.sheet.get_image(0, 0, 115, 137)
        self.img_list.append(image)
        image = self.sheet.get_image(115, 0, 115, 137)
        self.img_list.append(image)
        image = self.sheet.get_image(230, 0, 115, 137)
        self.img_list.append(image)
        image = self.sheet.get_image(345, 0, 115, 137)
        self.img_list.append(image)
        image = self.sheet.get_image(460, 0, 115, 137)
        self.img_list.append(image)
        image = self.sheet.get_image(575, 0, 115, 137)
        self.img_list.append(image)
        image = self.sheet.get_image(690, 0, 115, 137)
        self.img_list.append(image)
        image = self.sheet.get_image(805, 0, 115, 137)
        self.img_list.append(image)

    def show(self, current_image):
        """get image from list and blit on screen"""
        image = self.img_list[current_image]
        screen.blit(image, (180, 250))


"""load img is just a function to load and convert images like pygame.image.load("somefile").convert()"""
tree = load_img("tree.png", (150, 200))
RUN = Player()
curr_img = 0
ticker = 0
x, x1, x2 = 500, 500, 500
tree_pos = 500
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    """ticker change every second (3 ticks) the current  sprite img (very basical)"""
    ticker += 1
    if ticker == 3:
        """check if current img pos is in list"""
        if curr_img == len(RUN.img_list)-1:
            """set current img to 0 so sprite sheet start at again"""
            curr_img = 0
        else:
            curr_img += 1
        """reset ticker"""
        ticker = 0

    """move white rects"""
    x = x - 12
    x1 = x1 - 14
    x2 = x2 - 16

    """move tree"""
    tree_pos = tree_pos - 3

    """reset tree and rects"""
    if x == - 100:
        x = 500
        x1 = 500
        x2 = 500
    if tree_pos < - 150:
        tree_pos = 500

    """refresh screen (skyblue)"""
    screen.fill([34, 113, 179])
    """blit the tree"""
    screen.blit(tree, (tree_pos, 170))
    """blit player on screen"""
    RUN.show(curr_img)
    """black road"""
    pygame.draw.rect(screen, (0, 0, 0), (0, 365, 500, 200))
    """white rects"""
    pygame.draw.rect(screen, (255, 255, 255), (x, 370, 100, 20))
    pygame.draw.rect(screen, (255, 255, 255), (x1 + 50, 420, 100, 20))
    pygame.draw.rect(screen, (255, 255, 255), (x2 + 100, 470, 100, 20))

    pygame.display.flip()
    """toggle fps"""
    clock.tick(30)