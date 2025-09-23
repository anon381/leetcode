Complexity
Time complexity : O(max(∣v1∣,∣v2∣))
Space complexity : O(1)
class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        V1=v1.split('.')
        V2=v2.split('.')
        n1, n2=len(V1), len(V2)
        for x1, x2 in zip(V1, V2):
            if int(x1)<int(x2): return -1
            if int(x1)>int(x2): return 1
        n3=min(n1, n2)
        if n1<n2: 
            return -1 if any(int(V2[i])>0 for i in range(n3, n2)) else 0
        elif n1>n2:
            return 1 if any(int(V1[i])>0 for i in range(n3, n1)) else 0
        return 0



#in cpp
class Solution {
public:
    static int compareVersion(string& v1, string& v2) {
        const int n1=v1.size(), n2=v2.size();
        int x1=0, x2=0;
        for(int i=0, j=0; i<n1 || j<n2; i++, j++){
            while(i<n1 && v1[i]!='.'){
                x1=10*x1+(v1[i++]-'0');
            }
            while(j<n2 && v2[j]!='.'){
                x2=10*x2+(v2[j++]-'0');
            }
            if (x1<x2) return -1;
            else if (x1>x2) return 1;
            x1=0;
            x2=0;
        }
        return 0;
    }
};
