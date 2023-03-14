/*
PROBLEM: https://www.codingninjas.com/codestudio/problems/implement-trie_1387095
DIFFICULTY: MEDIUM

Implement a data structure ”TRIE” from scratch with following methods:

1) Trie(): Initialize the object of this “TRIE” data structure.

2) insert(“WORD”): Insert the string “WORD” into this “TRIE” data structure.

3) countWordsEqualTo(“WORD”): Return how many times this “WORD” is present in this “TRIE”.

4) countWordsStartingWith(“PREFIX”): Return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.

5) erase(“WORD”): Delete one occurrence of the string “WORD” from the “TRIE”.
*/

#include<iostream>
#include<string>

using namespace std;

struct TrieNode {
    TrieNode* next[26] = { nullptr };
    int count = 0;
};

class Trie{

    public:
    TrieNode* root = new TrieNode();

    void insert(string &word){
        TrieNode* curr = root;
        for(auto c:word) {
            if(curr->next[c-'a'] == nullptr) {
                curr->next[c-'a'] = new TrieNode();
            }
            curr = curr->next[c-'a'];
        }
        curr->count++;
    }

    int countWordsEqualTo(string &word){
        TrieNode* curr = root;
        for(auto c:word) {
            if(curr->next[c-'a'] == nullptr) {
                return 0;
            }
            curr = curr->next[c-'a'];
        }
        return curr->count;
    }

    int countWordsStartingWith(string &word){
        TrieNode* curr = root;
        int cnt = 0;
        for(auto c:word) {
            if(curr->next[c-'a'] == nullptr) {
                return 0;
            }
            curr = curr->next[c-'a'];
        }
        cnt += curr->count;
        for(int i=0; i<26; i++) {
            if(curr->next[i] == nullptr)
                continue;
            string temp(1, i+'a');
            string t = word+temp;
            cnt += countWordsStartingWith(t);
        }
        
        return cnt;
    }

    void erase(string &word){
        TrieNode* curr = root;
        for(auto c:word) {
            if(curr->next[c-'a'] == nullptr) {
                return;
            }
            curr = curr->next[c-'a'];
        }
        if(curr->count >=1){
            curr->count--;
        }
    }
};
