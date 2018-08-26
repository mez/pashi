from setuptools import setup

setup(name='pashi',
      version='0.1',
      description='A set of CUDA enabled image processing helper methods.',
      url='http://github.com/mez/pashi',
      author='Mez Gebre',
      author_email='mez@jetcode.io',
      license='MIT',
      packages=['pashi'],
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=[
            'pycuda',
            'opencv-python',
            'numpy'
      ],
      zip_safe=False)