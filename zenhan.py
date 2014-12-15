import re, functools

C_OFF = 0x80

S_ZNUM = '、。「」　ー０１２３４５６７８９'
S_HNUM = '､｡｢｣ -0123456789'

S_HIR = 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん' \
        'っぁぃぅぇぉゃゅょ' \
        'がぎぐげござじずぜぞだぢづでどばびぶべぼゔ' \
        'ぱぴぷぺぽ' \

S_ZEN = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン' \
        'ッァィゥェォャュョ'  \
        'ガギグゲゴザジズゼゾダヂヅデドバビブベボヴ' \
        'パピプペポ'

S_SEI = 'ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝ' \
        'ｯｧｨｩｪｫｬｭｮ'

S_DAK = 'ｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾊﾋﾌﾍﾎｳ'
S_HAT = 'ﾊﾋﾌﾍﾎ'
TENN, MARU = 'ﾞ', 'ﾟ'

L_DAK = [c+TENN for c in S_DAK] + [c+MARU for c in S_HAT]
S_CCH = ''.join(chr(i+C_OFF) for i in range(len(L_DAK)))
S_HAN = S_SEI + S_CCH
L_HAN = list(S_SEI) + L_DAK
H_DAK = dict(zip(L_DAK, S_CCH))
R_DAK = re.compile('[{}]{}|[{}]{}'.format(S_DAK, TENN, S_HAT, MARU))

def comb(*fs):
    return lambda x: functools.reduce(lambda y,f:f(y), fs, x)

def trans(k,v):
    assert len(k)==len(v)
    tbl = str.maketrans(k,v) if type(v) is str else \
          str.maketrans(dict(zip(k,v)))
    return lambda s: s.translate(tbl)

def replace(c0, c1): return lambda s: s.replace(c0,c1)
subd = lambda s: R_DAK.sub(lambda m:H_DAK[m.group()], s)

zj=comb(trans(S_ZEN, S_HIR))
jz=comb(trans(S_HIR, S_ZEN))
zh=trans(S_ZEN, L_HAN)
jh=comb(trans(S_HIR, L_HAN))
hz=comb(subd, trans(S_HAN, S_ZEN))
hj=comb(subd, trans(S_HAN, S_HIR))
nzh=trans(S_ZNUM, S_HNUM)
nhz=trans(S_HNUM, S_ZNUM)

if __name__=='__main__':
    test('zen>han>zen', comb(zh, hz), S_ZEN)
    test('zen>hira>zen', comb(zj, jz), S_ZEN)

    test('hira>zen>hira', comb(jz, zj), s_hir)
    test('hira>han>hira', comb(jh, hj), s_hir)

    s_han=''.join(L_HAN)
    test('han>hira>han', comb(hj, jh), s_han)
    test('han>zen>han', comb(hz, zh), s_han)