#!/usr/local/bin/python3

from order import Order
from shipper import Shipper

from fedex_strategy import FedExStrategy
from postal_strategy import PostalStrategy
from ups_strategy import UPSStrategy
from shipping_cost import ShippingCost
# Test Federal Express shipping

order = Order()
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.00

order = Order()
strategy = UPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.00

order = Order()
strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.00