# AhoCorasickAutomaton

Python version Aho-Corasic Automaton.

## 1. Usage

Please refer to [`main.py`](https://github.com/liu-nlper/AhoCorasickAutomation/edit/master/main.py).

### 1.1 Create tree from list

```python
words = ["北京", "故宫", "北京故宫", "中国", "紫禁城"]
tree = Trie().create_trie_from_list(words)
text = "北京故宫是中国明清两代的皇家宫殿，旧称紫禁城。"
matchs = tree.parse_text(text)
print(matchs
```
↓

    >>> [0:2=北京, 0:4=北京故宫, 2:4=故宫, 5:7=中国, 19:22=紫禁城]

### 1.2 Create tree from dict

```python
words = {"北京": "GPE", "故宫": "LOC", "北京故宫": "LOC", "紫禁城": "LOC"}
tree = Trie().create_trie_from_dict(words)
text = "北京故宫是中国明清两代的皇家宫殿，旧称紫禁城。"
matchs = tree.parse_text(text)
print(matchs)
```
↓

    >>> [0:2=北京/GPE, 0:4=北京故宫/LOC, 2:4=故宫/LOC, 19:22=紫禁城/LOC]

## 2. References

  - [FoolNLTK](https://github.com/rockyzhengwu/FoolNLTK)
