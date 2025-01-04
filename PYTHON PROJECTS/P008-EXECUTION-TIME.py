from time import time

start = time()

for i in range (1_000):
    print(i)
    
end = time()

print(f"Execution time: {end-start}")