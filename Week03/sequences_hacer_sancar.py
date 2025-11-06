def remove_duplicates(seq: list) -> list:    
    new_list = []    
    for item in seq:
        # Öğe, yeni listede daha önce yoksa ekle.
        if item not in new_list:
            new_list.append(item)           
    return new_list

def list_counts(seq: list) -> dict:
    my_dict=dict()
    for i in range(len(seq)):
        my_dict[seq[i]] = seq.count(seq[i])
    return my_dict

def reverse_dict(d: dict) -> dict:
    my_dict=dict()
    for key,value in d.items():
        my_dict[value] =key
    return my_dict
