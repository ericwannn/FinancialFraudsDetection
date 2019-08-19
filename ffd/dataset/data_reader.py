import pandas as pd


class DataReader(object):

  @staticmethod
  def read(file_path, file_type='csv'):
    if file_type == 'csv':
      method = pd.read_csv
    elif file_type == 'excel':
      method = pd.read_excel
    else:
      raise NotImplementedError
    return method(file_path)
