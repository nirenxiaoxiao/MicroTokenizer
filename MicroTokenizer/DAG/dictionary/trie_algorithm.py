from MicroTokenizer.DAG.dictionary.dictionary import DictionaryData


class TreeNode(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.is_leaf = False
        self.weight = None

    def set_as_leaf(self, weight):
        self.is_leaf = True
        self.weight = weight


class TrieAlgorithm(DictionaryData):
    def __init__(self, dict_data=None):
        super().__init__(dict_data)

        self.tree_root = TreeNode()
        self.build_trie_tree()

    def build_trie_tree(self):
        for token, weight in self.dict_data.items():
            current_node = self.tree_root
            for i in token:
                if i not in current_node:
                    current_node[i] = TreeNode()

                current_node = current_node[i]

            current_node.set_as_leaf(weight)

    def get_token_and_weight_at_text_head(self, text):
        current_node = self.tree_root
        for index, char in enumerate(text):
            if char in current_node:
                char_node = current_node[char]

                if char_node.is_leaf:
                    yield text[:index+1], char_node.weight

                current_node = char_node

            else:
                break

    def add_token_and_weight(self, token, weight):
        current_node = self.tree_root
        for i in token:
            if i not in current_node:
                current_node[i] = TreeNode()

            current_node = current_node[i]

        current_node.set_as_leaf(weight)


if __name__ == "__main__":
    from timer_cm import Timer

    dictionary_object = TrieAlgorithm()

    with Timer('Building DAG graph'):
        for _ in range(10000):
            result = list(
                dictionary_object.get_token_and_weight_at_text_head("王小明在北京的清华大学读书。")
            )

    print(result)
