from collections import defaultdict
import heapq


class Twitter:
    def __init__(self):
        self.timestamp: int = 0
        self.following: dict[int, set[int]] = defaultdict(set)
        self.tweets: dict[int, list[tuple[int, int]]] = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # For each followee and the user oneself, heap store the most recent tweet if available
        heap = []
        for followee in self.following[userId] | {userId}:
            tweets = self.tweets[followee]
            if tweets:
                timestamp, tweetId = tweets[-1]
                # Record the index of the tweet in its original list
                heap.append((-timestamp, followee, tweetId, len(tweets) - 1))
        heapq.heapify(heap)
        # k-way merge to get the top 10 most recent tweets
        res = []
        k = 0
        while k < 10 and heap:
            _, ownerId, tweetId, ind = heapq.heappop(heap)
            res.append(tweetId)
            # Add the next most recent tweet to the heap if available
            ind -= 1
            if ind >= 0:
                timestamp, tweetId = self.tweets[ownerId][ind]
                heapq.heappush(heap, (-timestamp, ownerId, tweetId, ind))
            k += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
