# this class will get a model based on the difficulty then compete against the player
class Machine:
    x = [0]
    y = [0]
    length = 5

    updateCount = 0
    updateCountMax = 2

    step = 67
    direction = 0

    def __init__(self, mode):

        self.mode = mode
        # train the NN, more training means a smarter game
        if mode == 'easy':
            nn = NeuralNetwork(3000)
        elif mode == 'medium':
            nn = NeuralNetwork(6000)
        elif mode == 'hard':
            nn = NeuralNetwork(10000)

        # add 2000 empty slots to the snake
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)

    # draws the machine snake
    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))

    # update the snake, same as in the player class
    def update(self, apple_x, apple_y):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update the rest of the snake, other than the head, by using previous positions of the head
            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

            self.get_direction(apple_x, apple_y)
            # update position of head of snake
            if self.direction == 0:     # right
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:     #left
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:     # up
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:     # down
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    # returns 0,1,2,3 as the direction the machine should go
    def get_direction(self, apple_x, apple_y):
        machine_apple_angle = self.get_angle(apple_x, apple_y)
        self.direction = 0

    # returns the angle between the head of the machine and the apple for the neural network
    def get_angle(self, apple_x, apple_y):
        return inverse_tan(apple_x - self.x[0], apple_y - self.y[0])