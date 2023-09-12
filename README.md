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

###  Sum of All Subset XOR Totals

The XOR total of an array is defined as the bitwise XOR of all its elements,
or 0 if the array is empty. Given an array nums, return the sum of all XOR
totals for every subset of nums. An array a is a subset of an array b if a can
be obtained from b by deleting some (possibly zero) elements of b.

###  My Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

// Function to calculate XOR of all elements in a vector
int calculateXOR(const vector<int>& subset) {
    int result = 0;
    for (int num : subset) {
        result ^= num;
    }
    return result;
}

// Function to recursively generate all subsets and calculate XOR totals
void generateSubsets(const vector<int>& nums, int index, vector<int>& currentSubset, int& totalXOR) {
    if (index == nums.size()) {
        // Base case: we have reached the end of the array
        // Add the XOR of the current subset to the total
        totalXOR += calculateXOR(currentSubset);
        return;
    }

    // Include the current element in the subset
    currentSubset.push_back(nums[index]);
    generateSubsets(nums, index + 1, currentSubset, totalXOR);

    // Exclude the current element from the subset
    currentSubset.pop_back();
    generateSubsets(nums, index + 1, currentSubset, totalXOR);
}

int subsetXORSum(const vector<int>& nums) {
    int totalXOR = 0;
    vector<int> currentSubset;
    generateSubsets(nums, 0, currentSubset, totalXOR);
    return totalXOR;
}

int main() {
    vector<int> nums = {1, 3};
    int result = subsetXORSum(nums);

    cout << "The sum of XOR totals for all subsets is: " << result << endl;

    return 0;
}
```

_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

