#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Command:

    command_number = 0
    total_price = 0

    def __init__(self, id_buyer, id_item, quantity_item, price_item):
        self.id_buyer = id_buyer
        self.id_item = id_item
        self.quantity_item = quantity_item
        self.price_item = price_item
        Command.command_number += 1
        Command.total_price += self.get_price()

    def __str__(self):
        ans = _("{}, {} : {} * {} = {}")
        return ans.format(self.id_buyer, self.id_item, self.price_item, self.quantity_item, self.price_item*self.quantity_item)

    def get_price(self) :
        return self.quantity_item*self.price_item

def get_number_total_commad() :
    return Command.command_number

def get_total_price() :
    return Command.total_price
