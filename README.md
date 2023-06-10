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

###  Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle. In
Pascal's triangle, each number is the sum of the two numbers directly above
it.

###  My Solution

```c#
public List<List<int>> GeneratePascalsTriangle(int numRows)
{
    List<List<int>> triangle = new List<List<int>>();

    for (int i = 0; i < numRows; i++)
    {
        List<int> row = new List<int>();
        for (int j = 0; j <= i; j++)
        {
            if (j == 0 || j == i)
            {
                row.Add(1);
            }
            else
            {
                int prevRowSize = triangle[i - 1].Count;
                int sum = triangle[i - 1][j - 1] + (j < prevRowSize ? triangle[i - 1][j] : 0);
                row.Add(sum);
            }
        }
        triangle.Add(row);
    }

    return triangle;
}
```

_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

