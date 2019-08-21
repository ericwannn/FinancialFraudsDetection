from __future__ import absolute_import

from collections import namedtuple

from ffd.dataset import DataReader
from ffd.utils import safe_get


class Mapping(DataReader):

  def __init__(self, file_path):
    self.data = self.read(file_path=file_path, file_type='csv')
    self.kmdm2kmmc, self.kmmc2kmdm = self.parse_into_dict()

  def parse_into_dict(self):
    kmdm2kmmc = dict()
    kmmc2kmdm = dict()
    _kmdm_info = namedtuple('kmdm_info', ['kmdm', 'info'])
    _kmmc_info = namedtuple('kmmc_info', ['kmmc', 'info'])
    for idx, row in self.data.iterrows():
      kmdm, kmmc, info = row 
      kmdm2kmmc[kmdm] = _kmmc_info(kmmc, info)
      kmmc2kmdm[kmmc] = _kmdm_info(kmdm, info)
    return kmdm2kmmc, kmmc2kmdm

  def to_kmdm(self, kmmc):
    return safe_get(kmmc, self.kmmc2kmdm).kmdm
  
  def to_kmmc(self, kmdm):
    return safe_get(kmdm, self.kmdm2kmmc).kmmc
    