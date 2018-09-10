#!usr/bin/env python
import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np
import sys

if len(sys.argv) < 2 or sys.argv[1] not in ('python', 'matlab'):
    print("Usage: python %s ( python | matlab ) [savename.gif] " % sys.argv[0])
    sys.exit(1)

order_type = sys.argv[1]

fig, axes = plt.subplots(1, 2)
fig.set_size_inches((6, 3))
fig.tight_layout()

axes[0].grid()
axes[1].grid()

if order_type == 'python':
    shape = (2, 3, 4)  # Python
else:
    shape = (3, 4, 2)  # MATLAB

im = np.zeros(shape)

axes_image0 = axes[0].imshow(im[0], aspect='equal')
axes_image1 = axes[1].imshow(im[1], aspect='equal')


def update_im(idx):
    im = np.zeros(shape)
    order_arg = 'C' if order_type == 'python' else 'F'
    (r1, r2, r3) = np.unravel_index(idx, shape, order=order_arg)
    im[r1, r2, r3] = 1

    if order_type == 'python':
        axes[0].imshow(im[0, :, :])
        axes[1].imshow(im[1, :, :])
        ysize = im.shape[1]
    else:
        axes[0].imshow(im[:, :, 0])
        axes[1].imshow(im[:, :, 1])
        ysize = im.shape[0]

    axes[0].yaxis.set_ticks(np.arange(0, ysize))
    axes[1].yaxis.set_ticks(np.arange(0, ysize))
    fig.suptitle("Pixel num %s = image[%s, %s, %s]" % (idx, r1, r2, r3), y=0.9)
    return axes_image0, axes_image1


stack_ani = matplotlib.animation.FuncAnimation(
    fig, update_im, frames=im.size, interval=500, blit=False, repeat=True)

# To save, add 'imagename.gif' as an argument
if len(sys.argv) > 2:
    outname = sys.argv[2]
    print("Saving to %s" % outname)
    stack_ani.save(outname, writer='imagemagick')
else:
    plt.show()
