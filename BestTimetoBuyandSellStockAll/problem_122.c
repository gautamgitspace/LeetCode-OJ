int maxProfit(int* prices, int pricesSize){

    int max_total_profit = 0;
    
    for ( int i = 0; i < pricesSize-1; i++) {
        if (prices[i+1] > prices[i]) {
            max_total_profit += prices[i+1] - prices[i];
        }
    }
    return max_total_profit;
}
