n = int(input())
print(sum(1 for i in range(1, int(n**0.5) + 1) if n % i == 0) * 2 - (int(n**0.5)**2 == n))