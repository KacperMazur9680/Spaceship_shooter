import pygame
import pygame_gui
import sys

pygame.init()

WIDTH, HEIGHT = 500, 200
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")

manager = pygame_gui.UIManager((WIDTH, HEIGHT))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((50, 75), (400, 50)), manager=manager,
                                                object_id='#main_text_entry')
label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((38, 40), (300, 50)), text='Please enter your username below:',
                                                manager=manager)

clock = pygame.time.Clock()

def get_user_name():
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                return event.text
            
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        SCREEN.fill((30, 30, 30))

        manager.draw_ui(SCREEN)

        pygame.display.update()

