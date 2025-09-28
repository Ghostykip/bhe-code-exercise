class Sieve:
    prime_list = list()

    def __init__(self) -> None:
        i = 2
        x = 0
        prime = False
        while x < 10000:
            f = 0
            while f < i:
                if f != 0:
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
