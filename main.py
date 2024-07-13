import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # Black background
GRID_COLOR = (50, 50, 50)  # Dark gray grid color
GRID_SPACING = 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pattern Generator")

# Pattern types
PATTERN_GRID = "Grid"
PATTERN_CIRCLE = "Circle"
PATTERN_RECTANGLE = "Rectangle"

patterns = [PATTERN_GRID, PATTERN_CIRCLE, PATTERN_RECTANGLE]
current_pattern = PATTERN_GRID

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                handle_key_event(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(event.pos)

        screen.fill(BACKGROUND_COLOR)
        draw_grid()

        if current_pattern == PATTERN_GRID:
            draw_grid_pattern()
        elif current_pattern == PATTERN_CIRCLE:
            draw_circle_pattern()
        elif current_pattern == PATTERN_RECTANGLE:
            draw_rectangle_pattern()

        draw_pattern_menu()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def handle_key_event(key):
    global current_pattern

    if key == pygame.K_g:
        current_pattern = PATTERN_GRID
    elif key == pygame.K_c:
        current_pattern = PATTERN_CIRCLE
    elif key == pygame.K_r:
        current_pattern = PATTERN_RECTANGLE

def handle_mouse_click(pos):
    global current_pattern

    menu_rect = pygame.Rect(SCREEN_WIDTH - 200, 10, 190, 30)
    if menu_rect.collidepoint(pos):
        x_offset = SCREEN_WIDTH - 200
        for idx, pattern in enumerate(patterns):
            pattern_rect = pygame.Rect(x_offset, 10, 60, 30)
            if pattern_rect.collidepoint(pos):
                current_pattern = patterns[idx]
                break
            x_offset += 70

def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

def draw_grid_pattern():
    for x in range(0, SCREEN_WIDTH, GRID_SPACING):
        for y in range(0, SCREEN_HEIGHT, GRID_SPACING):
            pygame.draw.rect(screen, (255, 255, 255), (x, y, GRID_SPACING, GRID_SPACING), 2)

def draw_circle_pattern():
    pattern_color = (255, 0, 0)
    pygame.draw.circle(screen, pattern_color, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 100)

def draw_rectangle_pattern():
    pattern_color = (0, 0, 255)
    pygame.draw.rect(screen, pattern_color, (100, 100, 200, 150))

def draw_pattern_menu():
    font = pygame.font.SysFont(None, 24)
    menu_text = "Select Pattern: "
    x_offset = SCREEN_WIDTH - 200

    pygame.draw.rect(screen, (100, 100, 100), (x_offset, 10, 190, 30))  # Menu background

    for pattern in patterns:
        pattern_text = font.render(pattern, True, (255, 255, 255))
        pattern_rect = pattern_text.get_rect(topleft=(x_offset + 5, 15))
        screen.blit(pattern_text, pattern_rect)
        x_offset += 70

if __name__ == "__main__":
    main()
