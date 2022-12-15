class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        songs = collections.defaultdict(int)

        count = 0

        for song in time:
            if song % 60 == 0:
                count += songs[0]
            else:
                count += songs[60 - song%60]

            songs[song % 60] += 1

        return count
