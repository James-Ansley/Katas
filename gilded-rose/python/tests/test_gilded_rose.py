from itertools import product
from pprint import pformat

from approvaltests import verify_all_combinations

from gilded_rose import GildedRose, Item
from utils import test


def simulate_n_days_with_items(item, n_days) -> str:
    shop = GildedRose([Item(*item)])
    for _ in range(n_days):
        shop.update_quality()
    return pformat(shop.items[0])


def format_run(args, result):
    item_data, n_days = args
    item = Item(*item_data)
    return f"{str(item):>50} after {n_days:>2} days becomes: {result}\n"


@test
def regression_test():
    items = [
        ("Sulfuras, Hand of Ragnaros", 1, 80),
        ("Sulfuras, Hand of Ragnaros", -1, 80),
        *list(product(
            ["Aged Brie", "Conjured Aged Brie"], [-1, 0, 1], [0, 1, 2, 50],
        )),
        *list(product(
            [
                "Backstage passes to a TAFKAL80ETC concert",
                "Conjured backstage passes to a TAFKAL80ETC concert",
            ],
            [-1, 0, 1, 11],
            [0, 1, 2, 48, 50],
        )),
        *list(product(["Burt's Baked Beans"], [-1, 0, 1, 11], [0, 1, 2, 50])),
        *list(product(["Conjured Mana Cake"], [-1, 0, 1, 11], [0, 1, 2, 50])),
    ]
    verify_all_combinations(
        simulate_n_days_with_items, [items, range(10)], format_run,
    )
