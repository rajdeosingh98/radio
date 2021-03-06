# pylint: disable=too-few-public-methods
""" Contains ResNodule3DNet50 model class. """

import numpy as np
from ...batchflow.models.tf import ResNet50         # pylint: disable=no-name-in-module, import-error


class ResNodule3DNet50(ResNet50):
    """ Implementation of custom DenseNet architecture for lung cancer detection. """

    @classmethod
    def default_config(cls):
        """ Specification of custom block parameters. """
        config = ResNet50.default_config()

        input_config = dict(layout='cnap', filters=16, kernel_size=7,
                            pool_size=3, pool_strides=(1, 2, 2))
        config['input_block'].update(input_config)      # pylint: disable=no-member

        filters = 16   # number of filters in the first block
        config['body']['filters'] = (2 ** np.arange(len(config['body']['num_blocks'])) * filters      # pylint: disable=invalid-sequence-index
                                     * config['body']['block']['width_factor'])                       # pylint: disable=invalid-sequence-index

        return config
