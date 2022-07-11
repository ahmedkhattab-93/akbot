import numpy as np

start_buy_pct = 0
end_buy_pct = -1.5
buy_levels = 3

stop_loss_pct = -1.75

total_fees = 0.35 * 2 * (buy_levels + 1)

step = (end_buy_pct - start_buy_pct) / buy_levels
pcts = []
for i, pct in enumerate(np.arange(start_buy_pct, end_buy_pct + step, step)):   
    size = (i + 1) / (buy_levels + 1) 
    pcts.append(pct)
    avg_buy_pct = np.mean(pcts)
    take_profit_pct = 0.5 + pct
    profit_return = size * (take_profit_pct - avg_buy_pct)
    print(i+1, round(size, 2), round(pct, 2), round(avg_buy_pct, 2), round(take_profit_pct, 2), round(profit_return, 2))

loss_return = stop_loss_pct - avg_buy_pct 
print(loss_return)

print("Total Fees:", total_fees)