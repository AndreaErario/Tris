import pygame
import os

pygame.init()
screen_width = 500
screen_height = 500
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tris")

font = pygame.font.SysFont("Times New Roman", 20)

run = True

class button(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 90
        self.height = 90
        self.show = False
        self.player_on = False
        self.player_x = False
        self.player_o = False

central_button = button(206, 206)
sideleft_button = button(106, 206)
sideright_button = button(306, 206)

topcentral_button = button(206, 106)
topleft_button = button(106, 106)
topright_button = button(306, 106)

bottomcentral_button = button(206, 306)
bottomleft_button = button(106, 306)
bottomright_button = button(306, 306)


turn = True
start_menu = True
game = False
x_score = 0
o_score = 0
x_win = False
o_win = False
draw = False
x = pygame.image.load(os.path.join("x.png"))
o = pygame.image.load(os.path.join("o.png"))
    
def create_table():
    left_line = pygame.draw.line(win, (255, 255, 255), (200, 100), (200, 400), 10)
    right_line = pygame.draw.line(win, (255, 255, 255), (300, 100), (300, 400), 10)
    top_line = pygame.draw.line(win, (255, 255, 255), (100, 200), (400, 200), 10)
    bottom_line = pygame.draw.line(win, (255, 255, 255), (100, 300), (400, 300), 10)

def restart():
    turn = True
    start_menu = True
    game = False
    central_button.player_x = False
    central_button.player_o = False
    central_button.player_on = False
    sideleft_button.player_x = False
    sideleft_button.player_o = False
    sideleft_button.player_on = False
    sideright_button.player_x = False
    sideright_button.player_o = False
    sideright_button.player_on = False
    topcentral_button.player_x = False
    topcentral_button.player_o = False
    topcentral_button.player_on = False
    topleft_button.player_x = False
    topleft_button.player_o = False
    topleft_button.player_on = False
    topright_button.player_x = False
    topright_button.player_o = False
    topright_button.player_on = False
    bottomcentral_button.player_x = False
    bottomcentral_button.player_o = False
    bottomcentral_button.player_on = False
    bottomleft_button.player_x = False
    bottomleft_button.player_o = False
    bottomleft_button.player_on = False
    bottomright_button.player_x = False
    bottomright_button.player_o = False
    bottomright_button.player_on = False
    
def click_button():
    global turn, start_menu, game, x_win, o_win, draw
    if central_button.x + central_button.width > mouse_pos[0] > central_button.x and central_button.y + central_button.height > mouse_pos[1] > central_button.y:
        if mouse_click:
            if start_menu:
                start_menu = False
                game = True
                turn = True
                x_win = False
                o_win = False
                draw = False
            else:
                if turn == True and central_button.player_on == False:
                    central_button.player_on = True
                    turn = False
                    central_button.player_x = True
                if turn == False and central_button.player_on == False:
                    central_button.player_on = True
                    turn = True
                    central_button.player_o = True
    if sideleft_button.x + sideleft_button.width > mouse_pos[0] > sideleft_button.x and sideleft_button.y + sideleft_button.height > mouse_pos[1] > sideleft_button.y:
        if mouse_click:
            if start_menu:
                start_menu = False
                game = True
                turn = True
                x_win = False
                o_win = False
                draw = False
            else:
                if turn == True and sideleft_button.player_on == False:
                    sideleft_button.player_on = True
                    turn = False
                    sideleft_button.player_x = True
                if turn == False and sideleft_button.player_on == False:
                    sideleft_button.player_on = True
                    turn = True
                    sideleft_button.player_o = True
    if sideright_button.x + sideright_button.width > mouse_pos[0] > sideright_button.x and sideright_button.y + sideright_button.height > mouse_pos[1] > sideright_button.y:
        if mouse_click:
            if start_menu:
                start_menu = False
                game = True
                turn = True
                x_win = False
                o_win = False
                draw = False
            else:
                if turn == True and sideright_button.player_on == False:
                    sideright_button.player_on = True
                    turn = False
                    sideright_button.player_x = True
                if turn == False and sideright_button.player_on == False:
                    sideright_button.player_on = True
                    turn = True
                    sideright_button.player_o = True
        
    if topcentral_button.x + topcentral_button.width > mouse_pos[0] > topcentral_button.x and topcentral_button.y + topcentral_button.height > mouse_pos[1] > topcentral_button.y:
        if mouse_click:
            if start_menu:
                start_menu = False
                game = True
                turn = True
                x_win = False
                o_win = False
                draw = False
            else:
                if turn == True and topcentral_button.player_on == False:
                    topcentral_button.player_on = True
                    turn = False
                    topcentral_button.player_x = True
                if turn == False and topcentral_button.player_on == False:
                    topcentral_button.player_on = True
                    turn = True
                    topcentral_button.player_o = True
    if topleft_button.x + topleft_button.width > mouse_pos[0] > topleft_button.x and topleft_button.y + topleft_button.height > mouse_pos[1] > topleft_button.y:
        if mouse_click:
            if start_menu:
                start_menu = False
                game = True
                turn = True
                x_win = False
                o_win = False
                draw = False
            else:
                if turn == True and topleft_button.player_on == False:
                    topleft_button.player_on = True
                    turn = False
                    topleft_button.player_x = True
                if turn == False and topleft_button.player_on == False:
                    topleft_button.player_on = True
                    turn = True
                    topleft_button.player_o = True
    if topright_button.x + topright_button.width > mouse_pos[0] > topright_button.x and topright_button.y + topright_button.height > mouse_pos[1] > topright_button.y:
        if mouse_click:
            if start_menu:
                start_menu = False
                game = True
                turn = True
                x_win = False
                o_win = False
                draw = False
            else:
                if turn == True and topright_button.player_on == False:
                    topright_button.player_on = True
                    turn = False
                    topright_button.player_x = True
                if turn == False and topright_button.player_on == False:
                    topright_button.player_on = True
                    turn = True
                    topright_button.player_o = True

    if bottomcentral_button.x + bottomcentral_button.width > mouse_pos[0] > bottomcentral_button.x and bottomcentral_button.y + bottomcentral_button.height > mouse_pos[1] > bottomcentral_button.y:
        if mouse_click:
            if start_menu:
                start_menu = False
                game = True
                turn = True
                x_win = False
                o_win = False
                draw = False
            else:
                if turn == True and bottomcentral_button.player_on == False:
                    bottomcentral_button.player_on = True
                    turn = False
                    bottomcentral_button.player_x = True
                if turn == False and bottomcentral_button.player_on == False:
                    bottomcentral_button.player_on = True
                    turn = True
                    bottomcentral_button.player_o = True
    if bottomleft_button.x + bottomleft_button.width > mouse_pos[0] > bottomleft_button.x and bottomleft_button.y + bottomleft_button.height > mouse_pos[1] > bottomleft_button.y:
        if mouse_click:
            if start_menu:
                start_menu = False
                game = True
                turn = True
                x_win = False
                o_win = False
                draw = False
            else:
                if turn == True and bottomleft_button.player_on == False:
                    bottomleft_button.player_on = True
                    turn = False
                    bottomleft_button.player_x = True
                if turn == False and bottomleft_button.player_on == False:
                    bottomleft_button.player_on = True
                    turn = True
                    bottomleft_button.player_o = True
    if bottomright_button.x + bottomright_button.width > mouse_pos[0] > bottomright_button.x and bottomright_button.y + bottomright_button.height > mouse_pos[1] > bottomright_button.y:
        if mouse_click:
            if start_menu:
                start_menu = False
                game = True
                turn = True
                x_win = False
                o_win = False
                draw = False
            else:
                if turn == True and bottomright_button.player_on == False:
                    bottomright_button.player_on = True
                    turn = False
                    bottomright_button.player_x = True
                if turn == False and bottomright_button.player_on == False:
                    bottomright_button.player_on = True
                    turn = True
                    bottomright_button.player_o = True

while run:

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.MOUSEBUTTONDOWN
    mouse_clicked = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == mouse_click and event.button == 1:
            click_button()
    
    if central_button.player_x and sideleft_button.player_x and sideright_button.player_x:
        game = False
        x_win = True
        x_score += 1
    if topcentral_button.player_x and topleft_button.player_x and topright_button.player_x:
        game = False
        x_win = True
        x_score += 1
    if bottomcentral_button.player_x and bottomleft_button.player_x and bottomright_button.player_x:
        game = False
        x_win = True
        x_score += 1
    if topleft_button.player_x and sideleft_button.player_x and bottomleft_button.player_x:
        game = False
        x_win = True
        x_score += 1
    if topcentral_button.player_x and central_button.player_x and bottomcentral_button.player_x:
        game = False
        x_win = True
        x_score += 1
    if topright_button.player_x and sideright_button.player_x and bottomright_button.player_x:
        game = False
        x_win = True
        x_score += 1
    if topright_button.player_x and central_button.player_x and bottomleft_button.player_x:
        game = False
        x_win = True
        x_score += 1
    if topleft_button.player_x and central_button.player_x and bottomright_button.player_x:
        game = False
        x_win = True
        x_score += 1

    if central_button.player_o and sideleft_button.player_o and sideright_button.player_o:
        game = False
        o_win = True
        o_score += 1
    if topcentral_button.player_o and topleft_button.player_o and topright_button.player_o:
        game = False
        o_win = True
        o_score += 1
    if bottomcentral_button.player_o and bottomleft_button.player_o and bottomright_button.player_o:
        game = False
        o_win = True
        o_score += 1
    if topleft_button.player_o and sideleft_button.player_o and bottomleft_button.player_o:
        game = False
        o_win = True
        o_score += 1
    if topcentral_button.player_o and central_button.player_o and bottomcentral_button.player_o:
        game = False
        o_win = True
        o_score += 1
    if topright_button.player_o and sideright_button.player_o and bottomright_button.player_o:
        game = False
        o_win = True
        o_score += 1
    if topright_button.player_o and central_button.player_o and bottomleft_button.player_o:
        game = False
        o_win = True
        o_score += 1
    if topleft_button.player_o and central_button.player_o and bottomright_button.player_o:
        game = False
        o_win = True
        o_score += 1

    if central_button.player_on and sideleft_button.player_on and sideright_button.player_on and topcentral_button.player_on and topleft_button.player_on and topright_button.player_on and bottomcentral_button.player_on and bottomleft_button.player_on and bottomright_button.player_on:
        if not x_win and not o_win: 
            game = False
            draw = True 

    if x_win:
        game = False
        start_menu = True
        restart()
    if o_win:
        game = False
        start_menu = True
        restart()
    if draw:
        game = False
        start_menu = True
        restart()

    win.fill((0,0,0))
    x_scoreboard = font.render("X: {}".format(x_score), 1, (255,255,255))
    o_scoreboard = font.render("O: {}".format(o_score), 1, (255,255,255))
    win.blit(x_scoreboard, (0,0))
    win.blit(o_scoreboard, (screen_width - o_scoreboard.get_rect().width,0))
    if start_menu:
        if not x_win and not o_win and not draw:
            title = font.render("Tris!", 1, (255,255,255))
            win.blit(title, (title.get_rect(center=(screen_width/2, 40))))
        if x_win:
            title = font.render("Player X Win!", 1, (255,255,255))
            win.blit(title, (title.get_rect(center=(screen_width/2, 40))))
        if o_win:
            title = font.render("Player O Win!", 1, (255,255,255))
            win.blit(title, (title.get_rect(center=(screen_width/2, 40))))
        if draw:
            title = font.render("Draw!", 1, (255,255,255))
            win.blit(title, (title.get_rect(center=(screen_width/2, 40))))
        start = font.render("Start", 1, (255,255,255))
        win.blit(start, (235,235))
        create_table()
    if game == True:
        create_table()
        if turn == True:
            turn_screen = font.render("X Turn", 1, (255,255,255))
            win.blit(turn_screen, (turn_screen.get_rect(center=(screen_width/2, 20))))
        if turn == False:
            turn_screen = font.render("O Turn", 1, (255,255,255))
            win.blit(turn_screen, (turn_screen.get_rect(center=(screen_width/2, 20))))
        if central_button.player_x == True:
            win.blit(x, (220, 220))
        if central_button.player_o == True:
            win.blit(o, (220, 220))
        if sideleft_button.player_x == True:
            win.blit(x, (120, 220))
        if sideleft_button.player_o == True:
            win.blit(o, (120, 220))
        if sideright_button.player_x == True:
            win.blit(x, (320, 220))
        if sideright_button.player_o == True:
            win.blit(o, (320, 220))
        if topcentral_button.player_x == True:
            win.blit(x, (220, 120))
        if topcentral_button.player_o == True:
            win.blit(o, (220, 120))
        if topleft_button.player_x == True:
            win.blit(x, (120, 120))
        if topleft_button.player_o == True:
            win.blit(o, (120, 120))
        if topright_button.player_x == True:
            win.blit(x, (320, 120))
        if topright_button.player_o == True:
            win.blit(o, (320, 120))
        if bottomcentral_button.player_x == True:
            win.blit(x, (220, 320))
        if bottomcentral_button.player_o == True:
            win.blit(o, (220, 320))
        if bottomleft_button.player_x == True:
            win.blit(x, (120, 320))
        if bottomleft_button.player_o == True:
            win.blit(o, (120, 320))
        if bottomright_button.player_x == True:
            win.blit(x, (320, 320))
        if bottomright_button.player_o == True:
            win.blit(o, (320, 320))
    pygame.display.update()

pygame.quit()