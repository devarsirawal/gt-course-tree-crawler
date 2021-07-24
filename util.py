def is_single_course(clause):
    return type(clause) is not list

def is_null_set(clause):
    return type(clause) is list and len(clause) == 1

def is_single_and(clause):
    if len(clause) < 1:
        return False
    return type(clause[1]) is list \
            and len(clause[1:]) == 1 \
            and clause[1][0] == "and"

def extract_prereq_ids(data):
    
    if len(data) > 0:
        ids = [p["id"] for p in flatten_prereq(data)]
    else:
        ids = []
    return ids

def flatten_prereq(x):
        if isinstance(x, list):
            return [a for i in x for a in flatten_prereq(i) if type(a) == dict]
        else:
            return [x]

def flatten(L):
    assert type(L) is list
    flat_list = []
    for i in L:
        if type(i) is not list:
            flat_list += [i] 
        else:
            flat_list += flatten(i)
    return flat_list

def flatten_clause(source):
    def flatten_inner(clause):
        if is_single_course(clause):
            return clause

        operator, *children = clause

        if len(children) == 1:
            return flatten_inner(children[0])

        new_children = []
        for child in children:
            flattened = flatten_inner(child)
            if (is_null_set(flattened)):
                continue

            if type(flattened) is list and flattened[0] == operator:
                new_children += flattened[1:]
            else:
                new_children.append(flattened)

        return [operator] + list(map(flatten_inner, children))

    operator, *children = source
    transformed_children = list(filter(lambda c: not is_null_set(c), map(flatten_inner, children)))
    return [operator] + transformed_children

