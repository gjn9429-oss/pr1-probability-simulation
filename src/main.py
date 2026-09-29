import os
import math
import random
import matplotlib.pyplot as plt
from block2_variants import run_block_2


def run_block_1():
    print("--- БЛОК 1: Закон великих чисел ---")
    p_theor = 0.5
    n_values = [10, 100, 1000, 10000, 100000, 1000000]
    frequencies = []

    for n in n_values:
        success = 0
        for _ in range(n):
            if random.random() < p_theor:
                success += 1
        w = success / n
        delta = abs(w - p_theor)
        frequencies.append(w)
        print(f"N = {n:<8} | W = {w:<8.5f} | Delta = {delta:<8.5f}")

    return n_values, frequencies


def run_block_3(n=100000):
    print("\n--- БЛОК 3: Метод Монте-Карло для числа Pi ---")
    m = 0
    step = 500
    points_x = []
    pi_values = []

    for i in range(1, n + 1):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x * x + y * y <= 1:
            m += 1

        if i % step == 0:
            current_pi = 4 * m / i
            points_x.append(i)
            pi_values.append(current_pi)

    final_pi = 4 * m / n
    print(f"Оцінка Pi для N = {n}: {final_pi:.5f}")
    print(f"Точне значення math.pi: {math.pi:.5f}")
    print(f"Похибка: {abs(final_pi - math.pi):.5f}")

    return points_x, pi_values


def run_block_4():
    print("\n--- БЛОК 4: Інженерна задача (Варіант 1) ---")
    total_runs = 5000
    failed_runs = 75

    p_error = failed_runs / total_runs
    p_success = 1 - p_error

    print(f"Загальна кількість запусків: {total_runs}")
    print(f"Кількість помилок: {failed_runs}")
    print(f"P(Error) = {p_error:.4f} ({p_error * 100:.2f}%)")
    print(f"P(Success) = {p_success:.4f} ({p_success * 100:.2f}%)")


def main():
    os.makedirs("graphics", exist_ok=True)

    n_vals, freqs = run_block_1()

    print()
    run_block_2()

    pts_x, pi_vals = run_block_3(100000)

    run_block_4()

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(n_vals, freqs, marker='o', label="W(A)")
    plt.axhline(0.5, color='r', linestyle='--', label="P(A) = 0.5")
    plt.xscale("log")
    plt.xlabel("Кількість випробувань N")
    plt.ylabel("Частота W(A)")
    plt.title("Блок 1: Закон великих чисел")
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(pts_x, pi_vals, label="Оцінка Pi")
    plt.axhline(math.pi, color='r', linestyle='--', label=f"math.pi ({math.pi:.4f})")
    plt.xscale("log")
    plt.xlabel("Кількість точок N")
    plt.ylabel("Значення Pi")
    plt.title("Блок 3: Оцінка Pi (Монте-Карло)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig("graphics/simulation_results.png", dpi=300)
    print("\nГрафіки збережено у graphics/simulation_results.png")
    plt.show()


if __name__ == "__main__":
    main()