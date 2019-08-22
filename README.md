# smart-snake
Play Snake against the Computer.

Now, we need a ML algorithm that will learn how to play snake.

We could do self.machine.draw(self._display_surf, self._machine_surf) next to the other draw functions to draw the machine snake.
We could also have 2 more for loops in the on_loop function that would see if the machine collided with the player snake or if the player collided with the machine.
We'd also need a function in the machine file that gets the apple.x and apple.y positions.
If the machine or the player collides with the apple, then the apple position changes but only one snake gets bigger.

(How do you make a bunch of snake games into a training set?)
Linear Regression:
    Training set:
        Features: action, barrier_left, barrier_front, barrier_right, angle
        Output: reaction