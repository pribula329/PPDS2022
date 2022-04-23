from numba import cuda
import numpy as np
from PIL import Image
import math


@cuda.jit
def rotuj(image1, vystup):
    x, y, z = cuda.grid(3)
    if x < image1.shape[0] and y < image1.shape[1] and z < image1.shape[2]:
        vystup[x][y][z] += (image1[127 - x][y][z])
        print(x)


def main():
    image = np.array(Image.open("mini.png"))
    print(image.shape)
    threadsperblock = (128, 128, 4)
    blockX = math.ceil(image.shape[0] / threadsperblock[0])
    blockY = math.ceil(image.shape[1] / threadsperblock[1])
    blockZ = math.ceil(image.shape[2] / threadsperblock[2])
    blockspergrid = (blockX, blockY, blockZ)

    input1 = cuda.to_device(image)
    output = cuda.device_array(image.shape)

    rotuj[blockspergrid, threadsperblock](input1, output)

    out = output.copy_to_host().astype('uint8')
    out = Image.fromarray(out)
    out.show()

main()