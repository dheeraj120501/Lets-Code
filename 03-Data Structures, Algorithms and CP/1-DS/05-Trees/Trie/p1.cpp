/*
PROBLEM: https://www.codingninjas.com/codestudio/problems/implement-trie_631356
DIFFICULTY: HARD

Implement Trie Data Structure to support these operations:
insert(word) - To insert a string "word" in Trie
search(word) - To check if string "word" is present in Trie or not.
startsWith(word) - To check if there is any string in the Trie that starts with the given prefix string "word".
*/

#include<iostream>
#include<string>

using namespace std;

struct TrieNode {
    bool isEnd = false;
    TrieNode* next[26] = { nullptr };
};

class Trie {

public:
    TrieNode* root = new TrieNode();

    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* curr = root;
        for(auto c:word) {
            if(curr->next[c-'a'] == nullptr) {
                curr->next[c-'a'] = new TrieNode();
            }
            curr = curr->next[c-'a'];
        }
        curr->isEnd = true;
    }

    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* curr = root;
        for(auto c:word) {
            if(curr->next[c-'a'] == nullptr) {
                return false;
            }
            curr = curr->next[c-'a'];
        }
        return curr->isEnd;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode* curr = root;
        for(auto c:prefix) {
            if(curr->next[c-'a'] == nullptr) {
                return false;
            }
            curr = curr->next[c-'a'];
        }
        return true;
    }
};