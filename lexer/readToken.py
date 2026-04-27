class readToken:
    def __init__(self, iterator):
        # use iter() to turn received input into readable stream
        self.iterator = iter(iterator)
        # defined function to read until end
        self.getEntireToken()
    
    def getEntireToken(self):
        try:
            # init next attribute of self => next elt in iter
            self.next = next(self.iterator)
        except StopIteration:
            # if there is no more elt left in iter set next to None
            self.next = None
    
    def moveNext(self):
        # res = self.next
        res = self.next
        # updates self.next to next elt in iter
        self.getEntireToken()
        # return next elt in iter
        return res