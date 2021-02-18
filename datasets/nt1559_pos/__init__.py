# -*- coding: utf-8 -*-
"""nt1559_pos dataset.

Generated 18/02/2021.
NT1559 - Kyma GaN buffer on AlN nucleation layer.
Ground truth discriminates positions only.

Author: SSD Group, Bohdan Starosta
University of Strathclyde Physics Department
"""

import datasets


class nt1559_pos(datasets.Dataset):

    def __init__(self):
        super().__init__()

        self.desc = ("NT1559 - Kyma GaN buffer on AlN nucleation layer. "
        "Ground truth discriminates positions only.")
        self.generated = '2021-02-18'

    def setup(self, limit=None):
        if limit is not None and limit < 1:
            raise datasets.DatasetException('Limit must be at least 1.')

        # raw experimental images
        self.x = self._list_images('exp', limit)
        # ground truth
        self.y = self._list_images('ground', limit)

        self.on_epoch_end()

    def load_data(self, batch_x, batch_y):
        return (
            self._load_images('exp', batch_x, 'uint8', 'gs'),
            self._load_images('ground', batch_y, 'uint8', 'gs')
        )
