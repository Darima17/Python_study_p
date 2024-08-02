import random
import time

def emit_gel(step: int):
    pressure = random.randint(0, 100)
    sign = 1
    while True:
        step_size = random.randint(0, step)
        f = yield pressure
        if f is not None:
            sign *= f
        pressure += step_size * sign

def valve():
    step = 20  # Set the initial step size
    gen = emit_gel(step)
    sign = 1
    while True:
        try:
            pressure = next(gen)
            yield pressure
            if pressure < 20 and sign == -1:
                sign = 1
                gen.send(-1)
            elif pressure > 80 and sign == 1:
                sign = -1
                gen.send(-1)
            if pressure > 90 or pressure < 10:
                gen.close()
                break
        except StopIteration:
            break

if __name__ == '__main__':
    result = valve()
    for i in result:
        print(i)
        time.sleep(1)
