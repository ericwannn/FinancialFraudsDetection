import re


def get_chinese_char(intput_string):
  return re.compile('[\u4e00-\u9fa5]+').findall(intput_string)


def safe_get(key_name, dict_name):
  res = dict_name.get(key_name, None)
  if not res:
    print('WARNING! {} not found in {}'.format(key_name, dict_name))
  return res