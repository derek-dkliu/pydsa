def pattern_match(pat, text):
    if pat is None or pat == '':
        raise Exception('Pattern should not be empty')
    acount = 0
    bcount = 0
    for c in pat:
        if c == 'a': acount += 1
        elif c == 'b': bcount += 1
        else: raise Exception('Invalid pattern')
    if acount == 0:
        return single_pattern(bcount, text)
    elif bcount == 0:
        return single_pattern(acount, text)

    for alen in range(1, len(text)):
        rem = len(text) - acount * alen
        if rem < bcount:
            break
        elif rem % bcount != 0:
            continue
        blen = rem // bcount
        index = 0
        apat = None
        bpat = None
        matched = True
        for c in pat:
            step = alen if c == 'a' else blen
            part = text[index:index+step]
            index += step
            if c == 'a':
                if apat is None:
                    apat = part
                elif part != apat:
                    matched = False
                    break
            else:
                if bpat is None:
                    bpat = part
                elif part != bpat:  
                    matched = False
                    break
        if matched:
            return True
    return False

def single_pattern(count, text):
    if len(text) % count != 0 or count > len(text):
        return False
    step = len(text) // count
    pat = text[0:step]
    index = step
    while index + step <= len(text):
        if text[index:index+step] != pat:
            return False
        index += step
    return True


def pattern_match2(pat, text):
    if pat is None or pat == '':
        raise Exception('Pattern should not be empty')

    char_main = pat[0]
    char_alt = 'b' if char_main == 'a' else 'a'
    first_alt = pat.find(char_alt)
    cnt_main = count_char(pat, char_main)
    cnt_alt = len(pat) - cnt_main
    maxsize = len(text) // cnt_main
    for size_main in range(maxsize + 1):
        rem = len(text) - cnt_main * size_main
        if cnt_alt == 0 and rem != 0:
            continue
        pat_main = text[0:size_main]
        if cnt_alt == 0 or rem % cnt_alt == 0:
            size_alt = 0 if cnt_alt == 0 else rem // cnt_alt
            start_alt = size_main * first_alt
            pat_alt = text[start_alt: start_alt + size_alt]
            if matched(text, pat, pat_main, pat_alt, size_main, size_alt):
                return True
    return False

def matched(text, pat, pat_main, pat_alt, size_main, size_alt):
    char_main = pat[0]
    index = 0
    for c in pat:
        step = size_main if c == char_main else size_alt
        s = text[index:index+step]
        index += step
        if c == char_main:
            if s != pat_main:
                return False
        else:
            if s != pat_alt:
                return False
    return True

def count_char(pat, t):
    count = 0
    for c in pat:
        if c == t:
            count += 1
    return count

cases = [
    ['aabab', 'catcatgocatgo'],
    ['abb', 'catcatgocatgo'],
    ['baa', 'catcatgocatgo'],
    ['ab', 'catcatgocatgo'],
    ['a', 'catcatgocatgo'],
    ['b', 'catcatgocatgo'],
    ['aa', 'ccc'],
    ['aa', 'cccc']
]
for pat, text in cases:
    print(pattern_match(pat, text), pattern_match2(pat, text))

