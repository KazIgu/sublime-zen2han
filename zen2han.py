import sublime, sublime_plugin
import sys
sys.path.append('/Users/iguchikazuya/Library/Application Support/Sublime Text 3/Packages/zen2han')
import zenhan
class Zen2hanCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
        select_texts = self.view.substr(region)

        if select_texts != "":
            zen2han_text = zenhan.hz(select_texts)
            han2zen_text = zenhan.zh(select_texts)
            if select_texts != zen2han_text:
                self.view.replace(edit, region, zen2han_text)
            elif select_texts != han2zen_text:
                self.view.replace(edit, region, han2zen_text)

class Kana2kanaCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
        select_texts = self.view.substr(region)

        if select_texts != "":
            zen2han_text = zenhan.jz(select_texts)
            han2zen_text = zenhan.zj(select_texts)
            if select_texts != zen2han_text:
                self.view.replace(edit, region, zen2han_text)
            elif select_texts != han2zen_text:
                self.view.replace(edit, region, han2zen_text)


class Han2zenCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
        select_texts = self.view.substr(region)

        if select_texts != "":
            han2zen_text = zenhan.hz(select_texts)
            if select_texts != han2zen_text:
                self.view.replace(edit, region, han2zen_text)

