class Sieve:
    prime_list = list()

    def __init__(self) -> None:
        i = 2
        x = 0
        prime = True
        while x <= 1000000:
            f = 2
            while f < i:
                if i % f != 0:
                    prime = True
                elif i % f == 0:
                    prime = False
                    break
                f += 1
            if prime:
                self.prime_list.append(i)
                x += 1
            i += 1

    def nth_prime(self, n: int) -> int:
        return self.prime_list[n]
