
require 'coveralls'
Coveralls.wear!

import unittest
from credit_card_val import credit_card_vali

class test_credit_card_vali():

    def test_validity(self):
        self.assertAlmostEqual('79927398713',True)
        self.assertAlmostEqual('79927398715',False)
        self.assertAlmostEqual('79927398710',False)

    def test_values(self):
        #make sure it rises a value error
        self.assertRaises(ValueError,"")
