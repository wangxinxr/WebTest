from math import sqrt

def is_prime(n):
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False
    
def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs = []
    try:
        for filename in filenames:
            fs.append(open(filename, 'w', encoding='utf-8'))
        for n in range(1, 2000):
            if is_prime(n):
                if n < 100:
                    fs[0].write(str(n) + '\n')
                elif n < 1000:
                    fs[1].write(str(n) + '\n')
                else:
                    fs[2].write(str(n) + '\n')
    except IOError as ex:
        print(ex)
        print('输入错误')
    finally:
        for filename in fs:
            filename.close()
    print('操作完成')

if __name__ == "__main__":
    main()    