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
```python
class XORSubsetCalculator:
    @staticmethod
    def subset_xor_sum(nums: List[int]) -> int:

        if not nums:
            return 0
            
        n = len(nums)
        total_sum = 0
        for subset_mask in range(1, 1 << n):
            xor_total = 0
            
            # Process each bit position
            for i in range(n):
                if subset_mask & (1 << i):
                    xor_total ^= nums[i]
            
            total_sum += xor_total
            
        return total_sum
```


_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

