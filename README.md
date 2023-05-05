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

###  Jump Game II

You are given a 0-indexed array of integers nums of length n. You are
initially positioned at nums[0]. Each element nums[i] represents the maximum
length of a forward jump from index i. In other words, if you are at nums[i],
you can jump to any nums[i + j] where: 0 <= j <= nums[i] and i + j < n Return
the minimum number of jumps to reach nums[n - 1]. The test cases are generated
such that you can reach nums[n - 1].

###  My Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

int jump_game(vector<int>& nums)
{
    int n = nums.size();
    unordered_map<int, int> dist;
    for (int i = 0; i < n; i++) 
    {
        dist[i] = INT_MAX;
    }
    dist[0] = 0;
    queue<int> q;
    q.push(0);
    while (!q.empty()) 
    {
        int i = q.front();
        q.pop();
        for (int j = 1; j <= nums[i] && i+j < n; j++) 
        {
            int k = i+j;
            if (dist[i]+1 < dist[k]) 
            {
                dist[k] = dist[i]+1;
                q.push(k);
            }
        }
    }
    return dist[n-1];
}
```

_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

