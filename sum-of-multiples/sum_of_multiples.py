def sum_of_multiples(limit, multiples):
    list_multiples = []
    for m in multiples :
        [ list_multiples.append(i) for i in range(0,limit,m) if i not in list_multiples ]
    return sum(list_multiples)
