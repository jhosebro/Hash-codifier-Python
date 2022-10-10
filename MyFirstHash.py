import hashlib


class HASH:
    def generateHash(h):
        digest = h.hexdigest()
        return digest


x = 0

while x < 1:
    print("Choose a hash algorithm: ")
    print("1. SHA256")
    print("2. SHA512")
    print("3. Exit")
    nAlgorithm = int(input())

    algorithm = ""
    if nAlgorithm != 3:

        if nAlgorithm == 1:
            print("Introduce data to hash: ")
            data = input()
            algorithm = "sha256"
        elif nAlgorithm == 2:
            print("Introduce data to hash: ")
            data = input()
            algorithm = "sha512"

        bdata = bytes(data, 'utf-8')
        h = hashlib.new(algorithm, bdata)
        hash1 = HASH.generateHash(h)
        print()
        print(hash1)
        print()

        x=0
    else:
        x=1
print("Bye!")
