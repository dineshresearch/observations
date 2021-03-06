# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def happiness(path):
  """happiness

  Data loads lazily. Type data(happiness) into the console.

  A data.frame with 17137 rows and 33 variables:

  -  year. gss year for this respondent

  -  workstat. work force status

  -  prestige. occupational prestige score

  -  divorce. ever been divorced or separated

  -  widowed. ever been widowed

  -  educ. highest year of school completed

  -  reg16. region of residence, age 16

  -  babies. household members less than 6 yrs old

  -  preteen. household members 6 thru 12 yrs old

  -  teens. household members 13 thru 17 yrs old

  -  income. total family income

  -  region. region of interview

  -  attend. how often r attends religious services

  -  happy. general happiness

  -  owngun. =1 if own gun

  -  tvhours. hours per day watching tv

  -  vhappy. =1 if 'very happy'

  -  mothfath16. =1 if live with mother and father at 16

  -  black. =1 if black

  -  gwbush04. =1 if voted for G.W. Bush in 2004

  -  female. =1 if female

  -  blackfemale. black\*female

  -  gwbush00. =1 if voted for G.W. Bush in 2000

  -  occattend. =1 if attend is 3, 4, or 5

  -  regattend. =1 if attend is 6, 7, or 8

  -  y94. =1 if year == 1994

  -  y96.

  -  y98.

  -  y00.

  -  y02.

  -  y04.

  -  y06. =1 if year == 2006

  -  unem10. =1 if unemployed in last 10 years

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `happiness.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 17137 rows and 33 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'happiness.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/happiness.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='happiness.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
