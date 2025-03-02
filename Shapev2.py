import turtle  
  
sc = turtle.Screen() 
sc.bgcolor("black") 
sc.title("Turtle") 
t1 = turtle.Turtle() 
t1.color("blue")            
  
def draw(rad):
    for i in range(2):
        t1.circle(rad,90)
        t1.circle(rad//2,90)
colour = ["red","blue","green","violet","yellow","blue"]
val = 10
ind = 0
t1.speed(100)
for i in range(36):
    t1.seth(-val)
    t1.color(colour[ind])
    
    if ind == 5:
        ind = 0
    else:
        ind +=1
    draw(80)
    val +=10

sc.exitonclick()
