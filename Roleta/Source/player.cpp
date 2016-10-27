#include <iostream>
#include "../Headers/player.h"

Player::Player(int id, string name)
{
    this->id = id;
    this->name = name;
}

Player::Player(int id, string name, int shotsNumbers)
{
    this->id = id;
    this->name = name;
    this->shotsNumbers = shotsNumbers;
}

string Player::getName()
{
    return this->name;
}

int Player::getId()
{
    return this->id;
}

int Player::getShotsNumbers()
{
    return this->shotsNumbers;
}

bool Player::setName(string name)
{
    this->name  = name;
    return true;
}

// Terminar implementar Lista com ids dos shots
bool Player::addShot(int shotId)
{
    this->shotsNumbers += 1;
    return true;
}