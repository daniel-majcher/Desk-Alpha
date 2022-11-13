#include "multistrat.hpp"
#include <chrono>

NPMultistrat::NPMultistrat(unordered_map<string, unordered_map<string, int> > data) {
    this->time = 0;
    this->ticks = 0;
    this->orders = vector<unordered_map<string, string> >();
    for(auto & [ticker, price] : data) {
        this->data[ticker] = price;
        this->setTrend(ticker, "Up");
    }
}

void NPMultistrat::clear_orders() {
    this->orders = vector<unordered_map<string, string> >();
}

void NPMultistrat::update(unordered_map <string, unordered_map <string, int> > newData) {
    this->ticks++;
    this->clear_orders();
    for(auto & [ticker, price] : newData) {
        int prevPrice = this->getPrice(ticker);

        this->setPrice(ticker, newData[ticker]["price"]);

        int newPrice = newData[ticker]["price"];

        if (newPrice>=prevPrice && this->getTrend(ticker)=="Down") {
            this->setTrend(ticker, "Up");
            unordered_map<string, string> new_order = unordered_map<string, string>();
            new_order[ticker] = "BUY";
            this->orders.push_back(new_order);
        } else if (newPrice<prevPrice && this->getTrend(ticker)=="Up") {
            this->setTrend(ticker, "Down");
            unordered_map<string, string> new_order = unordered_map<string, string>();
            new_order[ticker] = "SELL";
            this->orders.push_back(new_order);
        }
    }
}

int main() {return 0;}