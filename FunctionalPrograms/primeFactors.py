class primeFactors:
    def factorPrime(n):
        factor = 2
        for factor in range(2,factor*factor <= n):
            while n % factor == 0:
                print(factor, " ")
                n = n/factor
        return factor


def main():
    print("Enter the number")
    n = int(input())
    pf = primeFactors()
    pf.factorPrime(n)


if __name__ == "__main__":
    main()
