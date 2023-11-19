# Flappy-lite
1. *Bird Class:*
   - Represents the bird character in the game.
   - Has attributes like position, climb duration, and images for wing movement.
   - Updates bird's position based on climb or sink speed.
   - Uses images and masks for wing animation.
   - Provides properties for the image, mask, and rectangle of the bird.

2. *PipePair Class:*
   - Represents a pair of pipes (top and bottom) that the bird must navigate through.
   - Pipes move from right to left across the screen.
   - The height and gap between pipes are determined randomly.
   - Provides properties for the height of the top and bottom pipes, visibility, and rectangle.
   - Uses masks for collision detection with the bird.
   - Updates pipe position.

3. *Functions:*
   - `load_images`: Loads game images like background, pipes, and bird wings.
   - `frames_to_msec` and `msec_to_frames`: Convert frames to milliseconds and vice versa.

4. *Main Function:*
   - Initializes the game, sets up the display, and loads images.
   - Creates a bird and an empty queue for pipes.
   - Manages game events (e.g., quitting, pausing) and bird actions (climbing).
   - Checks for collisions with pipes and updates the game state.
   - Displays the background, pipes, bird, and score.
   - Handles scoring when the bird passes through pipes.
   - Ends the game if there is a collision or if the player quits.

5. *Execution:*
   - The game runs in a loop until the player quits or the bird collides with a pipe or screen boundaries.
   - The score is displayed at the end.
