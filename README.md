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

###  Gray Code

An n-bit gray code sequence is a sequence of 2n integers where: Every integer
is in the inclusive range [0, 2n - 1], The first integer is 0, An integer
appears no more than once in the sequence, The binary representation of every
pair of adjacent integers differs by exactly one bit, and The binary
representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.

###  My Solution
```c#
public class GrayCodeGenerator
{
    public List<int> GenerateGrayCode(int n)
    {
        List<int> result = new List<int> { 0 };
        HashSet<int> visited = new HashSet<int> { 0 };
        Backtrack(0, n, visited, result);
        return result;
    }

    private bool Backtrack(int curr, int n, HashSet<int> visited, List<int> result)
    {
        if (result.Count == (1 << n))
            return true;

        for (int i = 0; i < n; i++)
        {
            int nextNum = curr ^ (1 << i);
            if (!visited.Contains(nextNum))
            {
                visited.Add(nextNum);
                result.Add(nextNum);
                if (Backtrack(nextNum, n, visited, result))
                    return true;
                result.RemoveAt(result.Count - 1);
                visited.Remove(nextNum);
            }
        }

        return false;
    }
}

public class Program
{
    public static void Main()
    {
        int n = 3;
        GrayCodeGenerator generator = new GrayCodeGenerator();
        List<int> sequence = generator.GenerateGrayCode(n);
        Console.WriteLine(string.Join(", ", sequence));
    }
}

```
_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

