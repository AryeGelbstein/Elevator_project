from building import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(DING_SOUND_PATH)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Menivim Towers')


world_height = max(WINDOW_HEIGHT, MARGIN * 2 + NUM_OF_FLOORS * FLOOR_HEIGHT)
world = pygame.Surface((WINDOW_WIDTH, world_height))
scroll_y = 0
scroll_speed = SCROLL_SPEED
building = Building(NUM_OF_FLOORS, NUM_OF_ELEVATORS, world)

run = True

while run:
    pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LEFT:
                pos = pygame.mouse.get_pos()
                x, y = pos
                y -= scroll_y
                pos = x, y
            elif event.button == MOUSE_WHEEL_UP:
                scroll_y -= scroll_speed
            elif event.button == MOUSE_WHEEL_DOWN:
                scroll_y += scroll_speed
            scroll_y = max(0, min(world_height - WINDOW_HEIGHT, scroll_y))

    world.fill(WHITE)
    building.draw()

    building.update(pos)

    window.blit(world, (0, 0), pygame.Rect((0, world_height - WINDOW_HEIGHT - scroll_y, WINDOW_WIDTH, WINDOW_HEIGHT)))
    pygame.display.flip()

