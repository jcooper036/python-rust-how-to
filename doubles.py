import numpy as np
import string
import random
import string_doubles

# use ZIP to find all instances of double letter pairs. You could use regex,
# or any number of better approaches. But you are a data scientist so this is
# the most likely way that the code is written.


def count_doubles(val: str) -> int:
    """
    wow such docstring

    Parameters
    ----------
    val: str

    Returns
    ----------
    int
        The number of letter pairs in val.
        i.e. val = 'abbcCddef' returns 2.
    """
    total = 0
    for (
        c1,
        c2,
    ) in zip(val, val[1:]):
        if c1 == c2:
            total += 1
    return total


def doubles_numpy(val: str) -> int:
    ng = np.frombuffer(bytes(val, "UTF-8"), dtype=np.byte)
    return np.sum(ng[:-1] == ng[1:])


# benchmark data for 1M random letters
val = "".join(random.choice(string.ascii_letters) for i in range(1000000))


def test_python_count_doubles(benchmark):
    benchmark(count_doubles, val)


def test_rust_count_doubles(benchmark):
    benchmark(string_doubles.count_doubles, val)


def test_rust_count_doubles_bytes(benchmark):
    benchmark(string_doubles.count_doubles_bytes, val)


def test_numpy_go_brrr(benchmark):
    benchmark(doubles_numpy, val)
