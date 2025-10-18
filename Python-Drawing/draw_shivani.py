# Draw a Shivani
import turtle as t
t.bgcolor('black')
t.setup(1500, 1000)
t.title("Shivani")
t.tracer(2)
t.pensize(2)
c = ["purple", "cyan"]
for i in range(1200):
    t.color(c[i % 2])
    t.up()
    t.fd(i)
    t.down()
    t.rt(121)
    for k in range(5):
        t.fd(k * 5)
        t.lt(350)
        for j in range(10):
            t.fd(j * 6)
            t.up()
            t.down()
            t.rt(8)

t.done()
