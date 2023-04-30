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

###  Path Sum

Given the root of a binary tree and an integer targetSum, return true if the
tree has a root-to-leaf path such that adding up all the values along the path
equals targetSum.

###  My Solution
```java
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return false;
        }

        return hasPathSumHelper(root, targetSum, 0);
    }

    private boolean hasPathSumHelper(TreeNode node, int targetSum, int currentSum) {
        currentSum += node.val;

        if (node.left == null && node.right == null) {
            return currentSum == targetSum;
        }

        boolean leftPathExists = node.left != null && hasPathSumHelper(node.left, targetSum, currentSum);
        boolean rightPathExists = node.right != null && hasPathSumHelper(node.right, targetSum, currentSum);

        return leftPathExists || rightPathExists;
    }
}
```
  

_Note: Leet Code challenges update once a week😉_

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

