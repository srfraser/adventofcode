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

vector<string> line2vec(const string& s) {
        stringstream iss( s );

        vector<string> tokens{istream_iterator<string>{iss},
                              istream_iterator<string>{}};
        return tokens;
}

vector<string> line2vec_sort(const string& s) {
        stringstream iss( s );
        vector<string> tokens;
        do
        {
                string subs;
                iss >> subs;
                sort(subs.begin(), subs.end());

                cout << "Substring: " << subs << endl;
                tokens.push_back(subs);
        } while (iss);
        return tokens;
}



bool has_duplicates(const vector<string> s) {
        std::set<string> myset (s.begin(),s.end());
        if (myset.size() == s.size()) {
                return true;
        } else {
                return false;
        }
}


int main(int argc, char* argv[])
{
        ifstream f (argv[1]);
        if (!f.is_open())
                perror("error while opening file");

        int plain_total = 0;
        int dup_total = 0;

        string line;
        while(getline(f, line)) {
                vector<string> data = line2vec(line);
                vector<string> sorteddata = line2vec_sort(line);
                for (auto const& c : data)
                        cout << c << ' ';
                cout << endl;
                for (auto const& c : sorteddata)
                        cout << c << ' ';
                cout << endl;
                if (has_duplicates(data)) {
                        plain_total += 1;
                }
                if (has_duplicates(sorteddata)) {
                        dup_total += 1;
                }

        }
        if (f.bad())
                perror("error while reading file");

        cout << "Valid passwords (by duplicate) " << plain_total << endl;
        cout << "Valid passwords (by anagram) " << dup_total << endl;

        return 0;
}
