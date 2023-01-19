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

###  LRU Cache

Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache. Implement the LRUCache class: LRUCache(int capacity) Initialize
the LRU cache with positive size capacity. int get(int key) Return the value
of the key if the key exists, otherwise return -1. void put(int key, int
value) Update the value of the key if the key exists. Otherwise, add the key-
value pair to the cache. If the number of keys exceeds the capacity from this
operation, evict the least recently used key. The functions get and put must
each run in O(1) average time complexity.

###  My Solution

```c++
#include <iostream>
#include <unordered_map>


class LRUCache {
    struct Node {
        int key;
        int value;
        Node *prev;
        Node *next;
        Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) {}
    };
    int capacity;
    Node *head;
    Node *tail;
    std::unordered_map<int, Node*> cache;

public:
    LRUCache(int cap) : head(nullptr), tail(nullptr) {
        capacity = cap;
    }

    
    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1;
        }
        Node *node = cache[key];
        moveToHead(node);
        return node->value;
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            Node *node = cache[key];
            node->value = value;
            moveToHead(node);
            return;
        }
        Node *node = new Node(key, value);
        if (cache.size() == capacity) {
            cache.erase(tail->key);
            if (tail == head) {
                head = tail = nullptr;
            } else {
                tail = tail->prev;
                tail->next = nullptr;
            }
        }
        if (!head) {
            head = tail = node;
        } else {
            node->next = head;
            head->prev = node;
            head = node;
        }
        cache[key] = node;
    }

private:
    void moveToHead(Node *node) {
    if (head == node) {
        return;
    } else if (tail == node) {
        tail = tail->prev;
        tail->next = nullptr;
    } else {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }
    node->next = head;
    node->prev = nullptr;
    head->prev = node;
    head = node;
    }
};
```

##  My Statistics

![](https://github.com/Vivallo04/stats/blob/master/generated/overview.svg)
![](https://github.com/Vivallo04/stats/blob/master/generated/languages.svg)

