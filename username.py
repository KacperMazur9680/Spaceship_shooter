import pygame
import pygame_gui
import regex as re
import sys

pygame.init()

WIDTH, HEIGHT = 500, 200
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")

manager = pygame_gui.UIManager((WIDTH, HEIGHT))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((50, 75), (400, 50)),
                                                manager=manager,
                                                object_id='#main_text_entry')

label_1 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((33, 40), (300, 50)), 
                                        text='Please enter your username below:',
                                        manager=manager)

label_2 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 110), (440, 50)), 
                                        text='The username cannot start with numbers nor',
                                        manager=manager)

label_3 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((-115, 130), (440, 50)), 
                                        text='special signs',
                                        manager=manager)

clock = pygame.time.Clock()

def valid_user_name(username):
    username_regex = re.compile(r'^(?!^[0-9]*$)(?!^[-_]*$)(?!^\d.*$)[a-zA-Z0-9_-]{3,20}')
    
    if username_regex.match(username):
        return True
    else:
        return False
    

def get_user_name():
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                username =  event.text
                if valid_user_name(username):
                    return username
                else:
                    label_1.kill()
                    new_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, 40), (450, 50)),
                                                            text='Invalid username, please choose another one:',
                                                            manager=manager)
                    continue


            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        SCREEN.fill((30, 30, 30))

        manager.draw_ui(SCREEN)

        pygame.display.update()

