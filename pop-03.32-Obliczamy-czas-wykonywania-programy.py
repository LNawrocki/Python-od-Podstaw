import time

start_time = time.time()

for _ in range(10000000):
    pass

end_time = time.time()

print(f'Czasy wykonywania programu: {(end_time - start_time)} sekund')
