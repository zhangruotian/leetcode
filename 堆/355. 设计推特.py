from collections import defaultdict
class Twitter:
    def __init__(self):
        self.relationship = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time,tweetId))
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = self.posts[userId][:]
        
        for follow_id in self.relationship[userId]:
            max_heap.extend(self.posts[follow_id][:])
        heapq.heapify(max_heap)
        for _ in range(10):
            if max_heap:
                res.append(heapq.heappop(max_heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.relationship[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.relationship[followerId]:
            self.relationship[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
