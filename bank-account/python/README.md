# Bank Account

Kata from: <https://sammancoaching.org/kata_descriptions/bank_account.html>

## Comments

I have actually done this kata before and, on reflection, I had overengineered
it quite a bit. While this may be distressing to hear, the last time I did this
kata I didn't use TDD (I'll give you a moment to get over the shock)...

This time, I worked on this kata with simple tests following the faithful
red-green-refactor, and I feel things are much simpler. In the last iteration,
I had many gadgets and gizmos like _TableFormatter_ classes to make sure the
bank statement was being formatted _properly_. But doing this kata again and
guided by my tests, I have eschewed any tantalizing thoughts of heavenly
temptations such as extra abstractions or interfaces.

This has really crystallized the _YAGNI_ and _KISS_ concepts for me. Because in
reality, this kata is simple and loosely specified (e.g. what happens if there
are multiple translations on the same day?), so why make the design overly
complicated?

This kata also led to some cute tests using approvals, the much underloved
`redirect_stdout` context manager from the `contextlib` module, and the
`freezegun` package to manage setting the date for transactions.

### Pain Points

One thing I was unsure of when working on this kata was how robust to make
transactions. For example, as the project currently stands, if multiple
transactions happen on the same day, they are simply overwritten; or, someone
could, if they wanted to, deposit or withdraw a negative amount of money.
If this were a "real" system, I would imagine these things would need to be
guarded against. But the kata does not mention what to do in these cases, so I
have ignored them.
