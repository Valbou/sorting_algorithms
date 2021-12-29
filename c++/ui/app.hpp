
#ifndef APP_HPP
#define APP_HPP

#include <iostream>
#include <vector>
#include <string>

#include "../algos/algos.hpp"

using namespace std;

class Benchmark
{
    private:
        int64_t start;
        int64_t end;

    public:
        Benchmark();
        int64_t time();
        void go();
        void stop();
        string toString();
};

class ConfigApp 
{
    private:
        int min;
        int max;
        int size;
        vector<int> list;

    public:
        ConfigApp();
        vector<int> getRandomList();
        void manualConfig();
        void getInt(string, int &);
};

class App
{
    private:
        vector<string> app_choices;
        vector<string> algos_choices;
        ConfigApp *config;
        AlgoFabric *fabric;

    public:
        App();
        void exec();
        bool menu();
        vector<string> getChoices();
        string getInputChoice();
        bool treatChoice(string);
        void showList(vector<int>);
        ~App();
};

#endif // APP_HPP
