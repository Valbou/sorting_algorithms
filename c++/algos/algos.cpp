#include <vector>
#include <string>
#include <algorithm>
#include <stdexcept>

#include "algos.hpp"

using namespace std;


void Bubble::process(vector<int> &list) {
    size_t size = list.size();
    size_t fixed = 0;
    bool swap = true;

    while (swap) {
        swap = false;
        for(size_t i=1; i < (size - fixed); ++i) {
            if(list[i] < list[i-1]) {
                int temp = list[i];
                list[i] = list[i-1];
                list[i-1] = temp;
                ++this->invert;
                swap = true;
            }
        }
        ++fixed;
    }
}

string Bubble::showInfos() {
    return "Sorted in " + to_string(this->invert) + " inverts";
}


void Counting::process(vector<int> &list) {
    int min = *min_element(list.begin(), list.end());
    vector<int> countList = this->initList(list, min);

    for(int i=0; i < list.size(); ++i) {
        ++countList[list[i] - min];
    }

    int index = 0;
    for(int i=0; i < countList.size(); ++i) {
        for(int j=0; j < countList[i]; ++j) {
            list[index] = i + min;
            ++this->moves;
            ++index;
        }
    }
}

vector<int> Counting::initList(vector<int> list, int min) {
    int max = *max_element(list.begin(), list.end());
    this->count_list_size = max - min + 1;
    vector<int> countList;
    countList.resize(this->count_list_size, 0);
    return countList;
}

string Counting::showInfos() {
    return "Sorted in " + to_string(this->moves) + " moves + " + to_string(this->count_list_size);
}


void Insertion::process(vector<int> &list) {
    int j;
    for(int i=0; i < list.size(); ++i) {
        j = i;
        while (j > 0 && list[j-1] > list[j]) {
            int temp = list[j-1];
            list[j-1] = list[j];
            list[j] = temp;
            ++this->invert;
            --j;
        }
    }
}

string Insertion::showInfos() {
    return "Sorted in " + to_string(this->invert) + " inverts";
}


void Selection::process(vector<int> &list) {
    size_t size = list.size();
    int min, index;
    for(int i=0; i < size; ++i) {
        min = list[i];
        index = i;
        for(int j=i; j < size; ++j) {
            if(list[j] <= min) {
                min = list[j];
                index = j;
                ++this->comp;
            }
        }
        if(index != i) {
            int temp = list[index];
            list[index] = list[i];
            list[i] = temp;
            ++this->invert;
        }
    }
}

string Selection::showInfos() {
    return "Sorted in " + to_string(this->invert) + " inverts and " + to_string(this->comp) + " comparisons";
}


vector<string> AlgoFabric::getChoices() {
    vector<string> list = {
        string("Bubble"),
        string("Counting"),
        string("Insertion"),
        string("Selection")
    };
    return list;
}

Algo *AlgoFabric::getInstance(string choice) {
    if(choice == string("Bubble"))
        return new Bubble();
    else if(choice == string("Counting"))
        return new Counting();
    else if(choice == string("Insertion"))
        return new Insertion();
    else if(choice == string("Selection"))
        return new Selection();
    throw invalid_argument(choice + " is not a valid choice.");
}
