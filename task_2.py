def get_n_basket_with_fake_coins(n: int, w: int, d: int, p: int) -> int:
    n_basket = int((((n - 1) * n / 2) * w - p) / d)
    return n_basket or n
