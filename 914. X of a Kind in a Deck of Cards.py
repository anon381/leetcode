class Solution:
        def hasGroupsSizeX(self, deck):
            def gcd(a, b):
                while b: a, b = b, a % b
                return a
            count = collections.Counter(deck).values()
            return reduce(gcd, count) > 1




#in cpp
    # bool hasGroupsSizeX(vector<int>& deck) {
    #     unordered_map<int, int> count;
    #     int res = 0;
    #     for (int i : deck) count[i]++;
    #     for (auto i : count) res = __gcd(i.second, res);
    #     return res > 1;
    # }




# in java 
    # public boolean hasGroupsSizeX(int[] deck) {
    #     Map<Integer, Integer> count = new HashMap<>();
    #     int res = 0;
    #     for (int i : deck) count.put(i, count.getOrDefault(i, 0) + 1);
    #     for (int i : count.values()) res = gcd(i, res);
    #     return res > 1;
    # }

    # public int gcd(int a, int b) {
    #     return b > 0 ? gcd(b, a % b) : a;
    # }
