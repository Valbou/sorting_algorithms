
#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <algorithm>
#include <chrono>

#include "app.hpp"
#include "../algos/algos.hpp"

using namespace std;


Benchmark::Benchmark() {
    this->start = 0;
    this->end = 0;
}

int64_t Benchmark::time(){
    return std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::system_clock::now().time_since_epoch()).count();
}

void Benchmark::go() {
    this->start = this->time();
}

void Benchmark::stop() {
    this->end = this->time();
}

string Benchmark::toString() {
    return string("Ran in " + to_string((this->end - this->start) / 1000000.0) + " seconds");
}


ConfigApp::ConfigApp () {
    this->min = -100;
    this->max = 100;
    this->size = 50;
}

vector<int> ConfigApp::getRandomList () {
    if(this->list.size() == 0) {
        default_random_engine generator;
        uniform_int_distribution<int> distribution(this->min, this->max);
        this->list.clear();
        this->list.reserve(this->size);
        for(int i=0; i < this->size; ++i) {
            this->list.push_back(distribution(generator));
        }
    }
    return this->list;
}

void ConfigApp::manualConfig() {
    cout << "#### Configuration ####" << '\n';
    cout << "Min, max and size must be integers" << endl;
    getInt(string("Set the min of the list:"), this->min);
    getInt(string("Set the max of the list:"), this->max);
    getInt(string("Set the size of the list:"), this->size);

    cout << "Your config:" << '\n' << "Min: " << this->min << '\n' << "Max: " << this->max << '\n' << "Size: " << this->size << endl;
    this->list.clear();
    this->getRandomList();
}

void ConfigApp::getInt(string info, int &var) {
    cout << info << '\n';
    cin >> var;
}


App::App() {
    this->app_choices = {string("exit"), string("config")};
    this->config = new ConfigApp();
    this->fabric = new AlgoFabric();
    this->algos_choices = this->fabric->getChoices();

    cout << "#######################\n# Valbou - Sort Algos #\n#  Version 1.0 (C++)  #\n#######################\n" << endl;
}

App::~App() {
    delete this->config;
    delete this->fabric;
}

void App::exec() {
    while(this->menu()) {}
    cout << "########################" << endl;
}

bool App::menu() {
    cout << "Choose an algo to sort your list (by number or name) :" << '\n';
    vector<string> choices = this->getChoices();
    for(int i=0; i < choices.size(); ++i) {
        cout << " " << i << ": " << choices[i] << '\n';
    }

    string choice = this->getInputChoice();
    return this->treatChoice(choice);
}

vector<string> App::getChoices() {
    vector<string> choices;
    choices.insert(choices.end(),this->app_choices.begin(),this->app_choices.end());
    choices.insert(choices.end(),this->algos_choices.begin(),this->algos_choices.end());
    return choices;
}

string App::getInputChoice() {
    string choice;
    cout << "Your choice :" << endl;
    cin >> choice;

    vector<string> choices = this->getChoices();
    try {
        int result = stoi(choice);
        return choices[result];
    }
    catch (const invalid_argument& ia) {
        std::vector<string>::iterator it;
        it = find(choices.begin(), choices.end(), choice);
        if(it != choices.end()) {
            return choice;
        }
    }
    return string("");
}

bool App::treatChoice(string choice) {
    std::vector<string>::iterator it;
    it = find(this->app_choices.begin(), this->app_choices.end(), choice);
    if(it != this->app_choices.end()) {
        if(choice == string("exit")) {
            cout << "Exiting..." << '\n';
            return false;
        }
        else if(choice == string("config")) {
            this->config->manualConfig();
            return true;
        }
    }

    it = find(this->algos_choices.begin(), this->algos_choices.end(), choice);
    if(it != this->algos_choices.end()) {
        vector<int> list = this->config->getRandomList();
        Benchmark bench;
        auto *algo = this->fabric->getInstance(choice);

        cout << "List to sort:" << '\n';
        this->showList(list);
        cout << '\n';

        bench.go();
        algo->process(list);
        bench.stop();

        cout << "Sorted:" << '\n';
        this->showList(list);
        cout << '\n' << algo->showInfos() << '\n';
        cout << bench.toString() << endl;
        return true;
    }
    return false;
}

void App::showList(vector<int> list) {
    for(int i=0; i < list.size(); ++i) {
        cout << list[i] << ", ";
        if(i % 25 == 0) {
            cout << '\n';
        }
    }
}
