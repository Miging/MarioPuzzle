from bangtal import *

scene=Scene("","images/problem.png")

ob1=Object("images/1.png")
ob2=Object("images/2.png")
ob3=Object("images/3.png")
ob4=Object("images/4.png")
ob5=Object("images/5.png")
ob6=Object("images/6.png")
ob7=Object("images/7.png")
ob8=Object("images/8.png")
ob9=Object("images/9.png")
ob10=Object("images/10.png")
ob11=Object("images/11.png")
ob12=Object("images/12.png")
ob13=Object("images/13.png")
ob14=Object("images/14.png")
ob15=Object("images/15.png")
ob16=Object("images/16.png")

ob1.locate(scene,360,500)
ob2.locate(scene,500,500)
ob3.locate(scene,640,500)
ob4.locate(scene,780,500)
ob5.locate(scene,360,360)
ob6.locate(scene,500,360)
ob7.locate(scene,640,360)
ob8.locate(scene,780,360)
ob9.locate(scene,360,220)
ob10.locate(scene,500,220)
ob11.locate(scene,640,220)
ob12.locate(scene,780,220)
ob13.locate(scene,360,80)
ob14.locate(scene,500,80)
ob15.locate(scene,640,80)
ob16.locate(scene,780,80)

ob1.show()
ob2.show()
ob3.show()
ob4.show()
ob5.show()
ob6.show()
ob7.show()
ob8.show()
ob9.show()
ob10.show()
ob11.show()
ob12.show()
ob13.show()
ob14.show()
ob15.show()

list1=[[ob1,ob2,ob3,ob4],[ob5,ob6,ob7,ob8],[ob9,ob10,ob11,ob12],[ob13,ob14,ob15,None]]

def isempty(ob):



startGame(scene)
