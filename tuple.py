def add(a: int, b: int) -> int:
    return a + b
def QuotientRemainder(a: int, b: int) -> tuple[int, int]:
    return (a // b, a % b)
def GenerateSeries() -> list[float]:
    return [value for value in range(10, 1000, 50)]
def main():
    x, y = QuotientRemainder(10, 3)
    print(x)
    print(y)
    print(GenerateSeries())
main()