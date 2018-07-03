#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import string
import random
import unicodedata

import CorrAmazon as corr
import amazon


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


class TestStudent(unittest.TestCase):
    def test_exist(self):
        self.assertTrue((hasattr(amazon, '__init__') and hasattr(amazon, '__str__')),
                        _("You did not provide the init or str methods."))

    def test_str(self):
        id_buyer = random.randint(0,100)
        id_item = random.randint(0,100)
        price = random.randint(0,100)
        quantity = random.randint(0,100)
        ans = _("With the following data: {}, {}, {}, {} for the command created, you returned {} instead of {}")
        stu_ans = amazon.Command(id_buyer, id_item, price, quantity)
        corr_ans = corr.Command(id_buyer, id_item, price, quantity)
        self.assertEqual(equal_string(str(corr_ans)), equal_string(str(stu_ans)), ans.format(id_buyer, id_item, price,
                                                                                             quantity, stu_ans, corr_ans))


    def test_helper(self):
        id_buyer = random.randint(0,100)
        id_item = random.randint(0,100)
        price = random.randint(0,100)
        quantity = random.randint(0,100)
        number = random.randint(10,100)
        total_price = 0
        for i in range(0,number):
            amazon.Command(id_buyer, id_item, price, quantity)
            total_price += price*quantity
        self.assertEqual(number, amazon.get_number_total_command(),msg="you do not get the correct number of Command")
        self.assertEqual(total_price, amazon.get_total_price(),msg="you do not get the correct total price of all Command")


if __name__ == '__main__':
    unittest.main()
