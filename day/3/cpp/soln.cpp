#include <iostream>
#include <string>
#include <math.h>

using namespace std;

typedef std::pair<int, int> Point;

int manhattan_dist(const Point &a, const Point &b)
{
        return std::abs(a.first - b.first) +
               std::abs(a.second - b.second);
}


int square_size(int index) {
        return int(ceil(sqrt(index))) / 2 * 2 + 1;
}

int square_layer(int size) {
        return ceil(float(size) / 2.0);
}


Point adjust(int size, const Point &start, int start_index, int final_index) {
        size -= 1;
        auto distance = final_index - start_index;
        int x = start.first;
        int y = start.second;

        y += min(distance, size - 1);
        // first adjustment is offset by 1, as start isn't quite in the bottom right
        distance -= size - 1;
        distance = max(distance, 0);

        x -= min(distance, size);
        distance -= size;
        distance = max(distance, 0);

        y -= min(distance, size);
        distance -= size;
        distance = max(distance, 0);

        x += min(distance, size);

        return std::make_pair(x, y);

}

Point faster_coords(int index) {
        int size = square_size(index);
        int layer = square_layer(size);
        int square_start = pow(size-2, 2) + 1;
        const Point ss_coords = std::make_pair(size-layer,  layer-size+1);
        const Point final = adjust(size, ss_coords, square_start, index);
        return final;
}


int main(int argc, char* argv[])
{
        const Point origin = std::make_pair(0,0);

        const Point testcase = faster_coords(1024);
        cout << testcase.first << ":" << testcase.second << endl;
        cout << "Manhattan distance " << manhattan_dist(origin, testcase) << endl;

        const Point testcase2 = faster_coords(312051);
        cout << testcase2.first << ":" << testcase2.second << endl;
        cout << "Manhattan distance " << manhattan_dist(origin, testcase2) << endl;
        return 0;
}
