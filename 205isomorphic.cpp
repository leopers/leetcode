#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  bool isIsomorphic(string s, string t) {
    unordered_map<char, char> map;
    unordered_set<char> set;

    int n = s.size(), m = t.size();

    if (n != m)
      return false;

    for (int i = 0; i < n; ++i) {
      if (map.find(s[i]) == map.end() && set.find(t[i]) == set.end()) {
        map[s[i]] = t[i];
        set.insert(t[i]);
      }

      else {
        if (map[s[i]] == t[i])
          continue;

        return false;
      }
    }

    return true;
  }
};