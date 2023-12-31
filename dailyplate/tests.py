#!/usr/bin/env python3
import unittest
from homeapp.utilities import calculate_bmi, construct_prompt

class TestUtilitiyFunctions(unittest.TestCase):
  def test_calculate_BMI(self):
    self.assertEqual(calculate_bmi(1.65, 68), 24.98)

  def test_construct_prompt_returns_string(self):
    result = construct_prompt("dailyplate/prompts/prompt4.txt", [])
    self.assertIsInstance(result, str)

if __name__ == "__main__":
  unittest.main()
