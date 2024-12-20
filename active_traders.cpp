#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);



/*
 * Complete the 'mostActive' function below.
 *
 * The function is expected to return a STRING_ARRAY.
 * The function accepts STRING_ARRAY customers as parameter.
 */

vector<string> mostActive(vector<string> customers) {
    map<string, int> trades;
    vector<string> res;
    for(auto customer : customers) {
        trades[customer]++;
    }
    for(auto i = trades.begin(); i != trades.end(); ++i) {
        if((double)i->second/customers.size() >= 0.05) {
            res.push_back(i->first);
        }
    }
    return res;
}

int main()
