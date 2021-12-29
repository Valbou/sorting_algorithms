// Compile with: g++ main.cpp ui/app.cpp algos/algos.cpp -o sortalgo

#include "ui/app.hpp"

using namespace std;

int main(int argc, char *argv[])
{
    App ui;
    ui.exec();
    return 0;
}
