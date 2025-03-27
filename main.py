# recitation-05

from collections import defaultdict


import random, time
import tabulate

def ssort(L):
    ### selection sort
    if (len(L) == 1):
        return(L)
    else:
        m = L.index(min(L))
        #print('selecting minimum %s' % L[m])
        L[0], L[m] = L[m], L[0]
        #print('recursively sorting L=%s\n' % L[1:])
        return [L[0]] + ssort(L[1:])

def qsort(a, pivot_fn):
    l = []
    r = []
    if len(a) == 0:
        return a
    else:

        for value in a:
            if value <= pivot_fn:
                l.append(value)
            elif value >= pivot_fn:
                r.append(value)
            L, R = qsort(l, pivot_fn), qsort(r, pivot_fn)
        return L.append(value).append(R)
def qsort_curry(a):
    def sort(pivot_fn):
        l = []
        r = []
        def step_a(a):
            if len(a)==0:
                return a
            else:
                for value in a:
                    if a <= pivot_fn:
                        l.append(value)
                    elif a >= pivot_fn:
                        r.append(value)
                L, R = qsort(l, pivot_fn), qsort(r, pivot_fn)
            return L.append(value).append(R)
        return step_a
    return sort

def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds.
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """

    qsort_fixed_pivot = qsort_curry(sizes[0])
    qsort_random_pivot = qsort_curry(sizes[random.randrange(len(sizes))])
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_fixed_pivot, mylist),
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print("/n")
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
