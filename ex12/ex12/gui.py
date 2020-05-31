import tkinter as tki
import time
from tkinter import messagebox
from winsound import *
import tkinter.font as font


WIDTH = 900
HEIGHT = 600


class Gui:
    """
    This class defines all the visual pages of the game (open page,
    game page and end page and mannaging the game itself).
    """
    def __init__(self, maingame, root, game, player1, player2):
        # defines the players buttons pictures in the first page
        self.img1 = tki.PhotoImage(file="ex12/button1.png")
        self.img2 = tki.PhotoImage(file="ex12/button2.png")
        self.img3 = tki.PhotoImage(file="ex12/button3.png")
        self.img4 = tki.PhotoImage(file="ex12/button4.png")
        # defines the sounds
        self.play1 = lambda: PlaySound('ex12/statboy.wav', SND_FILENAME)
        self.play2 = lambda: PlaySound('ex12/benel.wav', SND_FILENAME)
        # defines the players options buttons pictures in the first page
        self.play_img = tki.PhotoImage(file="ex12/play.png")
        self.exit_img = tki.PhotoImage(file="ex12/exit.png")
        self.yes_img = tki.PhotoImage(file="ex12/yes.png")
        self.no_img = tki.PhotoImage(file="ex12/no.png")

        self.root = root
        self.game = game
        self.maingame = maingame
        self.player1 = player1
        self.player2 = player2
        self.player_dict = {"1": self.player1,
                             "2": self.player2}
        # Creates dictionary with the data of the game board pixels
        self.pixel_dict_x = {'0': 248, '1': 303, '2': 358, '3': 413,
                             '4': 468, '5': 523, '6': 578}
        self.pixel_dict_y = {'0': 30, '1': 85, '2': 140, '3': 195,
                             '4': 250, '5': 305}
        # defines all the game frames
        self.main_frame = tki.Frame(root)  # defines main container
        self.main_frame.pack(side="top", fill="both", expand=True)
        start_frame = tki.Frame(self.main_frame, name="startframe")
        game_frame = tki.Frame(self.main_frame, name="gameframe")
        end_frame = tki.Frame(self.main_frame, name="endframe")
        # inserts all the frames info into a dictionary.
        self.pages_dict = {"startframe": start_frame, "gameframe": game_frame,
                           "endframe": end_frame}
        # defines the spreading of the different frames.
        for frame in list(self.pages_dict.values()):
            frame.grid(row=0, column=0, sticky='nsew')
        # creates all the windows and inserts them into dict_frame:
        self.create_start_page(start_frame)
        self.create_game_page(game_frame)
        self.create_end_page(end_frame)
        self.counter = 0  # later help to add the winning song
        # shows the first frame:
        self.show_frame("startframe")
        tki.messagebox.showinfo("Ben-El & Static 'Four in a Row' Game",
                                "Welcome to the fans club of Static & "
                                "Ben-El!!!\n"
                                "Fasten your seat belt because we are taking"
                                " off to the HALAL - KALLLLL!\n"
                                "Game rules:\n"
                                "1) Choose 2 players, one player for each "
                                "singer.\n"
                                "2) After choosing 2 players the 'Play' "
                                "button will be available. Press 'Play' in "
                                "order to play and 'Exit' in order to exit "
                                "the game.\n"
                                "3) When it is your turn to play you can "
                                "press the column button which you whould "
                                "like the disc will enter in.\n"
                                "Press 'play' in order to restart the whole "
                                "game, and 'Exit' in order to exit the "
                                "game.\n"
                                "After finish the game, in the final page "
                                "you can start new game by pressing 'Yes', "
                                "and exit the game by pressing 'No'.\n"
                                "HAVE FUN!")
        # defult font size of game
        font.nametofont('TkDefaultFont').configure(size=12)

    def show_frame(self, page_name):
        """
        Description: This method shows the relevant page in the front of
        the screen.
        :param page_name: frame object
        :return: None
        """
        frame = self.pages_dict.get(page_name)  # takes the window from the
        # pages dictionary
        frame.tkraise()  # raises the layer that we want to the front
        # If you want to show gameframe itself then start the first turn
        if page_name == "gameframe":  # play best song ever!
            ## TODO THIS IS FOR THE VERSION WITH MUSIC THAT WE SENT IN MAIL
            PlaySound("ex12/gamesong.wav", SND_ASYNC | SND_ALIAS)
            self.is_game_over()


    def is_game_over(self):
        """
        Description: This method checks if the game ended or did not,
        and call the matching methods.
        :return: None
        """
        winner = self.game.get_winner()
        if winner == None:
            # the game did not end, continue to another turn
            self.run_single_turn()
        else:
            # show a small label of how wonn
            if self.counter == 0:  # in the first time you entered this func
                # play the winning song! yasso!!!!!!
                # TODO THIS IS FOR THE VERSION WITH MUSIC THAT WE SENT IN MAIL
                PlaySound("ex12/winsong.wav", SND_ASYNC | SND_ALIAS)
                # show a line in place of the winning balls
                cor_list = self.game.find_win_coordinates()
                y1 = self.pixel_dict_y.get(str(cor_list[0][0]))
                x1 = self.pixel_dict_x.get(str(cor_list[0][1]))
                y2 = self.pixel_dict_y.get(str(cor_list[1][0]))
                x2 = self.pixel_dict_x.get(str(cor_list[1][1]))
                self.open_canvas.create_line(x1+20, y1+10, x2+20, y2+10,
                                             dash=(4, 2), fill="white")
                # self.open_canvas.create_line(y1+10,x1+20,y2+10,x2+20,
                #                              dash=(4, 2), fill="white")
                self.counter += 1
            else:
                self.winner() # call the function that show the last screen


    def run_single_turn(self):
        """
        Description: This method runs in loop during the whole game.
        :return: None
        """
        player_string = str(self.game.get_current_player())
        self.visual_player_turn(player_string)
        player_object = self.player_dict.get(player_string)
        if player_object.get_current_player_brain() == "ai":
            time.sleep(1)  # create a dramatick pause
            current_brain = player_object.get_ai_brain()
            move_number = current_brain.find_legal_move()
            self.click_button(move_number)

    def winner(self):
        """show the winners frame"""
        win_msg = {"0": "its a tie!!!",
                   "1": "ben el won! yay!",
                   "2": "static won! kall!"}
        winner = str(self.game.get_winner())
        time.sleep(1.5)
        self.show_frame("endframe")
        lable = tki.Label(self.main_frame,
                          text=win_msg.get(winner), font=("Helvetica", 32))
        lable.place(x=290, y=290)


    def visual_player_turn(self, player_string):
        """
        Description: This method creates visual representation of the current
         player turn.
        :param player_string: str
        :return: None
        """
        temp_dict = {"1": "בן - אל", "2": "סטטיק"}
        if player_string == "1":
            color_pic = tki.PhotoImage(file="ex12/purple_ball.png")
        elif player_string == "2":
            color_pic = tki.PhotoImage(file="ex12/blue_ball.png")
        name = tki.Label(self.open_canvas, text=temp_dict.get(player_string))
        name.place(x=97, y=160)
        self.open_canvas.color_pic = color_pic  # Keep a reference in
        # case this code is put in a function.
        self.open_canvas.create_image(95, 100, anchor=tki.NW, image=color_pic)

    def create_start_page(self, mom_frame):
        """
        Description: This method creates the start game page.
        :param mom_frame: frame object
        :return: None
        """
        open_canvas = tki.Canvas(mom_frame,
                                 height=HEIGHT, width=WIDTH, bg="black")
        # pack the canvas into a frame/form
        open_canvas.pack(expand="yes", fill="both")
        # load the .gif image file
        img = tki.PhotoImage(file="ex12/game1.png")
        open_canvas.background = img  # Keep a reference in case this
        # code is put in a function.
        background = open_canvas.create_image(0, 0, anchor=tki.NW, image=img)
        self.start_page_buttons(mom_frame)

    def start_page_buttons(self, mom_frame):
        """
        Description: This method defines the buttons (players, exit and
        play) and connects them to the relevant page.
        :param mom_frame: obj
        :param canvas: obj
        :return: None
        """
        players_list = []
        # defines the ben el human being
        self.b_ben_el = tki.Button(mom_frame, image=self.img3, border=0,
                                   command=lambda: self.buttons_actions(
                                       players_list, "1"))
        self.b_ben_el.place(x=670, y=153)
        # defines the ben el ai player
        self.b_ben_ai = tki.Button(mom_frame, image=self.img4, border=0,
                                   command=lambda: self.buttons_actions(
                                       players_list, "2"))
        self.b_ben_ai.place(x=670, y=227)
        # defines the static human being
        self.b_stat = tki.Button(mom_frame, image=self.img1, border=0,
                                 command=lambda: self.buttons_actions(
                                     players_list,"3"))
        self.b_stat.place(x=35, y=153)
        # defines the static ai player
        self.b_stat_ai = tki.Button(mom_frame, image=self.img2, border=0,
                                    command=lambda: self.buttons_actions(
                                        players_list, "4"))
        self.b_stat_ai.place(x=35, y=227)
        # defines the exit button
        b_exit = tki.Button(mom_frame, image=self.exit_img, border=0,
                            command=self.root.destroy)
        b_exit.place(x=550, y=533)

        # play: is shown only after choosing two different players
        self.b_play = tki.Button(mom_frame, image=self.play_img, border=0,
                                 command=lambda: self.show_frame("gameframe"))
        self.b_play.config(state='disabled')
        self.b_play.place(x=215, y=533)

    def buttons_actions(self, players_list, player_num):
        """
        Description: This method defines the players buttons in the first
        page.
        :param players_list: list
        :param player_num: str
        :return: None
        """
        if player_num not in players_list:
            players_list.append(player_num)
            # Add item to list if not already exists
        if player_num == "1" or player_num == "2":
            self.play2()  # play static song
            if player_num == "1":
                self.player1.set_player_brain("boy")
                self.b_ben_ai.config(state='disabled')
            if player_num == "2":
                self.player1.set_player_brain("ai")
                self.b_ben_el.config(state='disabled')

        if player_num == "3" or player_num == "4":
            self.play1()  # play static song
            if player_num == "3":
                self.player2.set_player_brain("boy")
                self.b_stat_ai.config(state='disabled')
            if player_num == "4":
                self.player2.set_player_brain("ai")
                self.b_stat.config(state='disabled')
        # play: is shown only after choosing two different players
        if len(players_list) == 2:
            self.b_play.config(state="normal")

    def create_game_page(self, mom_frame):
        """
        Description: This method defines the game page.
        :param mom_frame: obj
        :return: None
        """
        self.container = tki.Frame(mom_frame)  # Creates main container
        self.container.pack()
        self.open_canvas = tki.Canvas(self.container, height=HEIGHT,
                                      width=WIDTH, bg="black")

        # packs the canvas into a frame/form
        self.open_canvas.pack(expand="yes", fill="both")
        # loads the .gif image file
        img = tki.PhotoImage(file="ex12/game2.png")
        self.open_canvas.background = img  # Defines the image as a background
        background = self.open_canvas.create_image(0, 0, anchor=tki.NW,
                                                   image=img)
        # Put a tkinter widget on the canvas.
        filename = tki.PhotoImage(file="ex12/board.png")
        self.open_canvas.image = filename
        self.board = self.open_canvas.create_image(210, 0, anchor=tki.NW,
                                                   image=filename)
        self.create_buttons(self.open_canvas)
        # play page
        b_play = tki.Button(mom_frame, image=self.play_img, border=0,
                            command=lambda: self.click_start_new_game())
        b_play.place(x=220, y=533)
        # exit page
        b_exit = tki.Button(mom_frame, image=self.exit_img, border=0,
                            command=self.root.destroy)
        b_exit.place(x=550, y=533)

    def create_buttons(self, canvas):
        """
        Description: This method creates the columns buttons of the board.
        :param canvas: obj
        :return: None
        """
        self.button1 = tki.Button(self.container, text="1", command=lambda:
        self.click_button(0))
        canvas.create_window(265, 380, window=self.button1, anchor=tki.NW)
        self.button2 = tki.Button(self.container, text="2", command=lambda:
        self.click_button(1))
        canvas.create_window(320, 380, window=self.button2, anchor=tki.NW)
        self.button3 = tki.Button(self.container, text="3", command=lambda:
        self.click_button(2))
        canvas.create_window(375, 380, window=self.button3, anchor=tki.NW)
        self.button4 = tki.Button(self.container, text="4", command=lambda:
        self.click_button(3))
        canvas.create_window(430, 380, window=self.button4, anchor=tki.NW)
        self.button5 = tki.Button(self.container, text="5", command=lambda:
        self.click_button(4))
        canvas.create_window(485, 380, window=self.button5, anchor=tki.NW)
        self.button6 = tki.Button(self.container, text="6", command=lambda:
        self.click_button(5))
        canvas.create_window(540, 380, window=self.button6, anchor=tki.NW)
        self.button7 = tki.Button(self.container, text="7", command=lambda:
        self.click_button(6))
        canvas.create_window(595, 380, window=self.button7, anchor=tki.NW)
        self.button_list = [self.button1, self.button2, self.button3,
                            self.button4, self.button5, self.button6,
                            self.button7]

    def click_button(self, button_num):
        """
        Description: This method checks whether the move can be performed
        by the button number which have been pressed.
        :param button_num: int
        :return: None
        """
        try:
            row_num = self.game.make_move(button_num)
            current_player = self.game.get_current_player()
        except:
            tki.messagebox.showinfo("Error", "You have an error, "
                                             "Pleas enter valid column.")
        else:
            self.main_frame.after(2000, self.create_ball(current_player,
                                                         button_num, row_num))

    def create_ball(self, player, x_name, y_name):
        """
        Description: This method creates disc according the current player.
        :param player: str
        :param x_name: int
        :param y_name: int
        :return: None
        """
        # creates ball according the player
        x_cor = self.pixel_dict_x.get(str(x_name))
        for button in self.button_list:
            button.config(state='disabled')  # causes the button to become
            # not available
        if player == 1:
            color_pic = tki.PhotoImage(file="ex12/blue_ball.png")

        elif player == 2:
            color_pic = tki.PhotoImage(file="ex12/purple_ball.png")


        ball = self.open_canvas.create_image(x_cor, 0, anchor=tki.NW,
                                             image=color_pic)
        self.open_canvas.tag_raise(self.board)  # keeping the board on the
        #  top layer
        self.move_ball(ball, y_name)  # calling animation method in game
        # which defines the ball falling

    def move_ball(self, ball, y_name):
        """
        Description: This method creates the animation of the dropping ball on
        the canvas.
        :param ball: obj
        :param y_name: int
        :return: None
        """
        x_speed = 0
        y_speed = 5
        y_cor = self.pixel_dict_y.get(str(y_name))
        while True:
            self.open_canvas.move(ball, x_speed, y_speed)
            pos = self.open_canvas.coords(ball)  # [left,top,right,bottom]
            if pos[1] >= y_cor:
                y_speed = 0
                for button in self.button_list:
                    button.config(state='normal')  # return all butto
                self.is_game_over()  # at the end of every turn check
            self.container.update()
            time.sleep(0.01)  # slow motion so that the move

    def create_end_page(self, mom_frame):
        """
        Description: This method defines the end page.
        :param mom_frame: obj
        :return: None
        """
        open_canvas = tki.Canvas(mom_frame,
                                 height=HEIGHT, width=WIDTH, bg="black")
        # pack the canvas into a frame/form
        open_canvas.pack(expand="yes", fill="both")
        # load the .gif image file
        img = tki.PhotoImage(file="ex12/game3.png")
        open_canvas.background = img  # Keep a reference in case this code
        #  is put in a function.
        background = open_canvas.create_image(0, 0, anchor=tki.NW, image=img)
        # do you want to play again? YES: - restart the whole game
        b_play = tki.Button(mom_frame, image=self.yes_img, border=0,
                            command=lambda: self.click_start_new_game())
        b_play.place(x=450, y=533)
        # do you want to play again? NO - exit the game
        b_exit = tki.Button(mom_frame, image=self.no_img, border=0,
                            command=self.root.destroy)
        b_exit.place(x=550, y=533)

    def click_start_new_game(self):
        """
        Description: This method creates new game.
        :return: None
        """
        PlaySound(None, SND_ASYNC | SND_ALIAS)
        self.main_frame.destroy()
        self.maingame.restart_game()
        self.maingame.gui_go()
