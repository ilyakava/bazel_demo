from third_party.version1.model import process as process1
from third_party.version2.model import process as process2

def myprocess(x):
    return x

def compare(x):
    return process1(x), process2(x), myprocess(x)

if __name__ == '__main__':
    print('Got      {}, {}, {}'.format(*compare(1)))
    print('Expected 2, 0, 1')
