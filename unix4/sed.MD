# SED Cheat Sheet



### 1) Print & selection
```bash
sed '=' demo.txt                    # print line numbers
sed -n '1,5p' demo.txt              # print lines 1–5
sed -n '$p' demo.txt                # print the last line
sed -n '/^$/p' demo.txt             # print blank lines
sed -n '/grep/Ip' demo.txt          # print lines containing "grep" (ignore case)
sed -n '/grep/,/unix/p' demo.txt    # print from a line matching "grep" to one matching "unix"
sed -n '1~2p' demo.txt              # print every 2nd line starting at 1 (GNU sed)
sed -n '2,+5p' demo.txt             # print 5 lines starting at line 2 (2..7)
```

### 2) Substitute (search/replace)
```bash
sed 's/unix/linux/' demo.txt        # replace first "unix" per line
sed 's/unix/linux/gi' demo.txt      # replace all case-insensitively
sed 's/\\( \\)/~/' demo.txt         # replace the first literal space with "~"
sed 's/\\\\/~/g' demo.txt           # replace "\" with "~" globally
sed 's/[#$^*()-:\\]/@/g' demo.txt   # replace any listed special with "@"
sed 's/[#$^*()-:\\]/ /g' demo.txt   # replace any listed special with a space
sed -E 's/([A-Za-z]+):[ ]*(.+)/\\1 => \\2/' demo.txt  # capture + backreference
sed 's/\\<grep\\>/sed/gI' demo.txt  # replace whole word "grep" with "sed" (GNU word-boundaries)
```

### 3) Print-on-substitute (verify changes)
```bash
sed -n 's/grep/USP/pi' demo.txt     # substitute "grep"→"USP"; print if changed
sed -n 's/^\\*/@/p' demo.txt        # replace leading "*" with "@" and print when changed
sed -n 's/\\$$/@/p' demo.txt        # replace trailing "$" with "@" and print when changed
sed -n 's/^$/BLANK LINE/p' demo.txt # replace blank line with literal text
sed -n 's/[A-Z]/ /gp' demo.txt      # replace uppercase letters with spaces; print changed lines
sed -n 's/[[:space:]]$/@/p' demo.txt # mark trailing whitespace with "@"; print if changed
```

### 4) Delete / keep
```bash
sed '5,25d' demo.txt                # delete lines 5–25
sed '5,$d' demo.txt                 # delete from line 5 to end
sed '5,$!d' demo.txt                # keep only lines 5 to end
sed '/grep/Id' demo.txt             # delete lines that match "grep" (ignore case)
sed '/grep/I!d' demo.txt            # keep only lines that match "grep" (ignore case)
```

### 5) Insert / Append / Change
```bash
sed '5i\\>>>INSERTING FIFTH LINE' demo.txt  # insert before line 5
sed '5,10i\\>>>A LINE' demo.txt             # insert before each line 5..10
sed '3c\\ Georges Bou Ghantous' demo.txt    # change (replace) line 3
sed '3,5c\\ Georges Bou Ghantous' demo.txt  # change lines 3..5
sed '3,$c\\ Georges Bou Ghantous' demo.txt  # change lines 3..end
```

### 6) Transform (y)
```bash
sed 'y/#*/@%/' demo.txt              # translate "#"→"@", "*"→"%"
sed 'y/#*\\\\/@%!/' demo.txt         # translate "#","*","\\" → "@","%","!"
```

### 7) Hold space tricks (advanced)
```bash
sed -n '1h;1!H;${;g;p;}' demo.txt    # accumulate entire file in hold space, then print once
sed -n 'h;g;p' demo.txt              # copy pattern->hold, then hold->pattern, then print
sed -n 'x;p' demo.txt                # swap hold and pattern, then print
```

### 8) In-place editing
```bash
sed -i.bak 's/unix/linux/g' demo.txt # edit file in place; save backup as demo.txt.bak
sed -i 's/\\s\\+$//' demo.txt        # strip trailing spaces in-place (GNU sed)
```
