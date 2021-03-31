import random
import sys
import pytest
from majority_element import majority_element


@pytest.mark.parametrize(
    "test_args, test_results",
    [
        ([], None),
        ([1], 1),
        ([1, 2], None),
        ([1, 2, 3], None),
        ([1, 2, 3, 2], None),
        ([1, 2, 3, 2, 2], 2),
    ],
)
def test_basic(test_args, test_results):
    assert majority_element(test_args) == test_results


class ListGenerator:
    def __init__(self, n_tests, list_size):
        self.n_tests = n_tests
        self.list_size = list_size

    def __call__(self):
        random.seed(42)
        for _ in range(self.n_tests):
            res_num = random.randint(0, sys.maxsize)
            res_num_count = random.randint(0, self.list_size)
            res_size = random.randint(0, self.list_size)
            res = list()
            for i in range(res_size):
                if i < res_num_count:
                    res.append(res_num)
                    continue
                while True:
                    tmp_num = random.randint(0, sys.maxsize)
                    if tmp_num != res_num:
                        break
                res.append(tmp_num)
            random.shuffle(res)
            if res_num_count <= res_size // 2:
                res_num = None
            yield res, res_num


# First param - number of tests(inputs)
# Second param - max size of testing list
@pytest.fixture(params=[[1000, 10000]])
def random_data(request):
    return ListGenerator(request.param[0], request.param[1])()


def test_large(random_data):
    for arg, res in random_data:
        assert majority_element(arg) == res
