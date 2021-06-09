def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph_a = re.sub("[!?',;.]+", ' ', paragraph)
        list_of_words = paragraph_a.lower().split(' ')
        word_cnt = {}
        for word in list_of_words:
            if word not in banned and word not in [ ' ', '']:
                word_cnt[word] = word_cnt.get(word,0) +1
        max_key = max(word_cnt, key=word_cnt.get) 
        return max_key