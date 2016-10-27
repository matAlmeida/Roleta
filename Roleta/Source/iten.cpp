// g++ -Wall -c iten.cpp -o ../Binaries/iten.o 
#include <iostream>
#include "../Headers/iten.h"

Iten::Iten(int id, string name)
{
    this->id = id;
    this->name = name;
    this->times = 0;
    this->chance = 10;
}

Iten::Iten(int id, string name, int chance)
{
    this->id = id;
    this->name = name;
    this->times = 0;
    this->chance = chance;
}

string Iten::getName()
{
    return this->name;
}

int Iten::getId()
{
    return this->id;
}

int Iten::getTimes()
{
    return this->times;
}

int Iten::getChance()
{
    return this->chance;
}

bool Iten::setName(string name)
{
    this->name = name;
    return true;
}

bool Iten::setChance(int chance)
{
    this->chance = chance;
    return true;
}