import sys
import time
import matplotlib.pyplot as plt

class Block:
    def __init__(self, mass, velocity, position):
        self.mass = mass
        self.velocity = velocity
        self.position = position

    def collide_with_wall(self):
        self.velocity *= -1.0

def will_collide(block1, block2):
    return (block1.position >= block2.position) and (block1.velocity > block2.velocity)

def simulate(block1, block2, delta_T):
    count_wall = 0
    count_blocks = 0

    time = 0.0
    times = []
    positions1 = []
    positions2 = []
    collisions_impossible = False
    fadeout = 1.0 / delta_T
    while (fadeout > 0):
        collisions_impossible = abs(block1.velocity) <= block2.velocity and block2.velocity >= 0.0
        if(collisions_impossible):
            fadeout -= 1

        if block2.position <= 0.0 and block2.velocity < 0.0:
            block2.position = 0.0  # correct position
            block2.collide_with_wall()
            count_wall += 1
        if block1.position <= 0.0 and block1.velocity < 0.0:
            block1.position = 0.0  # correct position
            block1.collide_with_wall()
            count_wall += 1

        if will_collide(block1, block2):
            v1, v2 = block1.velocity, block2.velocity
            block1.velocity = ((block1.mass - block2.mass) * v1 + 2.0 * block2.mass * v2) / (block1.mass + block2.mass)
            block2.velocity = ((block2.mass - block1.mass) * v2 + 2.0 * block1.mass * v1) / (block1.mass + block2.mass)
            count_blocks += 1

        block1.position += block1.velocity * delta_T
        block2.position += block2.velocity * delta_T

        time += delta_T
        times.append(time)
        positions1.append(block1.position)
        positions2.append(block2.position)

        sys.stdout.write("\rBlock 1: pos = %.2f, vel = %.2f | Block 2: pos = %.2f, vel = %.2f | BB collisions: %d, BW collisions: %d" %
                         (block1.position, block1.velocity, block2.position, block2.velocity, count_blocks, count_wall))
        sys.stdout.flush()

    print(f"\nFinal block-block collisions: {count_blocks}")
    print(f"Final block-wall collisions: {count_wall}")

    plt.figure(figsize=(12, 6))
    plt.plot(times, positions1, label='Block 1')
    plt.plot(times, positions2, label='Block 2')
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.title('Block Positions Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    block1 = Block(mass=1.0, velocity=0.0, position=1.0)  # second block
    block2 = Block(mass=10000.0, velocity=-2.0, position=2.0)  # first block (larger mass, initial speed)

    simulate(block1, block2, delta_T=0.0001)
