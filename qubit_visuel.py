import turtle
import math
import time

screen = turtle.Screen()
screen.title("Simulation Quantique - Sphère de Bloch")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0) 

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def dessiner_grille():
    t.pencolor("gray")
    t.pensize(1)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.circle(200)
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.goto(200, 0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.goto(0, 200)

def animer_qubit():
    gamma = 0.02 
    omega = 0.1  
    x, y = 1.0, 0.0
    echelle = 200
    t.penup()
    
    while math.sqrt(x**2 + y**2) > 0.05: 
        dx = (-omega * y - gamma * x)
        dy = (omega * x - gamma * y)
        x += dx
        y += dy
        
        try:
            t.clear()
            dessiner_grille()
            
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.pencolor("cyan")
            t.pensize(3)
            t.goto(x * echelle, y * echelle)
            
            t.dot(10, "red")
            
            t.penup()
            t.goto(-280, 250)
            t.pencolor("white")
            purete = math.sqrt(x**2 + y**2)
            t.write(f"Pureté : {purete:.3f}", font=("Arial", 16, "normal"))
            
            screen.update()
            time.sleep(0.05)
            
        except turtle.Terminator:
            print("Fenêtre fermée.")
            break

dessiner_grille()
animer_qubit()
screen.mainloop()
