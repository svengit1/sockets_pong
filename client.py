import pygame
import pickle
from network import Network

pygame.init()

screenW = 820
screenH = 520

win = pygame.display.set_mode((screenW, screenH))

clock = pygame.time.Clock()
pygame.display.set_caption('catch cube')



def redrawGameWindow(win, player1, player2, ball):
    win.fill((0, 0, 0))
    player1.draw(win)
    player2.draw(win)
    ball.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    p = n.getP()
    #[player, ball, scored]
    while run:
        clock.tick(30)
        data = n.send((p))
        p2 = data[0]
        ball = data[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        p.move()
        if data[2][0]:
            if data[2][1].id != p.id:
                print("The opponent scored a goal!")
                print('You', p.points, "Opponenet", p2.points + 1)
            else:
                print("You scored a goal!")
                p.increment_score()
                print('You', p.points, "Opponenet", p2.points)
        redrawGameWindow(win, p, p2, ball)

main()
pygame.quit()