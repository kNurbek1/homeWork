class Rectangle:
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height
    def calculate_volume(self):
        return self.length * self.width * self.height