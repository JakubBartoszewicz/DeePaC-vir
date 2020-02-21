from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='deepacvir',
      version='0.1.0',
      description='Detecting novel human viruses from DNA reads with reverse-complement neural networks.',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
      ],
      keywords='deep learning DNA sequencing synthetic biology pathogenicity prediction',
      url='https://gitlab.com/rki_bioinformatics/DeePaC',
      author='Jakub Bartoszewicz',
      author_email='jakub.bartoszewicz@hpi.de',
      license='MIT',
      packages=['deepacvir'],
      python_requires='>=3',
      install_requires=[
          'deepacvir>=0.10.1',
          'tensorflow==1.15',
          'scikit-learn>=0.22.1',
          'numpy>=1.18.1',
      ],
      entry_points={
          'console_scripts': ['deepacvir-vir=deepacvir.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
