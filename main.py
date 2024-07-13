import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
GRID_COLOR = (0, 0, 0)
GRID_SPACING = 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pattern Generator")

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BACKGROUND_COLOR)
        draw_grid()
        draw_sample_pattern()
        draw_text()
        draw_lines()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

def draw_sample_pattern():
    pattern_color = (255, 0, 0)
    pygame.draw.circle(screen, pattern_color, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 100)
    pygame.draw.rect(screen, pattern_color, (100, 100, 200, 150))

def draw_text():
    font = pygame.font.SysFont(None, 36)
    text = font.render("Pattern Generator", True, (0, 0, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 30))
    screen.blit(text, text_rect)

def draw_lines():
    line_color = (0, 255, 0)
    pygame.draw.line(screen, line_color, (50, 50), (SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50), 5)
    pygame.draw.line(screen, line_color, (50, SCREEN_HEIGHT - 50), (SCREEN_WIDTH - 50, 50), 5)

if __name__ == "__main__":
    main()
