using namespace std;

class Iten
{
    private:
        int id; // Iten ID
        string name; // Name
        int times; // Who many times got selected
        int chance; // 1 - 10
    public:
        Iten(int id, string name);
        Iten(int id, string name, int chance);

        // Gets
        string getName();
        int getId();
        int getTimes();
        int getChance();
        // Sets
        bool setName(string name);
        bool setChance(int chance);
};