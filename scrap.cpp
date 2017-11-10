#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <vector>
#include <fstream>
#include <sstream>
// #include <tuple>
// #include <utility>

using namespace std;

double inf = std::numeric_limits<double>::infinity();

int main(int argc, char const *argv[])
{
	int V; string line;
	fstream readme;
	readme.open("test.txt");
	readme >> line;
	V = stoi(line);
	cout << "Number of vertices: " <<  V << endl;
	for (int i = 0; i < 2*V; i = i + 2)
	{	
		double c[2];
		for (int j = 0; j < 2; ++j)
		{
			readme >> line;
			c[j] = stod(line);
		}
		cout << c[0] << " " << c[1] << endl;
	}

	return 0;
}
