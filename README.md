# Ergodic Experiment

Based on [this video](https://www.youtube.com/watch?v=f1vXAHGIpfc&t=360s&ab_channel=GreshamCollege).

Run this experiment with this command: 

`python main.py`

Try adjusting the `BET_PERCENT` to .25 to see the median amount won increase. 

## Conclusion
By having more "small bets" in the system, you increase your chances of winning the game.

## Example Output
Here's an example output when every ensemble does the max bet (100%). In other words, only 1 bet.

```
Number OF ENSEMBLES: 1000
Number OF Coin Flips: 1000
Total Money in System: $2,620,888.98
Max Final Balance: $9,228.53
Average Final Balance: $2,620.89
Median Final Balance: $0.00
Number of Ensembles with less than $100: 506
Number of Ensembles with more than $100: 494
```

And here is the result when everyone does 4 "small bets" of 25% of the max bet.

```
Number OF ENSEMBLES: 1000
Number OF Coin Flips: 1000
Total Money in System: $5,042,366.28
Max Final Balance: $22,283.97
Average Final Balance: $5,042.37
Median Final Balance: $4,861.62
Number of Ensembles with less than $100: 332
Number of Ensembles with more than $100: 668
```

Notice the median amount of money won has gone from $0 to $4k and the chance of "winning" (making more than you started with) went from 50% to ~67%.

