from pycuda.compiler import SourceModule

GaussianBlurCuda = SourceModule("""
__global__ void gaussian_blur_kernel(float *dest, float *a, float *b)
{
  const int i = threadIdx.x;
  dest[i] = a[i] * b[i];
}
""").get_function('gaussian_blur_kernel')



