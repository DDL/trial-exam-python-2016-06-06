# Create a class that represents a cuboid:
# It should take it's three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid():
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def getSurface(self):
        surface = (2 * self.width * self.length) + (2 * self.length * self.height) + (2 * self.width * self.height)
        return surface

    def getVolume(self):
        volume = self.length * self.width *  self.height
        return volume


cube = Cuboid(2, 3, 4)
print(cube.getSurface())
print(cube.getVolume())

# Surface = 2 × Width × Length + 2 × Length × Height + 2 × Width × Height
# Volume = Length × Width ×  Height
