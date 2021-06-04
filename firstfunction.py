def orice(x,y,z):
    print("Hello From My Function!  " + x)
    print("tot ce se poate  " + y)
    print("mai mult sau putin  " + z)

def orice2():
    x = "posibil"
    y = "temporar"
    z = "permanent"
    print("orice 2 function  " +x+ " " +y+" "  +z)

def testArgs(*args):
    for x in args:
        print(x)



orice("xy", "xx", "xz")
orice("x1", "y1", "z1")
orice("x2", "y2", "x2")

orice2()


testArgs(1,2,3,4,5,6,7,8,9,0,33,"opk" , "nuh")