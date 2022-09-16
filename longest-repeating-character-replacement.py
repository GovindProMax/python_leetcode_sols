class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq_count = {}
        max_length = 0

        # start 2 pointers
        l = 0
        for r in range(len(s)):
            char_freq_count[s[r]] = (
                char_freq_count.get(s[r], 0) + 1
            )  # add freq count to the hash table

            # set the window and check if the most frequent char is greater than k
            # the window is (r-l+1) and the most frequent char is max(char_freq_count.values())
            while (r - l + 1) - max(char_freq_count.values()) > k:
                char_freq_count[s[l]] -= 1
                l += 1 #

            max_length = max(max_length, (r - l + 1))
        return max_length