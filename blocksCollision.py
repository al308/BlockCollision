import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
import numpy as np

class Block:
    def __init__(self, mass, velocity, position, radius):
        self.mass = mass
        self.velocity = velocity
        self.position = position
        self.radius = radius

    def collide_with_wall(self):
        self.velocity *= -1.0

def will_collide(block1, block2):
    return (block1.position + block1.radius >= block2.position - block2.radius) and (block1.velocity > block2.velocity)

def simulate(block1, block2, delta_T):
    count_wall = 0
    count_blocks = 0
    positions1 = []
    positions2 = []

    collisions_impossible = False
    fadeout = 1.0 / delta_T
    while (fadeout > 0):
        collisions_impossible = abs(block1.velocity) <= block2.velocity and block2.velocity >= 0.0
        if(collisions_impossible):
            fadeout -= 1

        if block2.position - block2.radius <= 0.0 and block2.velocity < 0.0:
            block2.position = block2.radius  # correct position
            block2.collide_with_wall()
            count_wall += 1
        if block1.position - block1.radius <= 0.0 and block1.velocity < 0.0:
            block1.position = block1.radius  # correct position
            block1.collide_with_wall()
            count_wall += 1

        if will_collide(block1, block2):
            v1, v2 = block1.velocity, block2.velocity
            m1, m2 = block1.mass, block2.mass
            block1.velocity = ((m1 - m2) * v1 + 2.0 * m2 * v2) / (m1 + m2)
            block2.velocity = ((m2 - m1) * v2 + 2.0 * m1 * v1) / (m1 + m2)
            count_blocks += 1

        block1.position += block1.velocity * delta_T
        block2.position += block2.velocity * delta_T

        positions1.append(block1.position)
        positions2.append(block2.position)

    return positions1, positions2, count_blocks, count_wall

def update(num, block1, block2, blit=True):
    block1.center = (positions1[num], 0.5)
    block2.center = (positions2[num], 0.5)
    return block1, block2,

if __name__ == "__main__":
    block1 = Block(mass=1.0, velocity=0.0, position=1.0, radius=0.05)
    block2 = Block(mass=10000.0, velocity=-2.0, position=2.0, radius=0.1)
    positions1, positions2, count_blocks, count_wall = simulate(block1, block2, delta_T=0.001)

    fig, ax = plt.subplots()
    ax.set_xlim(0, 3)
    ax.set_ylim(-1, 1)  # Update the y-axis limits to include the floor

    ax.axhline(0, color='black', linewidth=1)  # Add a line at y=0

    block1_circle = Circle((0, 0), block1.radius)
    block2_circle = Circle((0, 0), block2.radius)  # Radius is larger to indicate larger mass
    ax.add_patch(block1_circle)
    ax.add_patch(block2_circle)

    ani = animation.FuncAnimation(fig, update, frames=np.arange(len(positions1)), fargs=[block1_circle, block2_circle], blit=True)

    ani.save('blocks_collision.mp4', writer='ffmpeg')

    print(f"Final block-block collisions: {count_blocks}")
    print(f"Final block-wall collisions: {count_wall}")
