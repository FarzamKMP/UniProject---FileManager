import random
import time
import matplotlib.pyplot as plt

# دکوراتور برای اندازه‌گیری زمان اجرای تابع
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' took {end - start:.4f} seconds.")
        return result
    return wrapper

# ژنراتور تولید اعداد تصادفی بین 1 تا 6
def dice_generator(count, seed_value=None):
    if seed_value is not None:
        random.seed(seed_value)
    for _ in range(count):
        yield random.randint(1, 6)

# تابع تولید داده‌ها با ژنراتور و ذخیره در لیست
@timer
def generate_data(count, seed_value=None):
    gen = dice_generator(count, seed_value)
    data = list(gen)
    return data

# تابع رسم هیستوگرام
def plot_histogram(data, count):
    plt.hist(data, bins=range(1,8), align='left', rwidth=0.8, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {count} dice rolls')
    plt.xlabel('Dice Face')
    plt.ylabel('Frequency')
    plt.xticks(range(1,7))
    plt.show()

# اجرای پروژه برای اندازه‌های مختلف داده
def main():
    sizes = [10, 100, 1000, 10000, 50000, 100000]
    seed_value = 42  # ثابت نگه داشتن بذر تصادفی
    for size in sizes:
        print(f"\nGenerating {size} dice rolls:")
        data = generate_data(size, seed_value)
        print(f"Max roll: {max(data)}")
        plot_histogram(data, size)

if __name__ == "__main__":
    main()
