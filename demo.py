# -*- coding:utf-8 -*-

from trie import Trie


def demo_list():
  words = ["北京", "故宫", "北京故宫", "中国", "紫禁城"]
  tree = Trie().create_trie_from_list(words)
  text = "北京故宫是中国明清两代的皇家宫殿，旧称紫禁城。"
  matchs = tree.parse_text(text)
  print(matchs)


def demo_dict():
  words = {"北京": "GPE", "故宫": "LOC", "北京故宫": "LOC", "紫禁城": "LOC"}
  tree = Trie().create_trie_from_dict(words)
  text = "北京故宫是中国明清两代的皇家宫殿，旧称紫禁城。"
  matchs = tree.parse_text(text)
  print(matchs)


if __name__ == '__main__':
  demo_list()

  demo_dict()
