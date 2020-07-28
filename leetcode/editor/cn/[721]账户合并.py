# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其
# 余元素是 emails 表示该帐户的邮箱地址。 
# 
#  现在，我们想合并这些帐户。如果两个帐户都有一些共同的邮件地址，则两个帐户必定属于同一个人。请注意，即使两个帐户具有相同的名称，它们也可能属于不同的人，因为
# 人们可能具有相同的名称。一个人最初可以拥有任意数量的帐户，但其所有帐户都具有相同的名称。 
# 
#  合并帐户后，按以下格式返回帐户：每个帐户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。accounts 本身可以以任意顺序返回。 
# 
#  例子 1: 
# 
#  
# Input: 
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnn
# ybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Ma
# ry", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.
# com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation: 
#   第一个和第三个 John 是同一个人，因为他们有共同的电子邮件 "johnsmith@mail.com"。 
#   第二个 John 和 Mary 是不同的人，因为他们的电子邮件地址没有被其他帐户使用。
#   我们可以以任何顺序返回这些列表，例如答案[['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com'
# ]，
#   ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']]仍然会被
# 接受。
# 
#  
# 
#  注意： 
# 
#  
#  accounts的长度将在[1，1000]的范围内。 
#  accounts[i]的长度将在[1，10]的范围内。 
#  accounts[i][j]的长度将在[1，30]的范围内。 
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 98 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        if len(accounts) <= 1:
            return accounts
        f = list(range(len(accounts)))

        def find_parent(x):
            if f[x] == x:
                return x
            else:
                f[x] = find_parent(f[x])
                return f[x]

        def union(x, y):
            f[find_parent(y)] = find_parent(x)

        for i in range(len(accounts)):
            for j in range(i + 1, len(accounts)):
                if accounts[i][0] == accounts[j][0]:
                    accounts_i = accounts[i][1:]
                    accounts_j = accounts[j][1:]
                    for email in accounts_i:
                        if email in accounts_j:
                            union(i, j)
                            break

        for i in range(len(accounts)):
            if find_parent(i) != i:
                for j in range(1, len(accounts[i])):
                    if accounts[i][j] not in accounts[f[i]][1:]:
                        accounts[f[i]].append(accounts[i][j])
                accounts[i] = []

        i = len(accounts) - 1
        while i >= 0:
            if not accounts[i]:
                del accounts[i]
            i -= 1

        for i in range(len(accounts)):
            accounts[i][1:] = sorted(accounts[i][1:])

        for i in range(len(accounts)):
            for j in range(len(accounts[i]) - 1, -1, -1):
                if accounts[i][j] == accounts[i][j-1]:
                    del accounts[i][j]

        return accounts
# leetcode submit region end(Prohibit modification and deletion)