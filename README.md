<!-- {#mainpage} -->

# DeePaC-vir

DeePaC-vir is a plugin for DeePaC (see below) shipping built-in models for novel human virus detection directly from NGS reads.
For details, see our preprint on bioRxiv: <https://www.biorxiv.org/content/10.1101/2020.01.29.925354v5>

# DeePaC

DeePaC is a python package and a CLI tool for predicting labels (e.g. pathogenic potentials) from short DNA sequences (e.g. Illumina 
reads) with interpretable reverse-complement neural networks. For details, see our preprint on bioRxiv: 
<https://www.biorxiv.org/content/10.1101/535286v3> and the paper in *Bioinformatics*: <https://doi.org/10.1093/bioinformatics/btz541>.
For details regarding the interpretability functionalities of DeePaC, see the preprint here: <https://www.biorxiv.org/content/10.1101/2020.01.29.925354v2>

Documentation can be found here:
<https://rki_bioinformatics.gitlab.io/DeePaC/>. 
See also the main repo here: <https://gitlab.com/rki_bioinformatics/DeePaC>.


## Installation

### With Bioconda (recommended)
 [![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/deepac/README.html)
 
You can install DeePaC with `bioconda`. Set up the [bioconda channel](
<https://bioconda.github.io/user/install.html#set-up-channels>) first (channel ordering is important):

```
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```

We recommend setting up an isolated `conda` environment:
```
# python 3.6, 3.7 and 3.8 are supported
conda create -n my_env python=3.8
conda activate my_env
```

and then:
```
# For GPU support (recommended)
conda install tensorflow-gpu deepacvir
# Basic installation (CPU-only)
conda install deepacvir
```


### With pip

We recommend setting up an isolated `conda` environment (see above). Alternatively, you can use a `virtualenv` virtual environment (note that deepac requires python 3):
```
# use -p to use the desired python interpreter (python 3.6 or higher required)
virtualenv -p /usr/bin/python3 my_env
source my_env/bin/activate
```

You can then install DeePaC with `pip`. For GPU support, you need to install CUDA and CuDNN manually first (see TensorFlow installation guide for details). 
Then you can do the same as above:
```
# For GPU support (recommended)
pip install tensorflow-gpu
pip install deepacvir
```

Alternatively, if you don't need GPU support: 
```
# Basic installation (CPU-only)
pip install deepacvir
```


## Usage
DeePaC-vir may be used exactly as the base version of DeePaC. To use the plugin, substitute the `deepac` command for `deepac-vir`.
Visit <https://gitlab.com/rki_bioinformatics/DeePaC> for a DeePaC readme describing basic usage.

For example, you can use the following commands:
```
# See help
deepac-vir --help

# Run quick tests (eg. on CPUs)
deepac-vir test -q
# Full tests
deepac-vir test -a

# Predict using a rapid CNN (trained on VHDB data)
deepac-vir predict -r input.fasta
# Predict using a sensitive LSTM (trained on VHDB data)
deepac-vir predict -s input.fasta
```

More examples are available at <https://gitlab.com/rki_bioinformatics/DeePaC>.

## Supplementary data and scripts
Training, validation and test datasets are available here: <https://doi.org/10.5281/zenodo.3630803>.
In the main DeePaC repository (<https://gitlab.com/rki_bioinformatics/DeePaC>) you can find the R scripts and data files used in the papers for dataset preprocessing and benchmarking.

## Cite us
If you find DeePaC useful, please cite:

```
@article{10.1093/bioinformatics/btz541,
    author = {Bartoszewicz, Jakub M and Seidel, Anja and Rentzsch, Robert and Renard, Bernhard Y},
    title = "{DeePaC: predicting pathogenic potential of novel DNA with reverse-complement neural networks}",
    journal = {Bioinformatics},
    year = {2019},
    month = {07},
    issn = {1367-4803},
    doi = {10.1093/bioinformatics/btz541},
    url = {https://doi.org/10.1093/bioinformatics/btz541},
    eprint = {http://oup.prod.sis.lan/bioinformatics/advance-article-pdf/doi/10.1093/bioinformatics/btz541/28971344/btz541.pdf},
}

@article {Bartoszewicz2020.01.29.925354,
    author = {Bartoszewicz, Jakub M. and Seidel, Anja and Renard, Bernhard Y.},
    title = {Interpretable detection of novel human viruses from genome sequencing data},
    elocation-id = {2020.01.29.925354},
    year = {2020},
    doi = {10.1101/2020.01.29.925354},
    publisher = {Cold Spring Harbor Laboratory},
    URL = {https://www.biorxiv.org/content/early/2020/02/01/2020.01.29.925354},
    eprint = {https://www.biorxiv.org/content/early/2020/02/01/2020.01.29.925354.full.pdf},
    journal = {bioRxiv}
}

```