
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [0, 0]
        for student in students:
            counts[student] += 1

        remaining = len(sandwiches)
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            if remaining == 0:
                break
            counts[sandwich] -= 1
            remaining -= 1
        
        return remaining
        
#in cpp
#include <vector>
using namespace std;

class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        vector<int> counts(2, 0);
        for (int student : students)
            counts[student]++;

        int remaining = sandwiches.size();
        for (int sandwich : sandwiches) {
            if (counts[sandwich] == 0)
                break;
            if (remaining == 0)
                break;
            counts[sandwich]--;
            remaining--;
        }

        return remaining;
    }
};

#in java
class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int[] counts = new int[2];
        for (int student : students) counts[student]++;
        
        int remaining = sandwiches.length;
        for (int sandwich : sandwiches) {
            if (counts[sandwich] == 0) break;
            if (remaining-- == 0) break;
            counts[sandwich]--;
        }
        
        return remaining;
    }
}
