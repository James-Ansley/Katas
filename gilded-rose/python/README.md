# Gilded Rose

Taken from: <https://github.com/emilybache/GildedRose-Refactoring-Kata>

## Comments

Yeowzah! What a refactoring exercise. I found the ApprovalTest's
`verify_all_combinations` function helpful for this exercise. It allowed me to
quickly get 100% branch coverage, which then meant I could (reasonably) safely
refactor.

Eventually, I decided to pull out update rules into `Rule` strategies which are
enumerated for each item when updating. Since it was unclear (I guess,
intentionally) in the problem description, I was unsure whether the "Conjured"
idea applied to all items or just "default" items. I decided to apply the
conjured rules to all items and made them part of each rule. I also toyed with
the idea of just having duplicate rules to handle each case (i.e. a rule
for `AgedBrie` and a separate rule for `ConjuredAgedBrie`). It might have been
possible to create an even more generic set of strategies that could
automatically apply the conjured logic.

If I were a better person, I would have gone on to write unit tests for all
the `Rule` strategies :^)
