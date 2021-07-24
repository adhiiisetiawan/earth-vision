import os
import shutil
import posixpath
from .utils import _urlretrieve
from torch.utils.data import Dataset
class LandCoverNet(Dataset):
    """Land Cover Net Dataset.
    http://registry.mlhub.earth/10.34911/rdnt.d2ce8i/
    """

    mirror = "https://storage.googleapis.com/ossjr/landcovernet-small"
    source_file = "ref_landcovernet_v1_source.tar.gz"
    labels_file = "ref_landcovernet_v1_labels.tar.gz"

    def __init__(self, root: str):
        self.root = root

        if not self._check_exists():
            self.download()
            self.extract_file()

    def __itemget__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def download(self):
        url_source = posixpath.join(self.mirror, self.source_file)
        url_label = posixpath.join(self.mirror, self.labels_file)
        _urlretrieve(url_source, os.path.join(self.root, self.source_file))
        _urlretrieve(url_label, os.path.join(self.root, self.labels_file))
    
    def extract_file(self):
        """Extract file from compressed file"""
        shutil.unpack_archive(os.path.join(self.root, self.source_file), self.root)
        shutil.unpack_archive(os.path.join(self.root, self.labels_file), self.root)

    def _check_exists(self):
        if not os.path.exists(self.root):
            os.makedirs(self.root)

        return os.path.exists(self.root, "ref_landcovernet_v1_labels") & \
            os.path.exists(self.root, "ref_landcovernet_v1_source")
