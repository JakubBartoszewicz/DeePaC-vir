"""@package deepacvir.command_line
A DeePaC CLI. Support subcommands, prediction with built-in and custom models, training, evaluation, data preprocessing.

"""
import sklearn # to load libgomp early to solve problems with static TLS on some systems like bioconda mulled-tests
import matplotlib.pyplot as plt # also to solve import ordering problems in bioconda mulled tests
import numpy as np
import tensorflow as tf
import random as rn
import os
from deepacvir import __file__
from deepacvir import __version__

from deepac.command_line import MainRunner


def main():
    """Run DeePaC-vir CLI."""
    seed = 0
    np.random.seed(seed)
    tf.random.set_seed(seed)
    rn.seed(seed)
    modulepath = os.path.dirname(__file__)
    print("DeePaC-vir {}. Using viral models.".format(__version__))
    builtin_configs = {"rapid": os.path.join(modulepath, "builtin", "config", "nn-vhdb-rapid-cnn.ini"),
                       "sensitive": os.path.join(modulepath, "builtin", "config", "nn-vhdb-sensitive-lstm.ini")}
    builtin_weights = {"rapid": os.path.join(modulepath, "builtin", "weights", "nn-vhdb-rapid-cnn.h5"),
                       "sensitive": os.path.join(modulepath, "builtin", "weights", "nn-vhdb-sensitive-lstm.h5")}
    runner = MainRunner(builtin_configs, builtin_weights)
    runner.parse()


if __name__ == "__main__":
    main()
