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

using namespace std;

double inf = std::numeric_limits<double>::infinity();

int main(int argc, char const *argv[])
{
	// Initialization
	int V; string line;
	vector<pair<double, double> > C;
	C.push_back(make_pair<double, double> (0,0));
	
	// Read file
	ifstream readFile;
	readFile.open("test.txt");
	readFile >> line;
	V = stoi(line);
	
	// collect data
	for (int i = 0; i < 2*V; i = i + 2)
	{
		double c[2];
		for (int j = 0; j < 2; ++j)
		{
			readFile >> line;
			c[j] = stod(line);
		}

		C.push_back(make_pair<double, double>(c[0], c[1]) );

	}

	// solve TSP
	double A[V+1];
	A[1] = 0
	for (int s = 2; s < V+1; ++s)
	{
		double current[V+1];
		if (s > 2)
		{
			A[1] = inf
		}

		// Generate subset of size s, with 1 as one of the elements and work on each
		
	}
	return 0;	
}