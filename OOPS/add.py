class FactorFinder:
    def __init__(self, n):
        self.n = n

    def find_factors(self):
        def backtrack(remaining, start, path, result):
            if remaining == 1:
                if len(path) > 0:
                    result.append(path[:])  # Include [1, n] if n is prime
                return
            for i in range(start, remaining + 1):
                if remaining % i == 0:
                    path.append(i)
                    backtrack(remaining // i, i, path, result)
                    path.pop()

        result = []
        backtrack(self.n, 2, [], result)
        return result

if __name__ == '__main__':
    n = int(input())
    factor_finder = FactorFinder(n)
    print(factor_finder.find_factors())
