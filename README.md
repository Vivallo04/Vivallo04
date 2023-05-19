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

###  Restore IP Addresses

A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but
"0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP
addresses that can be formed by inserting dots into s. You are not allowed to
reorder or remove any digits in s. You may return the valid IP addresses in
any order.

###  My Solution
```c#
class Program
{
    static List<string> RestoreIpAddresses(string s)
    {
        List<string> result = new List<string>();
        Backtrack(s, 0, 0, "", result);
        return result;
    }

    static void Backtrack(string s, int start, int segments, string current, List<string> result)
    {
        // Base case: if all segments are formed and no characters left in s
        if (segments == 4 && start == s.Length)
        {
            result.Add(current);
            return;
        }

        // Base case: if all segments are formed but there are characters left in s
        if (segments == 4 || start == s.Length)
        {
            return;
        }

        // Try different segment lengths from 1 to 3
        for (int i = 1; i <= 3; i++)
        {
            // Check if the remaining characters are enough for the current segment length
            if (start + i > s.Length)
            {
                break;
            }

            string segment = s.Substring(start, i);

            // Skip segments with leading zeros
            if (segment[0] == '0' && segment.Length > 1)
            {
                continue;
            }

            // Check if the segment is a valid number (between 0 and 255)
            if (!int.TryParse(segment, out int num) || num < 0 || num > 255)
            {
                continue;
            }

            // Append the current segment to the current IP address and move to the next segment
            string next = current + segment + (segments < 3 ? "." : "");
            Backtrack(s, start + i, segments + 1, next, result);
        }
    }

    static void Main(string[] args)
    {
        string s = "25525511135";
        List<string> result = RestoreIpAddresses(s);

        foreach (string ip in result)
        {
            Console.WriteLine(ip);
        }
    }
}
```

_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

