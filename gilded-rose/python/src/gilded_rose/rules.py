import abc
from typing import TYPE_CHECKING, final

if TYPE_CHECKING:
    from gilded_rose import Item

__all__ = (
    "Rule",
    "AgedBrie",
    "BackstagePass",
    "Sulfuras",
    "DefaultRule",
)


class Rule(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def is_match(cls, item: "Item") -> bool:
        ...

    @staticmethod
    def is_conjured(item: "Item") -> bool:
        return item.name.startswith("Conjured")

    @classmethod
    @final
    def update(cls, item: "Item") -> None:
        if cls.is_conjured(item):
            cls.update_conjured(item)
        else:
            cls.update_regular(item)

    @classmethod
    @abc.abstractmethod
    def update_regular(cls, item: "Item") -> None:
        ...

    @classmethod
    @abc.abstractmethod
    def update_conjured(cls, item: "Item") -> None:
        ...


class AgedBrie(Rule):
    @classmethod
    def is_match(cls, item: "Item") -> bool:
        return item.name == "Aged Brie" or item.name == "Conjured Aged Brie"

    @classmethod
    def update_regular(cls, item: "Item") -> None:
        quality_delta = 2 if item.sell_in <= 0 else 1
        item.quality = min(50, item.quality + quality_delta)
        item.sell_in = item.sell_in - 1

    @classmethod
    def update_conjured(cls, item: "Item") -> None:
        quality_delta = 4 if item.sell_in <= 0 else 2
        item.quality = min(50, item.quality + quality_delta)
        item.sell_in = item.sell_in - 1


class BackstagePass(Rule):
    @classmethod
    def is_match(cls, item: "Item") -> bool:
        return (
              item.name.startswith("Backstage pass")
              or item.name.startswith("Conjured backstage pass")
        )

    @classmethod
    def _regular_quality_delta(cls, sell_in: int) -> int:
        if 0 < sell_in <= 5:
            return 3
        elif 5 < sell_in <= 10:
            return 2
        else:
            return 1

    @classmethod
    def update_regular(cls, item: "Item") -> None:
        if item.sell_in <= 0:
            item.quality = 0
        else:
            delta = cls._regular_quality_delta(item.sell_in)
            item.quality = min(50, item.quality + delta)
        item.sell_in = item.sell_in - 1

    @classmethod
    def update_conjured(cls, item: "Item") -> None:
        if item.sell_in <= 0:
            item.quality = 0
        else:
            delta = cls._regular_quality_delta(item.sell_in)
            item.quality = min(50, item.quality + 2 * delta)
        item.sell_in = item.sell_in - 1


class Sulfuras(Rule):
    @classmethod
    def is_match(cls, item: "Item") -> bool:
        return "Sulfuras" in item.name

    @classmethod
    def update_regular(cls, item: "Item") -> None:
        pass

    @classmethod
    def update_conjured(cls, item: "Item") -> None:
        pass


class DefaultRule(Rule):
    @classmethod
    def is_match(cls, item: "Item") -> bool:
        return True

    @classmethod
    def update_regular(cls, item: "Item") -> None:
        quality_delta = -2 if item.sell_in <= 0 else -1
        item.quality = max(0, item.quality + quality_delta)
        item.sell_in = item.sell_in - 1

    @classmethod
    def update_conjured(cls, item: "Item") -> None:
        quality_delta = -4 if item.sell_in <= 0 else -2
        item.quality = max(0, item.quality + quality_delta)
        item.sell_in = item.sell_in - 1
