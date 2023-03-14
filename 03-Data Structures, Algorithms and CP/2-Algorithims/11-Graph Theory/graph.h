#pragma once
#include <vector>

enum GraphType {
    Directed,
    Undirected
};

class Graph {
    private:
    GraphType type;
    public:
    std::vector<std::vector<std::pair<int,int>>> g;
    Graph(GraphType type);
    Graph(GraphType type, std::vector<std::pair<int,std::pair<int, int>>> data);

    Graph* addNode(std::pair<int,std::pair<int, int>>);
};