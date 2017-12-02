#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> line2vec(const string& s) {
        stringstream iss( s );
        int number;
        vector<int> myvec;
        while ( iss >> number )
                myvec.push_back( number );
        return myvec;
}

int find_checksum(const vector<int> data) {
        return *max_element(data.begin(), data.end()) - *min_element(data.begin(), data.end());
}

int find_quotient(const vector<int> data) {
        for (auto i = 0; i < data.size(); i++) {
                for (auto j = i+1; j < data.size(); j++) {
                        auto numerator = max(data[i], data[j]);
                        auto denominator = min(data[i], data[j]);
                        div_t result = div(numerator, denominator);
                        if ( result.rem == 0 ) {
                                return result.quot;
                        }
                }
        }
}


int main(int argc, char* argv[])
{
        ifstream f (argv[1]);
        if (!f.is_open())
                perror("error while opening file");

        int total = 0;
        int checksum = 0;
        string line;
        while(getline(f, line)) {
                vector<int> data = line2vec(line);
                for (auto const& c : data)
                        cout << c << ' ';
                cout << endl;
                checksum += find_checksum(data);
                total += find_quotient(data);
        }
        if (f.bad())
                perror("error while reading file");

        cout << "Checksum is " << checksum << endl;
        cout << "Quotient total is " << total << endl;
        return 0;
}
