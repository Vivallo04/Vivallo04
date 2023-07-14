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

###  Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle in
the histogram.

###  My Solution
```c#
public class Solution
{
    public int LargestRectangleArea(int[] heights)
    {
        return CalculateLargestArea(heights, 0, heights.Length - 1);
    }
    
    private int CalculateLargestArea(int[] heights, int start, int end)
    {
        if (start > end)
        {
            return 0;
        }
        
        int minIndex = FindMinHeightIndex(heights, start, end);
        int areaWithMin = heights[minIndex] * (end - start + 1);
        int leftArea = CalculateLargestArea(heights, start, minIndex - 1);
        int rightArea = CalculateLargestArea(heights, minIndex + 1, end);
        
        return Math.Max(areaWithMin, Math.Max(leftArea, rightArea));
    }
    
    private int FindMinHeightIndex(int[] heights, int start, int end)
    {
        int minIndex = start;
        
        for (int i = start; i <= end; i++)
        {
            if (heights[i] < heights[minIndex])
            {
                minIndex = i;
            }
        }
        
        return minIndex;
    }
}
```

_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

