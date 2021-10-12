import time
from itertools import product


start_time = time.time()

combo = (8, 9, 1, 1, 4, 7, 1, 8)

for perm in product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=len(combo)):
    if perm == combo:
        print(f"Взломано! {combo} {perm}")

end_time = time.time()
print(f"\nВремя выполнения составило {end_time - start_time} секунд.")