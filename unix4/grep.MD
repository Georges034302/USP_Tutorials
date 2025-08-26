# GREP & SED Cheat Sheet (Applied to `demo.txt`)

This guide shows commands and what they *do* (not whether they match your file).

---

## 🔎 GREP

### 1) Basics, case, word boundaries
```bash
grep unix demo.txt                  # search for substring "unix"
grep -i unix demo.txt               # case-insensitive search
grep -w unix demo.txt               # whole-word search for "unix"
grep -wi unix demo.txt              # whole-word + ignore case
grep -n unix demo.txt               # show line numbers with matches
grep -H unix demo.txt               # show filename with matches
grep -c unix demo.txt               # count number of matches
grep -m 2 unix demo.txt             # stop after 2 matches
grep -v unix demo.txt               # print lines that DO NOT match "unix"
grep -F 'GREP & SED' demo.txt       # fixed-string search (no regex)
grep -f patterns.txt demo.txt       # read patterns from file
grep -q unix demo.txt               # quiet mode (status only, no output)
```

### 2) Character classes / counts / anchors
```bash
grep '[A-Z]' demo.txt               # any uppercase letter A–Z
grep -E '[A-Z]{3}' demo.txt         # 3 consecutive uppercase letters
grep -E '^[A-Z]{4}' demo.txt        # line starts with 4 uppercase letters
grep -E '[A-Z]{4}$' demo.txt        # line ends with 4 uppercase letters

grep '[0-9]' demo.txt               # any digit
grep -E '^[0-9]' demo.txt           # line begins with a digit
grep -E '[0-9]{2}' demo.txt         # exactly 2 consecutive digits
grep -E '[0-9]{3,4}' demo.txt       # 3 or 4 consecutive digits
grep -E '[0-9]$' demo.txt           # line ends with a digit

grep '^' demo.txt                   # start-of-line anchor (matches every line)
grep '$' demo.txt                   # end-of-line anchor (matches every line)
grep '^$' demo.txt                  # blank lines
grep -v '^$' demo.txt               # non-blank lines
grep '\$$' demo.txt                 # line ending with literal "$"
```

### 3) Escapes, brackets, special chars
```bash
grep '\\\\' demo.txt                # lines containing a backslash "\"
grep '^\\\\' demo.txt               # lines starting with "\"
grep -E '\\[[0-9]\\]' demo.txt      # literal bracketed digit like "[7]"
grep -E '\\[[0-9]{2}\\]' demo.txt   # literal bracketed two digits like "[12]"
grep -E '( )$' demo.txt             # ends with a literal space (ERE)
```

### 4) OR / AND / grouping
```bash
grep -E '#|[0-9]' demo.txt          # "#" OR any digit
grep -E '^#|:|[0-9]$' demo.txt      # starts "#", OR contains ":", OR ends with digit
grep -e '#' -e ':' -e '[0-9]' demo.txt  # multiple -e (OR)

grep '#' demo.txt | grep '[0-9]'          # AND via pipeline: "#" AND a digit
grep '#' demo.txt | grep -E '[0-9]{4}'    # AND: "#" AND 4 digits
grep '#' demo.txt | grep -E '[0-9]{4}' | grep ':'  # AND: "#", 4 digits, AND ":"

grep -E '[A-Z].*[0-9]' demo.txt     # uppercase followed later by a digit
grep -E '^[A-Z].*[0-9]' demo.txt    # starts uppercase, later a digit
grep -E '[A-Z].*[0-9]{3}$' demo.txt # has uppercase, ends with exactly 3 digits
```

### 5) Recursive search (projects) + filters
```bash
grep -R  'unix' ~/USP/              # recursive search for "unix"
grep -ER '([0-9]{4})' ~/USP/        # recursive, extended regex (4 digits)
grep -ERin 'unix' ~/USP/            # recursive, case-insens., show line numbers
grep -ERinl 'unix' ~/USP/           # recursive, list files with matches
grep -ERino 'unix' ~/USP/           # recursive, print only the matching part

grep -R --include='*.txt' unix .    # only search *.txt files
grep -R --exclude-dir='.git' unix . # exclude a directory
grep -Zrl unix . | xargs -0 sed -n '1p'  # null-delimited results for safe piping
```

### 6) PCRE (Perl) extras (`grep -P`)
```bash
grep -Po '\\bgrep\\b' demo.txt      # word-boundary match; print only the match
grep -Poi '\\b(regex|sed|grep)\\b' demo.txt  # alternation with ignore case
grep -P '(?<=#)\\w+' demo.txt       # positive lookbehind: word chars after "#"
grep -P '\\d{2,4}(?=\\])' demo.txt  # lookahead: 2–4 digits before a "]"
```

---

