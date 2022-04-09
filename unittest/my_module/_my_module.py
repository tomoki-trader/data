import six

class Sample:
    def __init__(self):
        self.message = "__file__:" + __file__ + ",__name__" + __name__
        self.saved_massage = self.message
    
    def get(self):#testing
        return self.message

if __name__ == "__main__":
    sample = Sample()
    six.print_(sample.get()) 