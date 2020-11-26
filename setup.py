from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='deepacvir',
      version='0.2.2',
      description='Detecting novel human viruses from DNA reads with reverse-complement neural networks.',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
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
          'deepac>=0.11.0',
          'tensorflow>=2.1',
          'scikit-learn>=0.22.1',
          'numpy>=1.17',
          'matplotlib>=3.1.3',
      ],
      entry_points={
          'console_scripts': ['deepac-vir=deepacvir.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
