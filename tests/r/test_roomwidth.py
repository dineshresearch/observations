from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.roomwidth import roomwidth


def test_roomwidth():
  """Test module roomwidth.py by downloading
   roomwidth.csv and testing shape of
   extracted data has 113 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = roomwidth(test_path)
  try:
    assert x_train.shape == (113, 2)
  except:
    shutil.rmtree(test_path)
    raise()
