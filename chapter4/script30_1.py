def parse_line(line):
    """
    mecabでパースされた一行を読み込みます。

    >>> parse_line('吾輩\\t名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ')
    {'surface': '吾輩', 'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞'}

    >>> parse_line('生れ\\t動詞,自立,*,*,一段,連用形,生れる,ウマレ,ウマレ')
    {'surface': '生れ', 'base': '生れる', 'pos': '動詞', 'pos1': '自立'}
    """
    (surface, attr) = line.split('\t')
    arr = attr.split(',')
    return {
        'surface': surface,
        'base': arr[6],
        'pos': arr[0],
        'pos1': arr[1]
    }


def read_mecab_file(filename):
    """
    指定されたファイルからすべての行を読み取って、
    一文ごとに１つのリストにして列挙します。
    各文の要素は parse_line の返り値のフォーマットです。

    # 3文目を取り出して、surfaceだけを連結する。
    >>> ''.join([i['surface'] for i in list(read_mecab_file('neko.txt.mecab'))[3]])
    '名前はまだ無い。'
    """
    sentence = []

    with open(filename, mode='rt', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if line == 'EOS':
                yield sentence
                sentence = []
            else:
                sentence.append(parse_line(line))
