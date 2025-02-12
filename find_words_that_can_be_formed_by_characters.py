from collections import Counter, defaultdict
from typing import List


def countCharacters(words: List[str], chars: str) -> int:
    res = 0
    count = Counter(chars)
    print(count)

    for w in words:
        cur_word = defaultdict(int)
        for c in w:
            cur_word[c] += 1
            good = True
            if c not in count or cur_word[c] > count[c]:
                good = False
                break
        if good:
            res += len(w)

    return res




if __name__ == '__main__':
    print(countCharacters(["cat","bt","hat","tree"], "atach"))
