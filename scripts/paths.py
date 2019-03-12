import numpy as np
from queue import PriorityQueue
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.animation


def dijkstra(graph, src, dest):
    """Find shortest path from src to dest

    graph:
        dict[list[(int, int)]]: {node: [adj_node1, adj_node2,...]}
        src (int):
        dest (int):
    """
    to_process = PriorityQueue()
    # Start with the source and zero cost
    to_process.put((0, src))

    # Now as you process nodes one at a time from the queue
    # At the end of processing, you will mark their final weight
    final_costs = {}
    while to_process.qsize() > 0:
        cur_cost, cur_node = to_process.get()
        if cur_node in final_costs:
            continue
        # Send runners! all adjacent nodes get queued with the next cost
        # Note: this may be worse than a cost they have while already queued,
        # or it may be lower (in which case they'll jump the line
        for weight_cur_next, next_node in graph[cur_node]:
            to_process.put((cur_cost + weight_cur_next, next_node))

        final_costs[cur_node] = cur_cost

    return final_costs


def build1(n):
    graph = defaultdict(list)
    for i in range(1, n + 1):
        graph[i]
        if i + 1 <= n:
            graph[i].append((1, i + 1))
        if 3 * i <= n:
            graph[i].append((1, i * 3))
    return graph


def build_grid(n):
    def neighbors8(point):
        x, y = point
        return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x - 1, y - 1),
                (x + 1, y - 1), (x - 1, y + 1))

    node_grid = np.arange(n**2).reshape((n, n))
    node_grid = np.pad(node_grid, (1, 1), mode='constant', constant_values=-1)
    print(node_grid)
    graph = defaultdict(list)
    idx_lookup = {}
    for idx in range(1, n + 1):
        for jdx in range(1, n + 1):
            cur = node_grid[idx, jdx]
            neighbors = [node_grid[n] for n in neighbors8((idx, jdx))]
            graph[cur] = [(1, n) for n in neighbors if n >= 0]

            idx_lookup[cur] = (idx, jdx)

    return graph, node_grid, idx_lookup


def plot_grid_costs(costs, node_grid, idx_lookup):
    cost_grid = np.full_like(node_grid, -1)
    for node, cost in costs.items():
        print(node)
        i, j = idx_lookup[node]
        cost_grid[i, j] = cost

    plt.imshow(cost_grid)
    plt.show(block=True)


def animate_costs(costs, node_grid, idx_lookup, interval=200, outname='dijkstra.gif'):
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches((4, 4))
    fig.tight_layout()

    cost_grid = np.full_like(node_grid, -1)
    max_cost = max(costs.values())
    axim = ax.imshow(cost_grid, vmax=max_cost, cmap='jet')
    fig.colorbar(axim)
    ax.set_title("Path explored by Dijkstra's algorithm")
    cost_items = list(costs.items())  # Should preserve order of adding (python3.5)

    def update_im(idx):
        node, cost = cost_items[idx]
        i, j = idx_lookup[node]
        cost_grid[i, j] = cost
        ax.imshow(cost_grid, vmax=max_cost, cmap='jet')
        return ax

    stack_ani = matplotlib.animation.FuncAnimation(
        fig, update_im, frames=len(costs), interval=interval, blit=False, repeat=True)

    if outname:
        print("Saving to %s" % outname)
        stack_ani.save(outname, writer='imagemagick')
    else:
        plt.show()


if __name__ == '__main__':
    n = 10
    graph = build1(n)
    graph, node_grid, idx_lookup = build_grid(n)
    # print(sorted(graph.items()))

    src = 0
    dest = n**2 - 1
    costs = dijkstra(graph, src, dest)
    print("Cost from %s to %s" % (src, dest))
    # print(costs[dest])
    print(sorted(costs.items()))

    # plot_grid_costs(costs, node_grid, idx_lookup)
    animate_costs(costs, node_grid, idx_lookup, interval=100, outname='dijkstra.gif')
