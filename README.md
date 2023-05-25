#  Hey! 🙋🏻‍♂️Vivallo here!

##  I am a Computer Engineering Student

###  Here are some of my interests and what I'm currently working on:

  * 🎆 Working on [ Lambda Blog ](https://lambdablog.com)
  * 🌱 I'm currently learning Go and Game Development 
  * 💭 Ask me about anything [ here ](https://github.com/Vivallo04/Vivallo04/issues/new) or we can connect on [ LinkedIn ](https://bit.ly/3zm1YjA)
  * 🎮 I have fun developing games and doing full-stack web development 
  * 🤓 Oh! I almost forget. Here's a link to my [ dotfiles ](https://github.com/Vivallo04/dotfiles) (I use Arch btw) 
  * 💘 I love high-level and low-level programming as much as electronics (and classical music too) 

##  LeetCode Challenge of the Day ⚛

###  Most Popular Video Creator

You are given two string arrays creators and ids, and an integer array views,
all of length n. The ith video on a platform was created by creator[i], has an
id of ids[i], and has views[i] views. The popularity of a creator is the sum
of the number of views on all of the creator's videos. Find the creator with
the highest popularity and the id of their most viewed video. If multiple
creators have the highest popularity, find all of them. If multiple videos
have the highest view count for a creator, find the lexicographically smallest
id. Return a 2D array of strings answer where answer[i] = [creator, id] means
that creator has the highest popularity and idi is the id of their most
popular video. The answer can be returned in any order.

###  My Solution
```c++
#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

struct Creator {
    string name;
    string id;
    int views;

    Creator(string _name, string _id, int _views) : name(_name), id(_id), views(_views) {}

    bool operator<(const Creator& other) const {
        if (views != other.views)
            return views > other.views;
        return id < other.id;
    }
};

vector<vector<string>> findPopularCreators(vector<string>& creators, vector<string>& ids, vector<int>& views) {
    int n = creators.size();
    unordered_map<string, Creator> creatorMap;
    vector<Creator> popularCreators;

    for (int i = 0; i < n; i++) {
        if (creatorMap.find(creators[i]) == creatorMap.end()) {
            Creator creator(creators[i], ids[i], views[i]);
            creatorMap[creators[i]] = creator;
            popularCreators.push_back(creator);
        } else {
            creatorMap[creators[i]].views += views[i];
            if (creatorMap[creators[i]].id > ids[i])
                creatorMap[creators[i]].id = ids[i];
        }
    }

    sort(popularCreators.begin(), popularCreators.end());

    int maxPopularity = popularCreators[0].views;
    vector<vector<string>> answer;

    for (const Creator& creator : popularCreators) {
        if (creator.views == maxPopularity) {
            answer.push_back({ creator.name, creator.id });
        } else {
            break;
        }
    }

    return answer;
}

int main() {
    vector<string> creators = { "John", "Jane", "John", "Jane", "Mark" };
    vector<string> ids = { "abc123", "def456", "ghi789", "jkl012", "mno345" };
    vector<int> views = { 1000, 500, 1500, 2000, 500 };

    vector<vector<string>> result = findPopularCreators(creators, ids, views);

    cout << "Popular Creators:" << endl;
    for (const auto& pair : result) {
        cout << pair[0] << ", " << pair[1] << endl;
    }

    return 0;
}
```

_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

