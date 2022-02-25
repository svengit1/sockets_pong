from ast import excepthandler
import socket
from _thread import *
import pickle
from player import Player
from ball import Ball

server = "192.168.1.4"
port = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen()
players = [Player(50, 50, (255, 0, 0), 0), Player(700, 50, (0, 0, 255), 1)]
ball = Ball(300, 300)
def threaded_client(conn, p):
    global curr_player
    conn.send(pickle.dumps(players[p]))
    #[player, ball, scored]
    while True:
        reply = []
        try:    
            data = pickle.loads(conn.recv(2048))
            players[p] = data
            if not data:
                print("Disconected, no data")
                break
            else:
                if p == 1:
                    reply.append(players[0])
                else:
                    reply.append(players[1])
                # print("reciveved", data)
                # print("sending", reply)

                if ball.y + ball.rad > 520:
                    ball.change_direction("y")
                if ball.y - ball.rad < 0:
                    ball.change_direction("y")
                if ball.x + ball.rad > players[1].x and players[1].y < ball.y < players[1].y + players[1].height:
                    ball.change_direction("x")
                    ball.increment_speed()
                if ball.x - ball.rad < players[0].x + players[0].width and players[0].y < ball.y < players[0].y + players[0].height:
                    ball.change_direction("x")
                    ball.increment_speed()
                if curr_player == 2:
                    ball.move()
                reply.append(ball)

                if ball.x < 0:
                    reply.append((1, players[1]))
                    players[p].detected_score = True
                elif ball.x > 820:
                    reply.append((1, players[0]))
                    players[p].detected_score = True
                else:
                    reply.append((None, None))
                if players[0].detected_score and players[1].detected_score:
                    ball.__init__(300, 300)
                    players[0].detected_score = False
                    players[1].detected_score = False

            conn.sendall(pickle.dumps(reply))
        except:
            break
    curr_player -= 1
    print("Lost connection")
    conn.close()

curr_player = 0
while True:
    if curr_player < 2:
        conn, addr = s.accept()
        print("Connected to", addr)
        start_new_thread(threaded_client, (conn, curr_player))
        curr_player += 1