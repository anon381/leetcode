class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        new = sentence.split()
        count = 1 
        
        for x in range(len(new)):
            if new[x][0].casefold() in 'aeiou': 
                new[x] = new[x] + 'ma' + 'a'*count
                count += 1
            elif new[x].casefold() not in 'aeiou': 
                new[x] = new[x][1:] + new[x][0] + 'ma' + 'a'*count 
                count += 1
        
        return " ".join(x for x in new) 


#in java
# class Solution {
#     public String toGoatLatin(String sentence) {
#         String[] words = sentence.split(" ");
#         StringBuilder sb = new StringBuilder();

#         for (int i = 0; i < words.length; i++) {
#             String word = words[i];
#             char ch = word.charAt(0);

#             if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'A' || ch == 'E' || ch == 'I'
#                     || ch == 'O' || ch == 'U') {
#                 sb.append(word);
#             } else {
#                 sb.append(word.substring(1)).append(ch);
#             }
#             sb.append("ma").append("a".repeat(i + 1)).append(" ");
#         }

#         sb.setLength(sb.length() - 1);

#         return sb.toString();
#     }
# }










# class Solution {
# public:
#     string toGoatLatin(string sentence) {
#         vector<string>v;
#         string s;
#         sentence+=' ';
#         for(auto u:sentence){
#             if(u==' '){
#                 v.push_back(s);
#                 s.clear();
#                 continue;
#             }
#             s+=u;
#         }
#         int j=1;
#         string s2;
#         for(auto u:v){
#             string s1=u;
#             if(s1[0]=='a'||s1[0]=='e'||s1[0]=='i'||s1[0]=='o'||s1[0]=='u'||s1[0]=='A'||s1[0]=='E'||s1[0]=='I'||s1[0]=='O'||s1[0]=='U'){
#                 s2+=s1;
#                 s2+="ma";
#             }
#             else{
#                 char ch=s1[0];
#                 reverse(s1.begin(),s1.end());
#                 s1.pop_back();
#                 reverse(s1.begin(),s1.end());
#                 s1+=ch;
#                 s2+=s1;
#                 s2+="ma";
                
#             }
#             for(int i=1;i<=j;i++){
#                 s2+='a';
#             }
#             s2+=' ';
#             j++;

#         }
#         s2.pop_back();
#         return s2;
#     }
# };
