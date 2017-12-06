#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <string>
#include <iterator>
#include <set>
#include <algorithm>

using namespace std;


int most_blocks(vector<int>& data) {
        return max_element(data.begin(), data.end()) - data.begin();
}


void redistribute(vector<int>& data) {
        int index = most_blocks(data);
        int to_spend = data[index];
        data[index] = 0;

        while (to_spend > 0) {
                index += 1;
                index %= data.size();
                to_spend -= 1;
                data[index] += 1;
        }
}

vector<int> line2vec(const string& s) {
        stringstream iss( s );
        int number;
        vector<int> myvec;
        while ( iss >> number )
                myvec.push_back( number );
        return myvec;
}


int main(int argc, char* argv[])
{
        ifstream f (argv[1]);
        if (!f.is_open())
                perror("error while opening file");

        string line;

        getline(f, line);
        vector<int> data = line2vec(line);

        for (auto const& c : data)
                cout << c << ' ';
        cout << endl;

        if (f.bad())
                perror("error while reading file");

        cout << "Highest value is at " << most_blocks(data) << endl;

        vector<vector<int> > seen;

        while(find(seen.begin(), seen.end(), data) == seen.end()) {
                seen.push_back(data);
                redistribute(data);
        }
        cout << "Found duplicate after " << seen.size() << " cycles" << endl;
        auto index = distance(seen.begin(), find(seen.begin(), seen.end(), data));
        cout << "Distance between duplicates: " << (seen.size() - index) << endl;
        return 0;
}
