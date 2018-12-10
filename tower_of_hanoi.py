step = 1


def hanoi(n, starting_point, intermediate_point, destination):
    if n > 0:
        hanoi(n - 1, starting_point, destination, intermediate_point)
        move(n, starting_point, destination)
        hanoi(n - 1, intermediate_point, starting_point, destination)


def move(n, starting_point, destination):
    global step
    print("Step {0}: Move {1} from {2} to {3}".format(step, n, starting_point, destination))
    step += 1


hanoi(10, 'A', 'B', 'C')
