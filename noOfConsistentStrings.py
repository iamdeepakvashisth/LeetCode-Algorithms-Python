def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowedSet = set(allowed)
        for i in words:
            if set(i).issubset(allowedSet):
                count += 1
        return count