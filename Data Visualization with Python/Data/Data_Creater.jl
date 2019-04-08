# the Domain of definition
D = range(0,stop=1,step=0.1)

F = open("data01.dat","w")
for x in D
    y1 = (1/2)*(-cos(3*x+0.0)+1)
    println(x,"\t",y1)
    write(F,join([x,"\t",y1,"\n"]))
end
close(F)

F = open("data02.dat","w")
for x in D
    y2 = (1/2)*(-cos(3*x+0.1)+1)
    println(x,"\t",y2)
    write(F,join([x,"\t",y2,"\n"]))
end
close(F)

F = open("data03.dat","w")
for x in D
    y3 = (1/2)*(-cos(3*x+0.2)+1)
    println(x,"\t",y3)
    write(F,join([x,"\t",y3,"\n"]))
end
close(F)

F = open("data04.dat","w")
for x in D
    y4 = (1/2)*(-cos(3*x+0.3)+1)
    println(x,"\t",y4)
    write(F,join([x,"\t",y4,"\n"]))
end
close(F)

F = open("data05.dat","w")
for x in D
    y5 = (1/2)*(-cos(3*x+0.4)+1)
    println(x,"\t",y5)
    write(F,join([x,"\t",y5,"\n"]))
end
close(F)

F = open("data06.dat","w")
for x in D
    y6 = (1/2)*(-cos(3*x+0.5)+1)
    println(x,"\t",y6)
    write(F,join([x,"\t",y6,"\n"]))
end
close(F)

F = open("data07.dat","w")
for x in D
    y7 = (1/2)*(-cos(3*x+0.6)+1)
    println(x,"\t",y7)
    write(F,join([x,"\t",y7,"\n"]))
end
close(F)

F = open("data08.dat","w")
for x in D
    y8 = (1/2)*(-cos(3*x+0.7)+1)
    println(x,"\t",y8)
    write(F,join([x,"\t",y8,"\n"]))
end
close(F)

F = open("data09.dat","w")
for x in D
    y9 = (1/2)*(-cos(3*x+0.8)+1)
    println(x,"\t",y9)
    write(F,join([x,"\t",y9,"\n"]))
end
close(F)

F = open("data10.dat","w")
for x in D
    y10 = (1/2)*(-cos(3*x+0.9)+1)
    println(x,"\t",y10)
    write(F,join([x,"\t",y10,"\n"]))
end
close(F)

F = open("data10.dat","w")
for x in D
    y1 = (1/2)*(-cos(3*x+0.0)+1)
    y2 = (1/2)*(-cos(3*x+0.1)+1)
    y3 = (1/2)*(-cos(3*x+0.2)+1)
    y4 = (1/2)*(-cos(3*x+0.3)+1)
    y5 = (1/2)*(-cos(3*x+0.4)+1)
    y6 = (1/2)*(-cos(3*x+0.5)+1)
    y7 = (1/2)*(-cos(3*x+0.6)+1)
    y8 = (1/2)*(-cos(3*x+0.7)+1)
    y9 = (1/2)*(-cos(3*x+0.8)+1)
    y10 = (1/2)*(-cos(3*x+0.9)+1)
    println(x,"\t",y1,"\t",y2,"\t",y3,"\t",y4,"\t",y5,"\t",y6,"\t",y7,"\t",y8,"\t",y9,"\t",y10)
    write(F,join([x,"\t",y1,"\t",y2,"\t",y3,"\t",y4,"\t",y5,"\t",y6,"\t",y7,"\t",y8,"\t",y9,"\t",y10,"\n"]))
end
