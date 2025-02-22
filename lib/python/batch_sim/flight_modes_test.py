# Copyright 2020 Makani Technologies LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test of the flight_mode work-around."""

import unittest

from makani.control import control_types
from makani.lib.python import c_helpers
from makani.lib.python.batch_sim import flight_modes


class FlightModeTest(unittest.TestCase):

  def setUp(self):
    self._flight_mode_helper = c_helpers.EnumHelper('FlightMode', control_types)

  def testFlightModes(self):
    test = flight_modes.GetFlightModes()
    self.assertEqual(len(self._flight_mode_helper), len(test))
    for key, value in self._flight_mode_helper:
      self.assertIn(key, test)
      self.assertEqual(test[key], value)


if __name__ == '__main__':
  unittest.main()
