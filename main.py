from numba import cuda
import numpy as np
from PIL import Image
import math


@cuda.jit
def rotuj(image1, vystup):
    pass


def main():
    image = np.array("mini.png")
    print(image.shape)
    threadsperblock = (256, 256, 4)
    blockX = math.ceil(image.shape[0] / threadsperblock[0])
    blockY = math.ceil(image.shape[1] / threadsperblock[1])
    blockZ = math.ceil(image.shape[2] / threadsperblock[2])
    blockspergrid = (blockX, blockY, blockZ)

    input1 = cuda.to_device(image)
    output = cuda.device_array(image.shape)

    rotuj[blockspergrid, threadsperblock](input1, output)

    out = output.to_host()
    out = Image.fromarray(out)
    out.show()

main()