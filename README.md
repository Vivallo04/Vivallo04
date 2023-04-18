#  Hey! 🙋🏻‍♂️Vivallo here!

##  I am a Computer Engineering Student

###  Here are some of my interests and what I'm currently working on:

  * 🎆 Working on [ Lambda Blog ](https://github.com/Vivallo04/lambda-blog)
  * 🌱 I'm currently learning Rust and Game Development 
  * 💭 Ask me about anything [ here ](https://github.com/Vivallo04/Vivallo04/issues/new) or we can connect on [ LinkedIn ](https://bit.ly/3zm1YjA)
  * 🎮 I have fun developing games and doing full-stack web development 
  * 🤓 Oh! I almost forget. Here's a link to my [ dotfiles ](https://github.com/Vivallo04/dotfiles) (I use Arch btw) 
  * 👨🏻‍💻 Want to do any fun project for the weekend? Sure! I'm [ down ](https://discordapp.com/users/521712126058823701)
  * 💘 I love high-level and low-level programming as much as electronics (and classical music too) 

##  LeetCode Challenge of the Day ⚛

###  Subsets II

Given an integer array nums that may contain duplicates, return all possible
subsets (the power set). The solution set must not contain duplicate subsets.
Return the solution in any order.

###  My Solution
```c++ subsets.cpp

class Solution {
public:
    void generateSubsets(vector<int>& nums, int index, vector<int>& current, vector<vector<int>>& result) {
        if (index == nums.size()) {
            result.push_back(current);
            return;
        }
        
        // skip duplicates
        int i = index + 1;
        while (i < nums.size() && nums[i] == nums[index]) i++;
        
        generateSubsets(nums, i, current, result);
        
        for (int j = index; j < i; j++) {
            current.push_back(nums[j]);
            generateSubsets(nums, i, current, result);
        }
        
        for (int j = index; j < i; j++) {
            current.pop_back();
        }
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        sort(nums.begin(), nums.end());
        generateSubsets(nums, 0, current, result);
        return result;
    }
};

```
_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

