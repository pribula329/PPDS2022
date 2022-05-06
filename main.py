"""
Author: Lukáš Pribula
Cuda program for mirroring image
"""
import time
from numba import cuda
import numpy as np
from PIL import Image
import math


@cuda.jit
def rotuj(image1, vystup):
    """
    Function for cuda computing
    :param image1: input image
    :param vystup: output image
    :return: none
    """
    x, y, z = cuda.grid(3)

    if x < image1.shape[0] and y < image1.shape[1] and z < image1.shape[2]:
        vystup[x][y][z] = (image1[x][y][z])



def main():
    """
    Function for cuda example
    :return: none
    """
    image = np.array(Image.open("mini.png"))
    print(image.shape)

    data_out = []
    data_gpu = []
    gpu_out = []
    streams = []
    start_events = []
    end_events = []
    imageSplit = np.array_split(image, 128)

    for x in range(len(imageSplit)):

        streams.append(cuda.stream())
        start_events.append(cuda.event())
        end_events.append(cuda.event())

    for i in range(len(imageSplit)):
        data_gpu.append(cuda.to_device(imageSplit[i], stream=streams[i]))
        data_out.append(cuda.to_device(imageSplit[i], stream=streams[i]))


    t_start = time.perf_counter()
    for i in range(len(imageSplit)):
        print(i)
        start_events[i].record(streams[i])
        rotuj[1, 64, streams[i]](data_gpu[i], data_out[127-i])

    t_end = time.perf_counter()

    for i in range(len(imageSplit)):
        end_events[i].record(streams[i])
        gpu_out.append(data_out[i].copy_to_host(stream=streams[i]))
    out =gpu_out[0]
    for i in range(1,len(gpu_out)):
        out = np.concatenate((out, gpu_out[i]))





    out = out.reshape(128,128,3)
    out = out.astype('uint8')
    out = Image.fromarray(out)
    out.show()
    print(f'Total time: {t_end - t_start}')



main()