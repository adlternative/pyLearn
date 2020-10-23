from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


recodes = [Stock('adl', 100, 200),Stock('ee',3,2)]
print (compute_cost(recodes))