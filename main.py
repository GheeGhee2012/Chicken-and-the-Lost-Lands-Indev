 # Welcome To Chicken and the lost lands
# These are the requirements
# You will need python 3 and PySimpleGUI in cmd/terminal write "pip install PySimpleGUI"

# Imports
import turtle
import PySimpleGUI as sg
import random

# On startup
setting_open = False
item_selected = None
inventory_open = False
level = 1
direction = None

# Launcher and Window Creation
launcher_layout = [[sg.Text("!Run Game?( INDEV V0.2)!")], [sg.Button("Close"), sg.Button('Run Indev')]]

wn = sg.Window("    CATLL Launcher",launcher_layout, size = (300, 200))
event, value = wn.read()
wn.close()

if event!='Close':
  
  wn = turtle.Screen()
  wn.setup(600, 500)
  wn.bgcolor("green")
  wn.title("Chicken and the Lost Lands")
  wn.tracer(0)
  
  wn.addshape("settings_icon.gif")
  wn.addshape("player_icon.gif")
  wn.addshape("Assets/Images/sheep.gif")
  wn.addshape("Assets/Images/pond.gif")
  wn.addshape("Assets/Images/fish.gif")
  wn.addshape("Assets/Images/farm.gif")

  entity3 = turtle.Turtle()
  entity3.shape("Assets/Images/pond.gif")
  entity3.penup()
  entity3.goto(180, -200)

  player = turtle.Turtle()
  player.shape("player_icon.gif")
  player.penup()
  player.goto(0, 0)

  entity = turtle.Turtle()
  entity.penup()
  entity.hideturtle()

  entity2 = turtle.Turtle()
  entity2.penup()
  entity2.hideturtle()
  
  settings_icon = turtle.Turtle()
  settings_icon.shape("settings_icon.gif")
  settings_icon.penup()
  settings_icon.goto(270, 220)
  
  pen = turtle.Turtle()
  pen.hideturtle()
  pen.penup()
  pen.goto(-280, 235)

  # Def creation and controls
  def go_up():
    global setting_open
    if not setting_open:
      player.setheading(90)
      player.forward(5)
  
  def go_down():
    global setting_open
    if not setting_open:
      player.setheading(270)
      player.forward(5)
  
  def go_left():
    global setting_open
    if not setting_open:
      player.setheading(180)
      player.forward(5)
  
  def go_right():
    global setting_open
    if not setting_open:
      player.setheading(0)
      player.forward(5)

  def QUIT_GAME():
    pass
  
  class Turtle_Editor(turtle.Turtle):
    def delete_on_click(self, x, y):
      self.hideturtle()
      global setting_open 
      setting_open = False

  def open_setting_menu(x,y):
    settings_layout = [
      [sg.Text("Paused. Press Resume To Resume")],[sg.Button("Resume")], [sg.Button("Quit Game(Button Still In development!)")]]
    
    wn = sg.Window("    Paused",settings_layout, size = (300, 200))
    event, value = wn.read()
    wn.close()
  
  def inventory():
    pass
  
  wn.listen()
  wn.onkeypress(go_up, "w")
  wn.onkeypress(go_down, "s")
  wn.onkeypress(go_left, "a")
  wn.onkeypress(go_right, "d")
  wn.onkeypress(inventory, "i")
  settings_icon.onclick(open_setting_menu)

# Game Loop
  running = True
  slowdown = 0
  while running:
    wn.update()
    if level == 1:
      entity.shape("Assets/Images/sheep.gif")
      entity2.shape("Assets/Images/sheep.gif")
      entity2.showturtle()
      entity.showturtle()
      if (slowdown%20)==0:
        entity.setheading(random.randint(0, 360))
        entity2.setheading(random.randint(0, 360))
      slowdown += 1
      entity.forward(1)
      entity2.forward(1)
      if entity3.distance(player) < 60:
        entity.hideturtle()
        entity2.hideturtle()
        entity3.hideturtle()
        entity.goto(0, 150)
        entity2.goto(0, -150)
        entity.setheading(0)
        entity2.setheading(0)
        player.goto(0, 0)
        level = 2
  
    if level == 2:
      wn.bgcolor("#3498DB")
      entity.shape("Assets/Images/fish.gif")
      entity2.shape("Assets/Images/fish.gif")
      entity.showturtle()
      entity2.showturtle()
      if (slowdown%20)==0:
        entity.setheading(random.randint(-45, 45))
        entity2.setheading(random.randint(-45, 45))
      slowdown += 1
      entity.forward(1)
      entity2.forward(1)
      if (entity.xcor()>280):
        entity.goto(-280, 150)
      if (entity2.xcor()>280):
        entity2.goto(-280, -150)
      if entity2.distance(player) < 20:
        level = 3
    
    if level == 3:
      wn.bgcolor("#AFEF53")
      entity2.hideturtle()
      entity.hideturtle()
      entity3.showturtle()
      entity3.shape("Assets/Images/farm.gif")
      entity3.goto(-250, -50)   
      if entity3.distance(player) < 55:
        level = 4

    if level == 4:
      wn.bgcolor("#27AE60")
      entity3.hideturtle()    