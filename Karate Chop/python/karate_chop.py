from collections.abc import Sequence


# Let us, for a moment, pretend the bisect module does not exist
#
# def chop[T](target: T, values: Sequence[T]) -> int:
#     idx = bisect_left(values, target)
#     return idx if idx < len(values) and values[idx] == target else -1


def chop[T](target: T, values: Sequence[T]) -> int:
    lo, hi = 0, len(values) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if values[mid] == target:
            return mid
        elif values[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

# A recursive solution
#
# def chop[T](target: T, values: Sequence[T]) -> int:
#     return chop_recursive_helper(target, values, 0, len(values) - 1)
#
#
# def chop_recursive_helper[T](
#       target: T, values: Sequence[T], lo: int, hi: int
# ) -> int:
#     mid = (lo + hi) // 2
#     if lo > hi:
#         return -1
#     elif values[mid] == target:
#         return mid
#     elif values[mid] > target:
#         return chop_recursive_helper(target, values, lo, mid - 1)
#     else:
#         return chop_recursive_helper(target, values, mid + 1, hi)
