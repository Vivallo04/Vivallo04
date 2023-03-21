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

###  Jump Game

You are given an integer array nums. You are initially positioned at the
array's first index, and each element in the array represents your maximum
jump length at that position. Return true if you can reach the last index, or
false otherwise.

###  My Solution
```c solution.c
#include <stdbool.h>

bool canJump(int* nums, int numsSize){
    int farthest_index = 0;
    for(int i = 0; i < numsSize; i++) {
        if(i > farthest_index) {
            return false;
        }
        farthest_index = (farthest_index > i + nums[i]) ? farthest_index : i + nums[i];
        if(farthest_index >= numsSize - 1) {
            return true;
        }
    }
    return false;
}
```


_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

