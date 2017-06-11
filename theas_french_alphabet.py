import string
fr_alphabet = list(string.ascii_lowercase)
chrs = [['\u00E0','\u00E1','\u00E4'],
    ['\u00E7'],
    ['\u00E8','\u00E9','\u00EA'],
    ['\u00EE', '\u00EF'],
    ['\u00F4', '\u0153'],
    ['\u00F9', '\u00FC'],
    ['\u00FF']]
fr = ['a', 'à', 'á', 'ä', 'b', 'c', 'ç', 'd', 'e', 'è', 'é', 'ê', 'f', 'g', 'h', 'î', 'ï', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ô', 'œ', 'p', 'q', 'r', 's', 't', 'u', 'ù', 'ü', 'v', 'w', 'x', 'y', 'ÿ', 'z']
poss = [1,6,9,15,24,32,38]

for x in range(0,7):
    pos = poss[x]
    car = chrs[x]
    while len(car) != 0:
        carr = car.pop(len(car)-1)
        fr_alphabet.insert(pos, carr)


while len(fr) != 0:
    s = fr.pop(0)
    ss = fr_alphabet.pop(0)
    if s != ss:
        print((s) + '  ' +(ss))

