#include <iostream>
#include <unordered_map>
#include <string>
#include <ctime>
#include <vector>

using namespace std;
class NPMultistrat { //non performant multistrat
private:
    unordered_map <string, unordered_map<string, int> > data;
    time_t time;
    vector<unordered_map<string, string> > orders;
    size_t ticks;
    unordered_map <string, string> trends;
public:
    NPMultistrat(unordered_map<string, unordered_map<string, int> > data);

    unordered_map <string, unordered_map <string, int> > getData() {return this->data;}
    int getPrice(string stock) {return this->data[stock]["price"];}
    time_t getTime() {return this->time;}
    vector<unordered_map <string, string> > getOrders() {return this->orders;}
    size_t getTicks() {return this->ticks;}
    string getTrend(string stock) {return this->trends[stock];}

    void setData(unordered_map <string, unordered_map<string, int > > data) {this->data = data;}
    void setPrice(string stock, int price) {this->data[stock]["price"] = price;}
    void setTrend(string stock, string trend) {this->trends[stock] = trend;}

    void clear_orders();
    void update(unordered_map <string, unordered_map <string, int> > newData);
};