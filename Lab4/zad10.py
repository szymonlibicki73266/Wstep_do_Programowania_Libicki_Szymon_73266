def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Przenieś dysk z {source} do {target}")
    else:
        hanoi(n-1, source, auxiliary, target)
        print(f"Przenieś dysk z {source} do {target}")
        hanoi(n-1, auxiliary, target, source)