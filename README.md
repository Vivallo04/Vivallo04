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

###  Word Search

Given an m x n grid of characters board and a string word, return true if word
exists in the grid. The word can be constructed from letters of sequentially
adjacent cells, where adjacent cells are horizontally or vertically
neighboring. The same letter cell may not be used more than once.

###  My Solution
```c#
public class Solution 
{
    public bool Exist(char[][] board, string word) 
    {
        int m = board.Length;
        int n = board[0].Length;
        
        bool Backtrack(int row, int col, string currWord)
        {
            if (row < 0 || row >= m || col < 0 || col >= n || board[row][col] != currWord[0])
                return false;
            
            if (currWord.Length == 1)
                return true;
            
            char temp = board[row][col];
            board[row][col] = '#'; // Mark the current position as visited
            
            bool result = Backtrack(row + 1, col, currWord.Substring(1))
                          || Backtrack(row - 1, col, currWord.Substring(1))
                          || Backtrack(row, col + 1, currWord.Substring(1))
                          || Backtrack(row, col - 1, currWord.Substring(1));
            
            board[row][col] = temp; // Mark the current position as unvisited
            
            return result;
        }
        
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (Backtrack(i, j, word))
                    return true;
            }
        }
        
        return false;
    }
}
```
_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

