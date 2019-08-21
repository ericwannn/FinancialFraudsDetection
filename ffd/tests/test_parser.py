import unittest

from ffd.features import FeatureGenerator


class MyTestCase(unittest.TestCase):

  feature_path = 'D:/Work/课题/财务异常识别/201907项目细化/ffd/data/features.xlsx'
  mapping_path = 'D:/Work/课题/财务异常识别/201907项目细化/ffd/data/kmmc.csv'

  def test_get_features(self):
    fg = FeatureGenerator(feature_path=self.feature_path, mapping_path=self.mapping_path)
    fg.get_features()

if __name__ == '__main__':
  unittest.main()
