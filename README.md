
# Blocks Collision Simulation

This Python project simulates the collision dynamics between two blocks and their interaction with a wall using matplotlib for animation. The simulation calculates the velocity and position of each block after each collision, considering their masses.

## Features

- Simulation of elastic collisions between two blocks.
- Blocks collision with a stationary wall.
- Calculation of velocities and positions post-collision.
- Animation of the simulation using matplotlib.
- Saving the animation as an MP4 file.

## Prerequisites

- Python
- matplotlib (`pip install matplotlib`)
- numpy (`pip install numpy`)

## Installation

1. Clone the repository:
   ```
   git clone [repository URL]
   ```

2. Navigate to the project directory:
   ```
   cd [project directory]
   ```

3. Install the required Python packages:
   ```
   pip install matplotlib numpy
   ```

## Usage

1. Run the script to start the simulation:
   ```
   python [script name]
   ```

2. The simulation will produce an MP4 file `blocks_collision.mp4` showing the animation of the collisions.

3. Console output will include the count of block-block and block-wall collisions.

## Customization

- Modify the `Block` class to change the mass, velocity, position, and radius of the blocks.
- Adjust the `simulate` function to change the time step (`delta_T`) and collision logic.
- Update the `update` function for custom animation requirements.

## Output

- Animation file: `blocks_collision.mp4`
- Console output: Number of collisions between blocks and with the wall.

## Note

- The simulation assumes perfectly elastic collisions.
- The animation is generated using matplotlib's FuncAnimation and saved using FFMpeg.
