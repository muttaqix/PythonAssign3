import turtle  
  
sc = turtle.Screen() 
sc.bgcolor("black") 
sc.title("Turtle") 
t1 = turtle.Turtle() 
t1.color("blue") 
tut = turtle.Screen()            
  
for i in range(4): 
    t1.color("green")
    t1.forward(100) 
    t1.left(90) 
  
t1.goto(50,50) 
  
for i in range(4): 
    t1.color("red")
    t1.forward(100) 
    t1.left(90) 

t1.goto(150,50) 
t1.goto(100,0) 
t1.goto(100,100) 
t1.goto(150,150) 
t1.goto(50,150) 
t1.goto(0,100)

sc.exitonclick()
