def merge_intersected_strings(str1: str, str2: str) -> str:
    for i in range(len(str1)):
        if str2.startswith(str1[i:]):
            return str1[:i] + str2
    return str1 + str2
