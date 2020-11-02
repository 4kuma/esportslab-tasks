def prime_divisors(number):
    return [i for i in range(2, number + 1) if number % i == 0 and is_prime(i)]


def is_prime(number):
    for i in range(2, int((number ** (1 / 2)) + 1)):
        if number % i == 0:
            return False
    return True


def primes(numbers):
    prime_dividers_set = sorted(
        list(set([item for sublist in [prime_divisors(abs(i)) for i in numbers] for item in sublist])))
    return [[i, sum(x for x in numbers if x % i == 0)] for i in prime_dividers_set]


def main():
    print(primes([12, 15]))


if __name__ == "__main__":
    main()
