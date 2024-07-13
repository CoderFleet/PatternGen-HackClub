import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
GRID_COLOR = (50, 50, 50)
GRID_SPACING = 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pattern Generator")

PATTERN_GRID = "Grid"
PATTERN_CIRCLE = "Circle"
PATTERN_RECTANGLE = "Rectangle"
PATTERN_SPIRAL = "Spiral"

patterns = [PATTERN_GRID, PATTERN_CIRCLE, PATTERN_RECTANGLE, PATTERN_SPIRAL]
current_pattern = None
shape_filled = False
shapes = []

def main():
    global shapes
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
        draw_grid()  # Draw grid before any shapes

        for shape in shapes:
            draw_shape(shape)

        draw_pattern_menu()
        draw_fill_mode_button()
        draw_clear_canvas_button()
        draw_pattern_controls()

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
    elif key == pygame.K_s:
        current_pattern = PATTERN_SPIRAL

def handle_mouse_click(pos):
    global shape_filled

    menu_rect = pygame.Rect(SCREEN_WIDTH - 200, 10, 190, 30)
    fill_button_rect = pygame.Rect(20, 20, 120, 30)
    clear_button_rect = pygame.Rect(150, 20, 120, 30)

    if menu_rect.collidepoint(pos):
        x_offset = SCREEN_WIDTH - 200
        for idx, pattern in enumerate(patterns):
            pattern_rect = pygame.Rect(x_offset, 10, 60, 30)
            if pattern_rect.collidepoint(pos):
                select_pattern(patterns[idx])
                break
            x_offset += 70
    elif fill_button_rect.collidepoint(pos):
        shape_filled = not shape_filled
    elif clear_button_rect.collidepoint(pos):
        clear_canvas()

def select_pattern(pattern):
    global current_pattern, shapes

    current_pattern = pattern
    if current_pattern == PATTERN_GRID:
        shapes.append({"type": "grid"})
    elif current_pattern == PATTERN_CIRCLE:
        shapes.append({"type": "circle"})
    elif current_pattern == PATTERN_RECTANGLE:
        shapes.append({"type": "rectangle"})
    elif current_pattern == PATTERN_SPIRAL:
        shapes.append({"type": "spiral"})

def clear_canvas():
    global shapes
    shapes = []

def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

def draw_shape(shape):
    if shape["type"] == "grid":
        draw_grid_pattern()
    elif shape["type"] == "circle":
        draw_circle_pattern()
    elif shape["type"] == "rectangle":
        draw_rectangle_pattern()
    elif shape["type"] == "spiral":
        draw_spiral_pattern()

def draw_grid_pattern():
    for x in range(0, SCREEN_WIDTH, GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

def draw_circle_pattern():
    pattern_color = (255, 0, 0)
    if shape_filled:
        pygame.draw.circle(screen, pattern_color, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 100)
    else:
        pygame.draw.circle(screen, pattern_color, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 100, 2)

def draw_rectangle_pattern():
    pattern_color = (0, 0, 255)
    rect = pygame.Rect(100, 100, 200, 150)
    if shape_filled:
        pygame.draw.rect(screen, pattern_color, rect)
    else:
        pygame.draw.rect(screen, pattern_color, rect, 2)

def draw_spiral_pattern():
    center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    radius = 100
    max_radius = 200
    num_lines = 100
    color = (0, 255, 0)

    for i in range(num_lines):
        angle = i * (360 / num_lines)
        line_length = radius + (max_radius - radius) * i / num_lines
        x1 = center_x + int(radius * pygame.math.cos(angle * pygame.math.pi / 180))
        y1 = center_y + int(radius * pygame.math.sin(angle * pygame.math.pi / 180))
        x2 = center_x + int(line_length * pygame.math.cos(angle * pygame.math.pi / 180))
        y2 = center_y + int(line_length * pygame.math.sin(angle * pygame.math.pi / 180))
        if shape_filled:
            pygame.draw.line(screen, color, (x1, y1), (x2, y2), 2)
        else:
            pygame.draw.line(screen, color, (x1, y1), (x2, y2))

def draw_pattern_menu():
    font = pygame.font.SysFont(None, 24)
    menu_text = "Select Pattern: "
    x_offset = SCREEN_WIDTH - 200

    pygame.draw.rect(screen, (100, 100, 100), (x_offset, 10, 190, 30))

    for pattern in patterns:
        pattern_text = font.render(pattern, True, (255, 255, 255))
        pattern_rect = pattern_text.get_rect(topleft=(x_offset + 5, 15))
        screen.blit(pattern_text, pattern_rect)
        x_offset += 70

def draw_fill_mode_button():
    font = pygame.font.SysFont(None, 24)
    button_text = "Toggle Fill/Outline"
    button_rect = pygame.Rect(20, 20, 120, 30)

    pygame.draw.rect(screen, (100, 100, 100), button_rect)
    text = font.render(button_text, True, (255, 255, 255))
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

def draw_clear_canvas_button():
    font = pygame.font.SysFont(None, 24)
    button_text = "Clear Canvas"
    button_rect = pygame.Rect(150, 20, 120, 30)

    pygame.draw.rect(screen, (100, 100, 100), button_rect)
    text = font.render(button_text, True, (255, 255, 255))
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

def draw_pattern_controls():
    font = pygame.font.SysFont(None, 24)
    controls_text = "Pattern Controls:"
    controls_rect = pygame.Rect(20, SCREEN_HEIGHT - 50, 200, 30)
    pygame.draw.rect(screen, (100, 100, 100), controls_rect)

    text = font.render(controls_text, True, (255, 255, 255))
    text_rect = text.get_rect(center=controls_rect.center)
    screen.blit(text, text_rect)

if __name__ == "__main__":
    main()
