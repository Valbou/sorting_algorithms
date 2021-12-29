
#ifndef ALGOS_HPP
#define ALGOS_HPP

#include <vector>
#include <string>

using namespace std;

class Algo
{
    public:
        virtual void process(vector<int> &) = 0;
        virtual string showInfos() = 0;
};

class Bubble: public Algo
{
    // Perf: O(n²) - O(n)
    // Mem: O(n)

    private:
        int invert = 0;

    public:
        void process(vector<int> &);
        string showInfos();
};

class Counting: public Algo
{
    // Perf: O(n+k) - O(n+k) where k is the count_list size
    // Mem: O(n+k)

    private:
        size_t count_list_size;
        int moves;

        vector<int> initList(vector<int>, int);

    public:
        void process(vector<int> &);
        string showInfos();
};

class Insertion: public Algo
{
    // Perf: O(n²) - O(n)
    // Mem: O(n)

    private:
        int invert = 0;

    public:
        void process(vector<int> &);
        string showInfos();
};

class Selection: public Algo
{
    // Perf: O(n²) - O(n)
    // Mem: O(n)

    private:
        int invert = 0;
        int comp = 0;

    public:
        void process(vector<int> &);
        string showInfos();
};

class AlgoFabric
{
    public:
        vector<string> getChoices();
        Algo *getInstance(string);
};

#endif // ALGOS_HPP
