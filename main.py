import pygame
import field

def run():
    pygame.init()
    board_size = (30,15)
    size = (board_size[0]*20+200, board_size[1]*20+200)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    game = field.Field(board_size[0],board_size[1], 1)
    total = 0
    done = False

    while not done:
        time_passed_seconds = clock.tick(60)/1000.0
        total += time_passed_seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        screen.fill((0, 0, 0))
        if total >= .1:
            total = 0
            game.draw(screen, True)
        else:
            game.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    run()