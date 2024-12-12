class RemoteControl:
    def __init__(self):
        self.channels = ["Disney Channel","National geography","MTV","Sony ESPN"]
        self.index = -1

    def __iter__(Self):
        return Self

    def __next__(self):
        self.index +=1
        if(self.index)==len(self.channels):
            raise StopIteration 

        return self.channels[self.index]   
        
r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr)) 
print(next(itr))
print(next(itr))       
 