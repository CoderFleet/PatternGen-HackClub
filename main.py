import pygame
import sys
import math

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

# Pattern parameters
circle_radius = 50  # Default size for circle
rectangle_width = 100  # Default width for rectangle
rectangle_height = 100  # Default height for rectangle

# UI parameters
slider_x = 20
slider_y = SCREEN_HEIGHT - 50
slider_width = 200
slider_height = 20
slider_color = (150, 150, 150)
slider_handle_radius = 8
slider_handle_color = (100, 100, 255)

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
            elif event.type == pygame.MOUSEMOTION:
                handle_slider_drag(event.pos)

        screen.fill(BACKGROUND_COLOR)
        draw_grid()

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
        x_offset = SCREEN_WIDTH - 400
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
    else:
        add_shape(pos)

def handle_slider_drag(pos):
    global circle_radius, rectangle_width, rectangle_height

    if current_pattern == PATTERN_CIRCLE:
        if slider_rect.collidepoint(pos):
            relative_x = pos[0] - slider_x
            circle_radius = int(relative_x / slider_width * 100)  # Adjust range as needed
    elif current_pattern == PATTERN_RECTANGLE:
        if slider_rect.collidepoint(pos):
            relative_x = pos[0] - slider_x
            rectangle_width = int(relative_x / slider_width * 200)  # Adjust range as needed
            rectangle_height = int(relative_x / slider_width * 200)  # Adjust range as needed

def select_pattern(pattern):
    global current_pattern, shapes

    current_pattern = pattern
    if current_pattern == PATTERN_GRID:
        shapes.append({"type": "grid", "position": (0, 0)})
    elif current_pattern == PATTERN_CIRCLE:
        shapes.append({"type": "circle", "position": (0, 0)})
    elif current_pattern == PATTERN_RECTANGLE:
        shapes.append({"type": "rectangle", "position": (0, 0)})
    elif current_pattern == PATTERN_SPIRAL:
        shapes.append({"type": "spiral", "position": (0, 0)})

def clear_canvas():
    global shapes
    shapes = []

def add_shape(pos):
    global shapes
    if current_pattern:
        shapes.append({"type": current_pattern.lower(), "position": pos})

def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

def draw_shape(shape):
    if shape["type"] == "grid":
        draw_grid_pattern()
    elif shape["type"] == "circle":
        draw_circle_pattern(shape["position"])
    elif shape["type"] == "rectangle":
        draw_rectangle_pattern(shape["position"])
    elif shape["type"] == "spiral":
        draw_spiral_pattern(shape["position"])

def draw_grid_pattern():
    for x in range(0, SCREEN_WIDTH, GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

def draw_circle_pattern(position):
    global circle_radius
    center_x, center_y = position
    pattern_color = (255, 0, 0)
    if shape_filled:
        pygame.draw.circle(screen, pattern_color, position, circle_radius)
    else:
        pygame.draw.circle(screen, pattern_color, position, circle_radius, 2)

def draw_rectangle_pattern(position):
    global rectangle_width, rectangle_height
    pattern_color = (0, 0, 255)
    rect = pygame.Rect(position[0] - rectangle_width // 2, position[1] - rectangle_height // 2, rectangle_width, rectangle_height)
    if shape_filled:
        pygame.draw.rect(screen, pattern_color, rect)
    else:
        pygame.draw.rect(screen, pattern_color, rect, 2)

def draw_spiral_pattern(position):
    center_x, center_y = position
    max_radius = 200
    num_lines = 100
    color = (0, 255, 0)

    for i in range(num_lines):
        angle = i * (360 / num_lines)
        line_length = (i + 1) * 2
        x1 = center_x + int(i * math.cos(angle * math.pi / 180))
        y1 = center_y + int(i * math.sin(angle * math.pi / 180))
        x2 = center_x + int((i + line_length) * math.cos(angle * math.pi / 180))
        y2 = center_y + int((i + line_length) * math.sin(angle * math.pi / 180))
        pygame.draw.line(screen, color, (x1, y1), (x2, y2))

def draw_pattern_menu():
    font = pygame.font.SysFont(None, 24)
    menu_text = "Select Pattern: "
    x_offset = SCREEN_WIDTH - 350

    pygame.draw.rect(screen, (100, 100, 100), (x_offset, 10, 390, 30))

    for pattern in patterns:
        pattern_text = font.render(pattern, True, (255, 255, 255))
        pattern_rect = pattern_text.get_rect(topleft=(x_offset + 5, 15))
        screen.blit(pattern_text, pattern_rect)
        x_offset += 100

def draw_fill_mode_button():
    font = pygame.font.SysFont(None, 20)
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
    global slider_rect
    font = pygame.font.SysFont(None, 24)
    slider_rect = pygame.Rect(slider_x, slider_y, slider_width, slider_height)

    pygame.draw.rect(screen, slider_color, slider_rect)
    pygame.draw.circle(screen, slider_handle_color, (slider_x + int(circle_radius / 100 * slider_width), slider_y + slider_height // 2), slider_handle_radius)

    text = font.render("Pattern Size", True, (255, 255, 255))
    text_rect = text.get_rect(midtop=(slider_x + slider_width // 2, slider_y - 20))
    screen.blit(text, text_rect)

def draw_slider_handle():
    handle_center_x = slider_x + int(circle_radius / 100 * slider_width)
    handle_center_y = slider_y + slider_height // 2
    pygame.draw.circle(screen, slider_handle_color, (handle_center_x, handle_center_y), slider_handle_radius)

if __name__ == "__main__":
    main()
