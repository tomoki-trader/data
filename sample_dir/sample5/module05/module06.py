#print(" in module06.py")
def hello(caller=""):
    print( "Hello, world! in module06 called by {}".format(caller) )
    
if __name__ == "__main__":
    hello()