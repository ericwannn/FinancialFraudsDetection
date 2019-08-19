import pandas as pd

from ffd.dataset import DataReader
from ffd.dataset import Mapping

class FeatureGenerator(DataReader):

  def __init__(self, feature_path, mapping_path):
    self.data = self.read(file_path=feature_path, file_type='excel')
    self.mapping = Mapping(file_path=mapping_path)

  def get_feature(self):
    for index, row in self.data.iterrows():
      pass


