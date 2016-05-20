'''http://fivethirtyeight.com/features/night-falls-a-storm-rolls-in-can-you-cross-the-river/'''
import argparse
import numpy as np


def print_rows(verts, crosses):
    '''Represent the bridges
    verts has one more row than crosses'''
    print verts[0]
    idx = 0
    while idx < len(crosses):
        print ' ' + str(crosses[idx])
        idx += 1
        print verts[idx]


def accessible(level):
    '''Used to check if a level has
    become completely inaccessable'''
    return any(level)


def next_side(verts, crosses):
    '''A platform is reachable through a direct route,
    or from another vertical bridge and cross bridge'''
    a, b, c = verts
    left, right = crosses
    platforms = np.array([
        a or (b * left) or (c * right * left),
        (a * left) or (b) or (c * right),
        c or (b * right) or (a * left * right)
    ])
    return platforms


def next_side_general(verts, crosses):
    '''For each possible platform, performs a two
    sided search to see if any combination of bridge
    and cross section and make the current platform accessible'''

    platforms = np.zeros_like(verts)
    cur_platform = 0

    while cur_platform < len(verts):
        # First, move left to find ways to reach platform
        left_idx = cur_platform
        while left_idx >= 0:
            # A path exists if the vertical bridge is intact
            # and all cross bridges from there to cur_platform are intact
            # Note: all([]) = True
            found_path = verts[left_idx] and all(crosses[left_idx:cur_platform])
            if found_path:
                platforms[cur_platform] = 1
                break
            left_idx -= 1

        # Check to the right
        right_idx = cur_platform + 1
        while right_idx < len(verts):
            found_path = verts[right_idx] and all(crosses[cur_platform:right_idx])
            if found_path:
                platforms[cur_platform] = 1
                break
            right_idx += 1

        cur_platform += 1

    return platforms


def next_row(platforms, bridges):
    '''Next level is reachable if the platform is reachable
    and corresponding bridge is intact'''
    return np.bitwise_and(platforms, bridges)


def process_bridges(verts, crosses):
    idx = 0
    level = verts[0]
    while idx < len(crosses):
        cross = crosses[idx]
        platforms_accessible = next_side_general(level, cross)

        next_bridges = verts[idx + 1]
        level = next_row(platforms_accessible, next_bridges)

        if not accessible(level):
            return False

        idx += 1

    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--size", type=int,
        help="Number of platforms to cross", default=3)
    parser.add_argument(
        "--iters", type=int,
        help="Number iterations to test on", default=100000)
    args = parser.parse_args()

    N, iterations = args.size, args.iters

    passed = 0
    for _ in range(iterations):
        vert_bridges = np.random.randint(0, 2, size=(N, N))
        cross_bridges = np.random.randint(0, 2, size=(N - 1, N - 1))
        # print_rows(vert_bridges, cross_bridges)

        result = process_bridges(vert_bridges, cross_bridges)

        if result:
            passed += 1

    print 'Cross attempts: %s' % iterations
    print 'Number of successful crosses: %s' % passed
    print 'Success rate: {0:.2%}'.format(float(passed) / iterations)
