class Solution {
public:
    string prune(string &str) {
        string result = "";
        int i, n = str.length(), count = 0;
        for (i=n-1; i>=0; i--){
            char c = str[i];
                if (c == '#'){
                    count++;
                } else {
                    if (count > 0){
                        count--;
                    } else {
                        result += c;
                    }
                }
        }
        return result;
    }
public:
    bool backspaceCompare(string S, string T) {
        return prune(S) == prune(T);
    }
};
