#include "graph.h"

Graph::Graph(GraphType type) {
    this->type = type;
}

Graph::Graph(GraphType type, std::vector<std::pair<int,std::pair<int, int>>> data) {
    this->type = type;
    for(auto node:data) {
        addNode(node);
    }
}

Graph* Graph::addNode(std::pair<int,std::pair<int, int>> node) {
    int u = node.first;
    int v = node.second.first;
    int w = node.second.second;

}