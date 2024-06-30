from collections.abc import Sequence
from typing import Final

from gilded_rose.rules import *

__all__ = ("DEFAULT_RULES", "Item", "GildedRose")

DEFAULT_RULES: Final[Sequence[type[Rule]]] = (
    AgedBrie,
    BackstagePass,
    Sulfuras,
    DefaultRule,
)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:
    def __init__(
          self,
          items: Sequence[Item],
          rules: Sequence[Rule] = DEFAULT_RULES,
    ):
        self.items = items
        self._rules = rules

    def update_quality(self) -> None:
        for item in self.items:
            rule = next(rule for rule in self._rules if rule.is_match(item))
            rule.update(item)
