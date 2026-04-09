class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int longest = 0;

        for (int i = 0; i < s.length(); i++){
            longest = 0;
            std::vector<char> contains = {};
            contains.push_back(s[i]);
            longest++;
            for (int j = i+1; j <s.length(); j++){
                if (std::find(contains.begin(), contains.end(), s[j]) != s[j]){
                    contains.push_back(s[j]);
                    longest++;
                } else {break;}
            }
        }
        return longest;

    }
};
