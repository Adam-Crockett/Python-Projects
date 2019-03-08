import random


def random_walk(n):
    """Return coordinates after walk 'n' random blocks"""
    walk_x, walk_y = 0, 0

    for step in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        walk_x += dx
        walk_y += dy

    return walk_x, walk_y


number_of_walks = 10000


for walk_length in range(1, 31):
    no_transport = 0
    for i in range(number_of_walks):
        (x, y) = random_walk(walk_length)
        distance = abs(x) + abs(y)  # Add the distance of the x and y directions
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length, " / % of no transport = ",
          100 * no_transport_percentage)
