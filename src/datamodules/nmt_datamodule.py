from pytorch_lightning import LightningDataModule
from src.datasets.nmt_dataset import NMTDataset
from torch.utils.data import DataLoader

class NMTDataModule(LightningDataModule):
    """

    """

    def __init__(self, *args, **kwargs):
        super(NMTDataModule, self).__init__()

        self.batch_size = kwargs['batch_size']
        self.num_worker = kwargs['num_workers']
        self.pin_memory = kwargs['pin_memory']
        self.data_train = None
        self.data_val = None
        self.data_test = None

    def setup(self, stage=None):
        self.data_train = NMTDataset('data/processed_iwslt_data', 'train')
        self.data_val = NMTDataset('data/processed_iwslt_data', 'val')
        self.data_test = NMTDataset('data/processed_iwslt_data', 'test')


    def train_dataloader(self):
        return DataLoader(dataset=self.data_train,
                          batch_size=self.batch_size,
                          num_workers=self.num_worker,
                          pin_memory=self.pin_memory,
                          shuffle=True)

    def val_dataloader(self):
        return DataLoader(dataset=self.data_val,
                          batch_size=self.batch_size,
                          num_workers=self.num_worker,
                          pin_memory=self.pin_memory,
                          shuffle=True)

    def test_dataloader(self):
        return DataLoader(dataset=self.data_test,
                          batch_size=self.batch_size,
                          num_workers=self.num_worker,
                          pin_memory=self.pin_memory,
                          shuffle=True)





