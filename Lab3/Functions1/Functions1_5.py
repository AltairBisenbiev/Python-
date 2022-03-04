permts = []
def prmute(sr, i, ln):
    if i == ln:
        permts.append(''.join(sr) )
    else:
        for j in range(i, ln):
            sr[i], sr[j] = sr[j], sr[i]
            prmute(sr, i + 1, ln)
            sr[i], sr[j] = sr[j], sr[i] 
word = input()

prmute(list(word), 0, len(word))

print(str(permts))