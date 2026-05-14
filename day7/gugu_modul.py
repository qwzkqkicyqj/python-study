def v_gugudan():
    for i in range(1, 10):
        print(f"{i}단")
        for j in range(1, 10):
            print(f"{i}x{j}={i*j}")
        print()

def h_gugudan():
    for i in range(1, 10):
        print(f"{i}단",end="\t")
        for j in range(1, 10):
            print(f"{i}x{j}={i*j}", end="\t")
        print()