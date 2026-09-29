import random


def run_block_2(n=1000000):
    count_a = 0
    count_b = 0
    count_a_and_b = 0
    count_a_or_b = 0
    count_not_a = 0

    for _ in range(n):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        is_a = (d1 + d2) == 8
        is_b = (d1 >= 5) or (d2 >= 5)

        if is_a:
            count_a += 1
        if is_b:
            count_b += 1
        if is_a and is_b:
            count_a_and_b += 1
        if is_a or is_b:
            count_a_or_b += 1
        if not is_a:
            count_not_a += 1

    p_a = count_a / n
    p_b = count_b / n
    p_ab = count_a_and_b / n
    p_aub = count_a_or_b / n
    p_na = count_not_a / n

    t_a = 5 / 36
    t_b = 20 / 36
    t_ab = 4 / 36
    t_aub = 21 / 36
    t_na = 31 / 36

    print("--- БЛОК 2: Варіант 1 (Дві кістки) ---")
    print(f"P(A): stat = {p_a:.5f}, theor = {t_a:.5f}, delta = {abs(p_a - t_a):.5f}")
    print(f"P(B): stat = {p_b:.5f}, theor = {t_b:.5f}, delta = {abs(p_b - t_b):.5f}")
    print(f"P(A and B): stat = {p_ab:.5f}, theor = {t_ab:.5f}, delta = {abs(p_ab - t_ab):.5f}")
    print(f"P(A or B): stat = {p_aub:.5f}, theor = {t_aub:.5f}, delta = {abs(p_aub - t_aub):.5f}")
    print(f"P(not A): stat = {p_na:.5f}, theor = {t_na:.5f}, delta = {abs(p_na - t_na):.5f}")
    print(f"Перевірка P(not A) == 1 - P(A): {p_na:.5f} vs {1 - p_a:.5f}")


if __name__ == "__main__":
    run_block_2()