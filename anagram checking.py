def check_anagram(data1, data2):
    data1 = data1.lower()
    data2 = data2.lower()
    if sorted(data1) != sorted(data2):
        return False
    return all(data1[i] != data2[i] for i in range(len(data1)))
