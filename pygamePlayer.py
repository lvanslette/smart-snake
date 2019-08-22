# class for the python snake itself
class Player:
    x = [0]     # keeps track of each snake's x-value
    y = [0]     # keeps track of each snake's y-value
    step = 67       # how far the snake head should jump in pixels in the frame
    direction = 0   # starts going east
    length = 3      # if not given a value, snake starts with length 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, 2000):    # add 2000 empty slots to the snake
            self.x.append(-100)
            self.y.append(-100)

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update the rest of the snake, other than the head, by using previous positions of the head
            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    # if an arrow key has been pressed, change the direction of the head of the snake
    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    # draws the image of the snake
    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))
