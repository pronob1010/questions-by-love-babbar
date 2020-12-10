# User function Template for python3

class Solution:
    def middle(self, A, B, C):
        m = max(A, B, C)
        mi = min(A, B, C)

        if mi < A < m:
            r = A
        elif mi < B < m:
            r = B
        else:
            r = C
        return r

        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B, C = map(int, input().strip().split())
        ob = Solution()
        print(ob.middle(A, B, C))
# } Driver Code Ends