from pashi.kernels import GaussianBlurCuda
import numpy
import cv2

"""
NOTE: WIP and for now these methods are forwarding to the opencv methods. 

"""

def gaussian2(size, sigma):
    """Returns a normalized circularly symmetric 2D gauss kernel array

    f(x,y) = A.e^{-(x^2/2*sigma^2 + y^2/2*sigma^2)} where

    A = 1/(2*pi*sigma^2)

    as define by Wolfram Mathworld
    http://mathworld.wolfram.com/GaussianFunction.html
    """
    A = 1 / (2.0 * numpy.pi * sigma ** 2)
    x, y = numpy.mgrid[-size // 2 + 1:size // 2 + 1, -size // 2 + 1:size // 2 + 1]
    g = A * numpy.exp(-((x ** 2 / (2.0 * sigma ** 2)) + (y ** 2 / (2.0 * sigma ** 2))))
    return g


def fspecial_gauss(size, sigma):
    """Function to mimic the 'fspecial' gaussian MATLAB function
    """
    x, y = numpy.mgrid[-size // 2 + 1:size // 2 + 1, -size // 2 + 1:size // 2 + 1]
    g = numpy.exp(-((x ** 2 + y ** 2) / (2.0 * sigma ** 2)))
    return g / g.sum()


def greyscale(img_bgr):
    '''
    CUDA enabled color (BGR) to greyscale method.
    :param img:
    :return: greyscale version of the image
    '''
    cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

def gaussian_bulanik(src, ksize, sigmaX, sigmaY):
    '''
    CUDA enabled gaussian blur operation.

    :param src:
    :param ksize:
    :param sigmaX: Gaussian kernel standard deviation in X direction.
    :param sigmaY: Gaussian kernel standard deviation in Y direction; if sigmaY is zero, it is set to be equal to sigmaX.
    :return: resulting blurred image
    '''
    cv2.GaussianBlur(src=src, ksize=ksize, sigmaX=sigmaX, sigmaY=sigmaY)



def evrisim_2D(src, desired_depth, kernel, delta):
    '''
    CUDA enabled 2D convolution, close to filter2D in opencv
    :param src:
    :param desired_depth:
    :param kernel:
    :param delta:
    :return:
    '''
    cv2.Filter2D(src=src, ddepth=desired_depth, kernel=kernel, delta=delta)
