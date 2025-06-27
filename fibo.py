def fibonacci(n):
    """
    n번째 피보나치 수를 반환하는 함수
    반복문 방식으로 구현
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")

if __name__ == "__main__":
    main()

