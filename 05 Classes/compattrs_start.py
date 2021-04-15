# customize string representations of objects


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: use getattr to dynamically return a value
    

    # TODO: use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        super().__setattr__(attr, val)

    # TODO: use dir to list the available properties
        

def main():
    # create an instance of myColor
    cls1 = myColor()
    # print the value of a computed attribute
    
    # set the value of a computed attribute
    
    # access a regular attribute
    
    # list the available attributes
    

if __name__ == "__main__":
    main()
