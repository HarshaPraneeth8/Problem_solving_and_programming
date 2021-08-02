lst = [2,3,4]
def cumulative_product(lst):
    i=1
    print([(i := i*iter) for iter in lst])
cumulative_product(lst)
