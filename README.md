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

###  Search Insert Position

Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order. You must write an algorithm with O(log n) runtime
complexity.

###  My Solution
```c#
using System;

class Program
{
    static void Main()
    {
        int[] nums = { 1, 3, 5, 6 };
        int target = 5;
        int result = SearchInsert(nums, target);
        Console.WriteLine(result);
    }

    static int SearchInsert(int[] nums, int target)
    {
        int low = 0;
        int high = nums.Length - 1;

        while (low <= high)
        {
            int mid = (low + high) / 2;
            int midVal = nums[mid];

            if (midVal == target)
            {
                return mid;
            }
            else if (midVal < target)
            {
                low = mid + 1;
            }
            else
            {
                high = mid - 1;
            }
        }

        // If the loop completes without finding the target, 'low' will be the correct insertion position
        return low;
    }
}
```


_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

