import sublime, sublime_plugin

ZEN2HAN = (
    ("ァ", "ｧ"), ("ィ", "ｨ"), ("ゥ", "ｩ"), ("ェ", "ｪ"), ("ォ", "ｫ"),
    ("ッ", "ｯ"), ("ャ", "ｬ"), ("ュ", "ｭ"), ("ョ", "ｮ"),
    ("ガ", "ｶﾞ"), ("ギ", "ｷﾞ"), ("グ", "ｸﾞ"), ("ゲ", "ｹﾞ"), ("ゴ", "ｺﾞ"),
    ("ザ", "ｻﾞ"), ("ジ", "ｼﾞ"), ("ズ", "ｽﾞ"), ("ゼ", "ｾﾞ"), ("ゾ", "ｿﾞ"),
    ("ダ", "ﾀﾞ"), ("ヂ", "ﾁﾞ"), ("ヅ", "ﾂﾞ"), ("デ", "ﾃﾞ"), ("ド", "ﾄﾞ"),
    ("バ", "ﾊﾞ"), ("ビ", "ﾋﾞ"), ("ブ", "ﾌﾞ"), ("ベ", "ﾍﾞ"), ("ボ", "ﾎﾞ"),
    ("パ", "ﾊﾟ"), ("ピ", "ﾋﾟ"), ("プ", "ﾌﾟ"), ("ペ", "ﾍﾟ"), ("ポ", "ﾎﾟ"),
    ("ヴ", "ｳﾞ"),
    ("ア", "ｱ"), ("イ", "ｲ"), ("ウ", "ｳ"), ("エ", "ｴ"), ("オ", "ｵ"),
    ("カ", "ｶ"), ("キ", "ｷ"), ("ク", "ｸ"), ("ケ", "ｹ"), ("コ", "ｺ"),
    ("サ", "ｻ"), ("シ", "ｼ"), ("ス", "ｽ"), ("セ", "ｾ"), ("ソ", "ｿ"),
    ("タ", "ﾀ"), ("チ", "ﾁ"), ("ツ", "ﾂ"), ("テ", "ﾃ"), ("ト", "ﾄ"),
    ("ナ", "ﾅ"), ("ニ", "ﾆ"), ("ヌ", "ﾇ"), ("ネ", "ﾈ"), ("ノ", "ﾉ"),
    ("ハ", "ﾊ"), ("ヒ", "ﾋ"), ("フ", "ﾌ"), ("ヘ", "ﾍ"), ("ホ", "ﾎ"),
    ("マ", "ﾏ"), ("ミ", "ﾐ"), ("ム", "ﾑ"), ("メ", "ﾒ"), ("モ", "ﾓ"),
    ("ヤ", "ﾔ"), ("ユ", "ﾕ"), ("ヨ", "ﾖ"),
    ("ラ", "ﾗ"), ("リ", "ﾘ"), ("ル", "ﾙ"), ("レ", "ﾚ"), ("ロ", "ﾛ"),
    ("ワ", "ﾜ"), ("ヲ", "ｦ"), ("ン", "ﾝ"),

    ("。", "｡"), ("、", "､"), ("ー", "ｰ")
)

HAN2ZEN = lambda: ((h, z) for z, h in ZEN2HAN)

def convert(text, *maps):
    def replace(text, fr, to):
        return text.replace(fr, to)

    for m in maps:
        if callable(m):
            m = m()
        elif isinstance(m, dict):
            m = m.items()
        for fr, to in m:
            text = replace(text, fr, to)

    return text

class Zen2hanCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
        select_texts = self.view.substr(region)

        if select_texts != "":
            zen2han_text = convert(select_texts, ZEN2HAN)
            if select_texts != zen2han_text:
                self.view.replace(edit, region, zen2han_text)


class Han2zenCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
        select_texts = self.view.substr(region)

        if select_texts != "":
            han2zen_text = convert(select_texts, HAN2ZEN)
            if select_texts != han2zen_text:
                self.view.replace(edit, region, han2zen_text)

