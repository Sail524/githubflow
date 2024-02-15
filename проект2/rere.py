import pygame
import random

# Инициализация игрового движка
pygame.init()

# Размер окна игры
window_width = 800
window_height = 800

# Цвета
white = (255, 255, 255)
gray = (128, 128, 128)
red = (255, 0, 0)

# Создание главного окна
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Стрельба по мишеням")


# Функция отрисовки текста
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)


# Функция отображения главного меню
def show_main_menu():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(gray)
        draw_text("Стрельба по мишеням", pygame.font.Font(None, 50), white, window_width // 2, window_height // 4)
        pygame.draw.rect(window, white, (window_width // 2 - 75, window_height // 2 - 50, 150, 50))
        pygame.draw.rect(window, white, (window_width // 2 - 75, window_height // 2 + 50, 150, 50))
        draw_text("Играть", pygame.font.Font(None, 30), gray, window_width // 2, window_height // 2 - 25)
        draw_text("Выход", pygame.font.Font(None, 30), gray, window_width // 2, window_height // 2 + 75)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if window_width // 2 - 75 <= mouse_pos[0] <= window_width // 2 + 75 and window_height // 2 - 50 <= mouse_pos[
            1] <= window_height // 2:
            pygame.draw.rect(window, red, (window_width // 2 - 75, window_height // 2 - 50, 150, 50))
            draw_text("Играть", pygame.font.Font(None, 30), white, window_width // 2, window_height // 2 - 25)
            if mouse_click[0] == 1:
                show_level_menu()
        elif window_width // 2 - 75 <= mouse_pos[0] <= window_width // 2 + 75 and window_height // 2 + 50 <= mouse_pos[
            1] <= window_height // 2 + 100:
            pygame.draw.rect(window, red, (window_width // 2 - 75, window_height // 2 + 50, 150, 50))
            draw_text("Выход", pygame.font.Font(None, 30), white, window_width // 2, window_height // 2 + 75)
            if mouse_click[0] == 1:
                running = False
        else:
            draw_text("Играть", pygame.font.Font(None, 30), white, window_width // 2, window_height // 2 - 25)
            draw_text("Выход", pygame.font.Font(None, 30), white, window_width // 2, window_height // 2 + 75)

        pygame.display.flip()


# Функция отображения меню выбора уровня
def show_level_menu():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(gray)
        draw_text("Выбор уровня", pygame.font.Font(None, 50), white, window_width // 2, window_height // 4)

        level_button_y = window_height // 3
        for level in range(1, 11):
            pygame.draw.rect(window, white, (window_width // 2 - 75, level_button_y, 150, 50))
            draw_text("Уровень " + str(level), pygame.font.Font(None, 30), gray, window_width // 2, level_button_y + 25)

            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            if window_width // 2 - 75 <= mouse_pos[0] <= window_width // 2 + 75 and level_button_y <= mouse_pos[
                1] <= level_button_y + 50:
                pygame.draw.rect(window, red, (window_width // 2 - 75, level_button_y, 150, 50))
                draw_text("Уровень " + str(level), pygame.font.Font(None, 30), white, window_width // 2,
                          level_button_y + 25)
                if mouse_click[0] == 1:
                    show_game(level)

            level_button_y += 70

        pygame.display.flip()


# Функция отображения игрового экрана
def show_game(level):
    running = True
    score = 0
    timer = 100 - (level - 1) * 5
    target_radius = 20
    targets_count = 25 + (level - 1) * 10
    target_speed = 2 + (level - 1) * 2

    targets = []
    for _ in range(targets_count):
        target = pygame.Rect(random.randint(50, window_width - 50), random.randint(50, window_height - 50), 30, 30)
        targets.append(target)

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for target in targets:
                    if (target[0] - mouse_pos[0]) ** 2 + (target[1] - mouse_pos[1]) ** 2 <= target[2] ** 2:
                        targets.remove(target)
                        score += 2

        window.fill(white)

        for target in targets:
            pygame.draw.circle(window, gray, (target[0], target[1]), target[2])
            pygame.draw.circle(window, red, (target[0], target[1]), target[2] // 2)

        draw_text("Счет: " + str(score), pygame.font.Font(None, 30), gray, 70, 30)
        draw_text("Время: " + str(timer), pygame.font.Font(None, 30), gray, window_width - 70, 30)

        if pygame.time.get_ticks() % 10 == 0:
            timer -= 1

        if timer <= 0:
            running = False

        pygame.display.flip()
        clock.tick(60)

    show_level_menu()


# Запуск главного меню
show_main_menu()

# Выход из игрового движка
pygame.quit()