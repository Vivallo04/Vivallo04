#  Hey! 🙋🏻‍♂️Vivallo here!

##  I am a Computer Engineering Student

###  Here are some of my interests and what I'm working on:

  * 🎆 Working on [ Lambda Blog ](https://github.com/Vivallo04/lambda-blog)
  * 🌱 I'm currently learning Rust and Game Development 
  * 💭 Ask me about anything [ here ](https://github.com/Vivallo04/Vivallo04/issues/new) or we can connect on [ LinkedIn ](https://bit.ly/3zm1YjA)
  * 🎮 I have fun developing games and doing full-stack web development 
  * 🤓 Oh! I almost forget. Here's a link to my [ dotfiles ](https://github.com/Vivallo04/dotfiles) (I use Arch btw) 
  * 👨🏻‍💻 Want to do any fun project for the weekend? Sure! I'm [ down ](https://discordapp.com/users/521712126058823701)
  * 💘 I love high-level and low-level programming as much as electronics (and classical music too) 

##  LeetCode Challenge of the Day ⚛

###  Search Insert Position

Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order. You must write an algorithm with O(log n) runtime
complexity.

###  My Solution
```c#
public class Solution {
    public int SearchInsert(int[] nums, int target) {
        for (int i = 0; i < nums.Length; i++)
        {
            if (target == nums[i] || nums[i] > target)
            {
                return i;
            }
        }
        return nums.Length;
    }
}
````

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

