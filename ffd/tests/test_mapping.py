import unittest
from ffd.dataset import Mapping


class TestMapping(unittest.TestCase):
  def test_parse_into_dict(self):
    mapping = Mapping('D:/Work/课题/财务异常识别/201907项目细化/ffd/data/kmmc.csv')
    self.assertEqual(mapping.to_kmmc('sy'), '商誉')
    self.assertEqual(mapping.to_kmdm('商誉'), 'sy')


if __name__ == "__main__":
    unittest.main()