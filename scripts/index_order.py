import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np
import sys

fig, axes = plt.subplots(1, 2)
fig.set_size_inches((6, 3))
fig.tight_layout()

axes[0].grid()
axes[1].grid()

shape = (2, 3, 4)  # Python
# shape = (3, 4, 2)  # MATLAB
im = np.zeros(shape)

axes_image0 = axes[0].imshow(im[0], aspect='equal')
axes_image1 = axes[1].imshow(im[1], aspect='equal')


def update_im(idx):
    im = np.zeros(shape)
    (r1, r2, r3) = np.unravel_index(idx, shape)  # Python
    # (r1, r2, r3) = np.unravel_index(idx, shape, order='F')  # MATLAB
    im[r1, r2, r3] = 1

    # Python:
    axes[0].imshow(im[0, :, :])
    axes[1].imshow(im[1, :, :])
    ysize = im.shape[1]

    # MATLAB:
    # axes[0].imshow(im[:, :, 0])
    # axes[1].imshow(im[:, :, 1])
    # ysize = im.shape[0]

    axes[0].yaxis.set_ticks(np.arange(0, ysize))
    axes[1].yaxis.set_ticks(np.arange(0, ysize))
    fig.suptitle("image[%s, %s, %s]" % (r1, r2, r3), y=0.9)
    return axes_image0, axes_image1


stack_ani = matplotlib.animation.FuncAnimation(
    fig, update_im, frames=im.size, interval=500, blit=False, repeat=True)

# To save, add 'imagename.gif' as an argument
if len(sys.argv) > 1:
    outname = sys.argv[1]
    print("Saving to %s" % outname)
    stack_ani.save(outname, writer='imagemagick')
else:
    plt.show()
