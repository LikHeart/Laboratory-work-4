import time

def benchmark(size):
    print(f"size: {size}")
    loop_times = []
    comp_times = []
    for _ in range(7):
        start_time = time.time()
        res1 = []
        for x in range(size):
            if x % 2 == 0:
                res1.append(x ** 2)
        loop_times.append(time.time() - start_time)
        start_time = time.time()
        res2 = [x**2 for x in range(size) if x % 2 == 0]
        comp_times.append(time.time() - start_time)
    avg_loop = sum(loop_times) / len(loop_times)
    avg_comp = sum(comp_times) / len(comp_times)
    print(res1 == res2)
    print(f"avg_loop: {avg_loop:.5f} сек.")
    print(f"avg_comp: {avg_comp:.5f} сек.")
    print(f"avg_loop/avg_comp {avg_loop/avg_comp:.5f}")
benchmark(10_000)
benchmark(100_000)
benchmark(1_000_000)
