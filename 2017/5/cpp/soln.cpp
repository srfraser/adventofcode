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


int part1(vector<int>& data) {
        int steps = 0;
        int current_index = 0;

        int max_index = data.size();

        int prev_index;

        while (0 <= current_index && current_index < max_index) {
                prev_index = current_index;
                current_index += data[current_index];
                data[prev_index] += 1;
                steps++;
        }

        return steps;
}


int part2(vector<int>& data) {
    int steps = 0;
    int current_index = 0;

    int max_index = data.size();

    int prev_index;

    while (0 <= current_index && current_index < max_index) {
            prev_index = current_index;
            current_index += data[current_index];
            if (data[prev_index] >= 3) {
                data[prev_index] -= 1;
            } else {
                data[prev_index] += 1;
            }
            steps++;
    }
    return steps;
}


int main(int argc, char* argv[])
{
        ifstream f (argv[1]);
        if (!f.is_open())
                perror("error while opening file");

        string line;
        vector<int> data;
        while(getline(f, line)) {
                std::string::size_type sz;
                data.push_back(stoi(line, &sz));
        }
        for (auto const& c : data)
                cout << c << ' ';
        cout << endl;

        vector<int> part2_data = data;

        if (f.bad())
                perror("error while reading file");

        cout << "Part 1 steps: " << part1(data) << endl;
        cout << "Part 2 steps: " << part2(part2_data) << endl;

        return 0;
}
