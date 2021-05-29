import os
from torch.utils.data import Dataset


class RarePlanes(Dataset):
    """RarePlanes: Synthetic Data Takes Flight Dataset.

    Args:
        root (string): Root directory of dataset.
        download (bool, optional): If true, downloads the dataset from the internet and
            puts it in root directory. If dataset is already downloaded, it is not
            downloaded again.
        data_mode (int): 0 for train data, 1 for testing data.
    """

    resources = {
        'sample_train_PS-RGB_tiled': 'gs://ossjr/sample_train_PS-RGB_tiled.tar.gz',
        'sample_train_geojson_aircraft_tiled': 'gs://ossjr/sample_train_geojson_aircraft_tiled.tar.gz',
        'sample_test_PS-RGB_tiled': 'gs://ossjr/sample_test_PS-RGB_tiled.tar.gz',
        'sample_test_geojson_aircraft_tiled': 'gs://ossjr/sample_test_geojson_aircraft_tiled.tar.gz'
    }

    def __init__(self, root: str, download: bool = False, data_mode: int = 0):
        self.root = root
        self.data_mode = data_mode

        if download and self._check_exists():
            print('Dataset already exists.')

        # if download and not self._check_exists():
            # self.download()

            # self.load_dataset()

    def _check_exists(self) -> bool:
        train_data, train_label, test_data, test_label = self.resources.keys()
        if os.path.exists(train_data) and os.path.exists(train_label) and \
                os.path.exists(test_data) and os.path.exists(test_label):
            return True
        else:
            return False
