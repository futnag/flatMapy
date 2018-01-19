from itertools import chain

def flatten(l):
    ltype = type(l)
    return ltype(chain(*l))


def flatmap(func, l):
    ltype = type(l)
    return ltype(flatten([map(func, elem) for elem in l]))


def flat_all(l):
    ltype = type(l)
    l = list(l)
    out = []
    while l:
        while l and isinstance(l[0], (list, tuple)):
            l[0:1] = l[0]
        if l:
            out.append(l.pop(0))
    return ltype(out)



if __name__ == '__main__':
    print("hello!")