# Complexity
# Time complexity: O(N)
# Space complexity: O(1)

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        current_indx = [0,0]
        alphabet_hashMap = {}
        letters = [
                    ['a', 'b', 'c', 'd', 'e'],
                    ['f', 'g', 'h', 'i', 'j'],
                    ['k', 'l', 'm', 'n', 'o'],
                    ['p', 'q', 'r', 's', 't'],
                    ['u', 'v', 'w', 'x', 'y'],
                    ['z', '', '', '', '']
                ]
        for i in range(len(letters)):
            for j in range(len(letters[0])):
                if letters[i][j] != '':
                    alphabet_hashMap[letters[i][j]] = [i, j]
        path = ""
        for i in target:
            x , y =  alphabet_hashMap[i]

            if current_indx[0] == x and current_indx[1] == y:
                path += "!"
                continue

            if current_indx[1] > y:
                direction = "L"*(current_indx[1] - y)
                path += direction

            if x > current_indx[0]:
                direction = "D"*(x - current_indx[0])
                path += direction

            if current_indx[0] > x:
                direction = "U"*(current_indx[0] - x)
                path += direction

            if y > current_indx[1]:
                direction = "R"*(y - current_indx[1])
                path += direction

            current_indx[0] = x
            current_indx[1] = y
            path += "!"
            
        return path




#in cpp
class Solution {
public:

    string alphabetBoardPath(string s) {
        map<char,pair<int,int>> m;
        char ch = 'a';
        for(int i =0;i<6;i++){
            for(int j =0;j<5;j++){
                m[ch]={i,j};
                if(ch=='z'){break;}
                ch=char(ch+1);
            }
        }
        int p =0,q=0;string ans;
        while(s.size()>0){
            char ch = s[0];int a=p-m[ch].first,b=q-m[ch].second;
            if(ch=='z'){
            for(int i =0;i<abs(b);i++)
            {if(b>0){ans.push_back('L');}else{ans.push_back('R');}}
            for(int i =0;i<abs(a);i++)
            {if(a>0){ans.push_back('U');}else{ans.push_back('D');}}
            }
            else{
            for(int i =0;i<abs(a);i++)
            {if(a>0){ans.push_back('U');}else{ans.push_back('D');}}
            for(int i =0;i<abs(b);i++)
            {if(b>0){ans.push_back('L');}else{ans.push_back('R');}}
            }ans.push_back('!');
            s=s.substr(1,s.size()-1);
            p=m[ch].first;q=m[ch].second;
        }
        return ans;
    }
};
