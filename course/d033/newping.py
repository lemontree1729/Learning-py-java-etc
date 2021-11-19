from tkinter import *
from threading import Timer
from random import randint

# import table, ball

# global variables
g_vx, g_vy = 10, 0  # x, y coord of initial speed
score_left, score_right = 0, 0
first_serve = True


class Table:
    def __init__(self, master, width, height, bg, net_color, net_op):
        self.width, self.height = width, height
        self.canvas = Canvas(master, width=self.width, height=self.height, bg=bg)
        self.canvas.pack()
        if net_op == "vertical":
            self.canvas.create_line(self.width / 2, 0, self.width / 2, self.height, width=2,
            fill=net_color, dash=(15, 23))  # fmt: skip
        else:
            self.canvas.create_line(0, self.height / 2, self.width, self.height / 2, width=2,
            fill=net_color, dash=(15, 23))  # fmt: skip
        self.scoreboard = self.canvas.create_text(300, 65, font=("monaco", 72), fill="darkgreen")  # fmt: skip

    # add score to scoreboard
    def draw_score(self, left, right):
        scores = str(right) + "  " + str(left)
        self.canvas.itemconfigure(self.scoreboard, text=scores)


class Ball:
    def __init__(self, table: Table, radius, color, vx, vy, x, y):
        self.radius = radius
        self.x_start, self.y_start = x, y
        self.vx, self.vy = vx, vy
        self.canvas = table.canvas
        self.circle = self.canvas.create_oval(
            x, y, x + 2 * radius, y + 2 * radius, fill=color
        )
        ##### strange error!!!!
        print(self.getcord())

    def getcord(self):
        return self.canvas.coords(self.circle)

    def move_next(self):
        print(self.vx, self.vy)
        y = self.getcord()[1]
        xmove, ymove = self.vx, self.vy
        uplimit = 3
        if y + self.vy <= uplimit:
            ymove = uplimit - y
            self.vy *= -1
        downlimit = self.canvas.winfo_height() - (self.radius * 2 - 3)
        if y + self.vy >= downlimit:
            ymove = downlimit - y
            self.vy *= -1
        self.canvas.move(self.circle, xmove, ymove)

    def start_position(self):
        self.canvas.moveto(self.circle, self.x_start, self.y_start)

    def start_ball(self, vx, vy):
        self.vx = -vx if randint(0, 1) else vx
        self.vy = -vy if randint(0, 1) else vy
        self.start_position()

    def stop_ball(self):
        self.vx, self.vy = 0, 0


class Bat:
    def __init__(self, table: Table, width, height, x, y, color, vx=23, vy=23):
        self.width, self.height = width, height
        self.x_start, self.y_start = x, y
        self.vx, self.vy = vx, vy
        self.canvas = table.canvas
        self.rectangle = self.canvas.create_rectangle(
            x, y, x + width, y + height, fill=color
        )

    def getcord(self):
        return self.canvas.coords(self.rectangle)

    def detect_collision(self, ball, side_relative=True, topbottom_relative=False):
        collision_direction = ""  # 충돌 방향 저장
        collision = False  # 충돌이 감지되면 True 로 바뀜
        feel = 5  # sensitivity
        # varible for bet:
        left, top, right, bottom = self.getcord()
        h_center, w_center = (top + bottom) / 2, (right + left) / 2
        # varible for ball:
        left_b, top_b, right_b, bottom_b = ball.getcord()
        h_center_b, w_center_b = (top_b + bottom_b) / 2, (right_b + left_b) / 2
        # collision check
        if (bottom_b > top) and (top_b < bottom):
            if (right_b > left) and (left_b < right):
                collision = True
                print("collision")

        if collision:
            # guess direction of collision
            if top < h_center_b < bottom:
                ball.vx *= -1
                if right <= w_center_b:
                    collision_direction = "Right"
                elif w_center_b <= left:
                    collision_direction = "Left"
            elif left < w_center_b < right:
                ball.vy *= -1
                if bottom <= h_center_b:
                    collision_direction = "Down"
                elif h_center_b <= top:
                    collision_direction = "Up"
            else:
                collision_direction = "miss"
            # give relative speed to side or topbottom
            if side_relative and collision_direction in ("Right", "Left"):
                adjustment = (-(h_center - h_center_b)) / ((bottom - top) / 2)
                ball.vy = feel * adjustment
            if topbottom_relative and collision_direction in ("Up", "Down"):
                adjustment = (-(w_center - w_center_b)) / ((right - left) / 2)
                ball.vx = feel * adjustment
            return (collision, collision_direction)

    def move_up(self, event):  # method to bind
        uplimit = 0
        y = self.getcord()[1]
        ymove = -self.vy
        if y - self.vy <= uplimit:
            ymove = uplimit - y
        self.canvas.move(self.rectangle, 0, ymove)

    def move_down(self, event):  # method to bind
        downlimit = self.canvas.winfo_height - self.height
        y = self.getcord()[1]
        ymove = self.vy
        if y + self.vy >= downlimit:
            ymove = downlimit - y
        self.canvas.move(self.rectangle, 0, ymove)

    def start_position(self):
        self.canvas.moveto(self.rectangle, self.x_start, self.y_start)


# game running function
def game_flow():
    global first_serve, score_left, score_right

    # make ball stop while restart game
    if first_serve == True:
        my_ball.stop_ball()
        first_serve = False

    # collision check and give relative speed
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)

    # check collision with left wall
    if my_ball.getcord()[0] <= 3:
        my_ball.stop_ball()
        # initalize ball and bat
        my_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        score_left += 1
        # show "W"(Win) when left get more than 5 score
        if score_left >= 5:
            score_left = "W"
            score_right = "L"
        first_serve = True
        my_table.draw_score(score_left, score_right)

    # check collision with right wall
    if my_ball.getcord()[0] + my_ball.radius * 2 >= my_table.width - 3:
        my_ball.stop_ball()
        my_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        score_right += 1
        if score_right >= 5:
            score_right = "W"
            score_left = "L"
        first_serve = True
        my_table.draw_score(score_left, score_right)

    my_ball.move_next()
    master.after(30, game_flow)  # recursion with 30 ms delay


# start or restart game
def restart_game(event):
    global score_left, score_right
    my_ball.start_ball(g_vx, g_vy)
    if score_left == "W" or score_left == "L":
        score_left, score_right = 0, 0
    my_table.draw_score(score_left, score_right)


# main
master = Tk()
master.title("MyPingPong")

# make table, ball, bat
my_table = Table(master, 600, 400, "black", "green", "vertical")
my_ball = Ball(table=my_table, radius=12, x=288, y=188, vx=0, vy=0, color="red")
bat_L = Bat(table=my_table, width=15, height=100, x=20, y=150, color="blue")
bat_R = Bat(table=my_table, width=15, height=100, x=575, y=150, color="yellow")

# bind keys
master.bind("w", bat_L.move_up)
master.bind("s", bat_L.move_down)
master.bind("<Up>", bat_R.move_up)
master.bind("<Down>", bat_R.move_down)
# you should press spacebar to start!
master.bind("<space>", restart_game)

# run game
game_flow()

master.mainloop()
