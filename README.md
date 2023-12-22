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
```java
public class PascalTriangle {

    public static List<List<Integer>> generate(int numRows) {
        return IntStream.range(0, numRows)
                .mapToObj(rowIndex -> IntStream.range(0, rowIndex + 1)
                        .mapToObj(colIndex -> binomialCoefficient(rowIndex, colIndex))
                        .collect(Collectors.toList()))
                .collect(Collectors.toList());
    }

    private static int binomialCoefficient(int n, int k) {
        return k == 0 ? 1 : binomialCoefficient(n, k - 1) * (n - k + 1) / k;
    }

    public static void main(String[] args) {
        int numRows = 5;
        List<List<Integer>> result = generate(numRows);

        // Print the result
        result.forEach(System.out::println);
    }
}
```
_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

