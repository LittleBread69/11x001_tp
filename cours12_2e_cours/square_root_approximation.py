def square_root(q: float, epsilon: float = 1e-6):
    a = 0
    b = 1 + q
    
    while b-a>= epsilon:
        x = (a+b)/2
        if (x*x >= q):
            b = x
        else: a = x
        
    return x

if __name__ == "__main__":
    print(square_root(5))