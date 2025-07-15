class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        for i, ticket in enumerate(tickets):
            if i <= k:
                # If we are at or before the k-th person, we can buy tickets directly
                time += min(ticket, tickets[k])
            else:
                # If we are after the k-th person, we can only buy tickets if they are less than the k-th person's ticket
                time += min(ticket, tickets[k] - 1)

        return time
