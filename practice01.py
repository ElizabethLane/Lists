def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """
    ascending_list = []
    while items:
        numbers_list = items[0]
        for number in items:
            if number > numbers_list:
                numbers_list = number
        ascending_list.append(numbers_list)
        items.remove(numbers_list)
        
        ascending_to_n_list = ascending_list[:n]
        ascending_to_n_list_final = ascending_to_n_list[::-1]
        


    return ascending_to_n_list_final


print largest_n_items([1,400, 300,100000,7,1000], 2)