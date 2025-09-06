# Complexity
# Time complexity:
# O(n)

# Space complexity:
# O(18)

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        expSum4=[1]+[0]*17
        def expSum(x):
            if x==0: return 0
            log4=(x.bit_length()-1)>>1
            r=x-(1<<(log4<<1))
            return expSum4[log4]+r*(log4+1)
        for i in range(1,18):
            expSum4[i]=expSum4[i-1]+3*i*(1<<(2*(i-1)))+1
        op=0
        for l1, r in queries:
            op+=(expSum(r)-expSum(l1-1)+1)>>1

        return op


# in cpp
# class Solution {
# public:
#     long long expSum4[18]={1};
#     long long expSum(unsigned x){
#         if (x==0) return 0;
#         int log4=(31-countl_zero(x))/2;
#         int r=x-(1<<(2*log4));
#         return expSum4[log4]+r*(log4+1LL);
#     }
#     long long minOperations(vector<vector<int>>& queries) {
#         for(int i=1; i<18; i++){
#             expSum4[i]=expSum4[i-1]+3LL*i*(1LL<<(2*(i-1)))+1;
#         //    cout<<i<<"->"<<expSum4[i]<<", ";
#         }
#         long long op=0;
#         for(auto& q: queries){
#             int l=q[0]-1, r=q[1];
#             op+=(expSum(r)-expSum(l)+1)/2;// ceiling of (expSum(r)-expSum(l))/2
#         }
#         return op;
#     }
# };



# in java
# class Solution {
#     static long expSum4[]=new long[18];
#     static long expSum(int x){
#         if (x==0) return 0;
#         int log4=(31-Integer.numberOfLeadingZeros(x))>>1;
#         int r=x-(1<<(log4<<1));
#         return expSum4[log4]+r*(log4+1L);
#     }
#     static public long minOperations(int[][] queries) {
#         expSum4[0]=1;
#         for(int i=1; i<18; i++)
#             expSum4[i]=expSum4[i-1]+3L*i*(1L<<(2*(i-1)))+1;
#         long op=0;
#         for(int[] q : queries){
#             int l=q[0]-1, r=q[1];
#             op+=(expSum(r)-expSum(l)+1)>>1;// ceiling of (expSum(r)-expSum(l))/2
#         }
#         return op;
#     }
# }
