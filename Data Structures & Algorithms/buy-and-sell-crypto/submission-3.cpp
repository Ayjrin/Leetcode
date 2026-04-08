class Solution {
public:
    int max_profit = 0;
    int maxProfit(vector<int>& prices) {
        for(int i =0; i < size(prices) - 1; i++){
            for(int j = i+1; j < size(prices); j++){
                if (max_profit < prices[j] - prices[i]){
                    max_profit = prices[j] - prices[i];
                }
            }
        }
        return max_profit;
    }
};
