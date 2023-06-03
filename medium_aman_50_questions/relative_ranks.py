# In the relative ranks problem, you will be given an array of integers representing the scores of athletes,
# and we need to assign ranks in descending order. The highest score will get the rank of “Gold Medal”,
# the second-highest score will get the rank of “Silver Medal”, the third-highest will get “Bronze Medal”,
# and the remaining scores will be ranked in descending order. For example, look at the input
# and output values of this problem shown below:

# Input: [5, 4, 3, 2, 1] | Output: [“Gold Medal”, “Silver Medal”, “Bronze Medal”, “4”, “5”]

# use dictionaries
def relative_ranks(scores):

    scores.sort(reverse=True)
    rank = []
    for i in range(len(scores)):
        rank.append(i+1)

    rank[0] = 'Gold medal'
    rank[1] = 'Silver medal'
    rank[2] = 'Bronze medal'
    return rank


scores = [7, 5, 8, 2, 3]
print(relative_ranks(scores))
