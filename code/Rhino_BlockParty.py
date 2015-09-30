


import rhinoscriptsyntax as rs
import random
import Rhino.Geometry 

#variables
endx =0
endy =0
endz =0

startX=0
startY=0
startZ=0

var1 = -1
var2 = -1
var3 = -1
positiveX = False
positiveZ = False
positiveY = False
randomDirection=0
tempX=0
tempY=0
tempZ=0
jumper=0
jumper2= rs.GetInteger("Enter Box size")
randomStart = 4
randomEnd = 20

repetition=rs.GetInteger("Enter the amount of Boxes you want to draw (it should be completely divisible by four)")


counterZ=0
breakoutZ=0
i = 0

#getting the point, the boxes will built around these points
startPoint=rs.GetPoint("Set a starpoint in the Top view, X-axis define the position, Y-axis defines the size, just try, you will see ;) ")
(tempX,tempY,tempZ)= startPoint
endx=tempX
endy=0
endz=0 
(tempX,tempY,tempZ)= startPoint
cluster2=rs.GetPoint("set the second point")
cluster3=rs.GetPoint("set the third point")
cluster4=rs.GetPoint("set the fourth point")



bottom1= Rhino.Geometry.Point3d(tempX,tempY,tempZ)
bottom2= Rhino.Geometry.Point3d(tempX,tempY+jumper2,tempZ)
bottom3= Rhino.Geometry.Point3d(tempX+jumper2,tempY+jumper2,tempZ)
bottom4= Rhino.Geometry.Point3d(tempX+jumper2,tempY,tempZ)
top1= Rhino.Geometry.Point3d(endx,endy,endz)
top2= Rhino.Geometry.Point3d(endx,endy+jumper2,endz)
top3= Rhino.Geometry.Point3d(endx+jumper2,endy+jumper2,endz)
top4= Rhino.Geometry.Point3d(endz+jumper2,endy,endz)
myList=[bottom1,bottom2,bottom3,bottom4,top1,top2,top3,top4]


#the main process is made in this while loop, it will execute 250 times
while i < repetition:
    global startPoint
    global endx
    global endy
    global endz
    global var1
    global var2
    global var3
    global positiveX
    global positiveZ
    global positiveY
    global randomDirection
    global randomEnd
    global tempX
    global tempY
    global tempZ
    global cluster2
    global cluster3
    global cluster4
    global myList
    global startX
    global startY
    global startZ
    global counterZ
    global breakoutZ
    global jumper
    global jumper2
    global repetition
    #define the direction of the next box, alway straight in one direction
    randomDirection = random.randint(1,3)
    
    if i == 0:
        (tempX,tempY,tempZ)=startPoint
        endy=0
        endz=0
        if tempY <= 0:
            tempY = tempY * -1
            if tempY <= randomStart:
                tempY= tempY +randomStart +1
        if tempY <= randomStart:
            tempY= tempY +randomStart +1
        randomEnd = tempY
        i =i+1
    #starting with the second Point as center of the boxes
    if i == repetition/4:
        (tempX,tempY,tempZ)=cluster2
        if tempY <= 0:
            tempY = tempY * -1
            if tempY <= randomStart:
                tempY= tempY +randomStart+1
            if tempY <= randomStart:
                tempY= tempY +randomStart+1
        randomEnd = tempY
        i = i+1
    #starting with the third Point as center of the boxes
    if i == repetition/2:
        (tempX,tempY,tempZ)=cluster3
        if tempY <= 0:
            tempY = tempY * -1
            if tempY <= randomStart:
                tempY= tempY +randomStart+1
        if tempY <= randomStart:
            tempY= tempY +randomStart+1
        randomEnd = tempY
        i = i+1
    #starting with the fourth Point as center of the boxes
    if i == repetition/2 + repetition/4 :
        (tempX,tempY,tempZ)=cluster4
        if tempY <= 0:
            tempY = tempY * -1
            if tempY <= randomStart:
                tempY= tempY +randomStart+1
        if tempY <= randomStart:
                tempY= tempY +randomStart+1
        randomEnd = tempY
        i = i+1

    
    #draw in X direction
    if randomDirection == 1 and positiveX is not True:
        
        startX= endx
        startY= endy
        startZ= endz
        
        endx = random.randrange(randomStart,randomEnd)
        #this changes the direction everytime (var1) from, minus to plus and otherwise; tempX is the center of the current boxes
        endx = endx * var1 + tempX
        
        if var1 == -1:
            jumper = -jumper2
        
        #define corners of the new Box (eight 3d Points)
        bottom1= Rhino.Geometry.Point3d(startX-jumper,startY,startZ)
        bottom2= Rhino.Geometry.Point3d(startX-jumper,startY+jumper2,startZ)
        bottom3= Rhino.Geometry.Point3d(startX-jumper,startY+jumper2,startZ+jumper2)
        bottom4= Rhino.Geometry.Point3d(startX-jumper,startY,startZ+jumper2)
        top1= Rhino.Geometry.Point3d(endx,endy,endz)
        top2= Rhino.Geometry.Point3d(endx,endy+jumper2,endz)
        top3= Rhino.Geometry.Point3d(endx,endy+jumper2,endz+jumper2)
        top4= Rhino.Geometry.Point3d(endx,endy,endz+jumper2)

        myList = [bottom1,bottom2,bottom3,bottom4,top1,top2,top3,top4]
        
        rs.AddBox(myList)
        
        
        var1 = var1 * -1
        jumper = 0
        #this let the boxes grow in plus X direction
        if tempX >= 0:
            tempX = tempX + tempX/150
        if tempX <= 0:
            tempX = tempX - tempX/150
        
        #with these booleans I prevent that the box will be drawed two times on the same axis/direction
        positiveX =True
        positiveY =False
        positiveZ =False
        i = i+ 1
        #draw in Y direction
    if randomDirection == 2 and positiveY is not True:
        
        startX= endx
        startY= endy
        startZ= endz
        endy =  random.randrange(randomStart,randomEnd)
        endy = endy * var2
        if var2 == -1:
            jumper = -jumper2
        
        #define corners of the new Box (eight 3d Points)
        bottom1= Rhino.Geometry.Point3d(startX,startY-jumper,startZ)
        bottom2= Rhino.Geometry.Point3d(startX+jumper2,startY-jumper,startZ)
        bottom3= Rhino.Geometry.Point3d(startX+jumper2,startY-jumper,startZ+jumper2)
        bottom4= Rhino.Geometry.Point3d(startX,startY-jumper,startZ+jumper2)
        top1= Rhino.Geometry.Point3d(endx,endy,endz)
        top2= Rhino.Geometry.Point3d(endx+jumper2,endy,endz)
        top3= Rhino.Geometry.Point3d(endx+jumper2,endy,endz+jumper2)
        top4= Rhino.Geometry.Point3d(endx,endy,endz+jumper2)
        
        
        
        myList = [bottom1,bottom2,bottom3,bottom4,top1,top2,top3,top4]
        
        rs.AddBox(myList)

        var2 = var2 * -1
        jumper=0
        i = i+ 1    
        #with these booleans I prevent that the box will be drawed two times on the same axis/direction
        positiveX =False
        positiveY =True
        positiveZ =False
        
        #draw in Z direction
    if randomDirection == 3  and positiveZ is not True:
        
        startX= endx
        startY= endy
        startZ= endz
        #breakoutZ will be execute every 15th iteration, its for esthetic
        if counterZ == 15:
            breakoutZ =random.randrange(20,40) * var3
            counterZ = 0
        endz =  random.randrange(randomStart,randomEnd)
         #this changes the direction everytime (var1) from, minus to plus and otherwise
        endz = breakoutZ + endz * var3  

        
        if var3 == -1:
            jumper = -jumper2

        #define corners of the new Box (eight 3d Points)
        bottom1= Rhino.Geometry.Point3d(startX,startY,startZ-jumper)
        bottom2= Rhino.Geometry.Point3d(startX+jumper2,startY,startZ-jumper)
        bottom3= Rhino.Geometry.Point3d(startX+jumper2,startY+jumper2,startZ-jumper)
        bottom4= Rhino.Geometry.Point3d(startX,startY+jumper2,startZ-jumper)
        top1= Rhino.Geometry.Point3d(endx,endy,endz)
        top2= Rhino.Geometry.Point3d(endx+jumper2,endy,endz)
        top3= Rhino.Geometry.Point3d(endx+jumper2,endy+jumper2,endz)
        top4= Rhino.Geometry.Point3d(endx,endy+jumper2,endz)
        
        myList = [bottom1,bottom2,bottom3,bottom4,top1,top2,top3,top4]
        
        rs.AddBox(myList)
        
        var3 = var3 * -1
        breakoutZ = 0
        counterZ = counterZ +1
        i = i+ 1
        
        #with these booleans I prevent that the box will be drawed two times on the same axis/direction
        positiveX =False
        positiveY =False
        positiveZ =True


