using namespace std;

class Player
{
    private:
        int id;
        string name;
        int shotsNumbers;
    public:
        Player(int id, string name);
        Player(int id, string name, int shotsNumbers);

        // Gets
        string getName();
        int getId();
        int getShotsNumbers();
        // Sets
        bool setName(string name);
        bool addShot(int shotId);
};