# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.129889  
> tokenB->tokenA (amountBIn=5, amountAOut=5.655322)  
tokenA->tokenD (amountAIn=5.655322, amountDOut=2.458781)  
tokenD->tokenC (amountDIn=2.458781, amountCOut=5.088927)  
tokenC->tokenB (amountCIn=2.458781, amountBOut=20.129889)

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Slippage in AMMs like Uniswap V2 is the difference between the expected price of a trade and the actual price you get when you make the trade. Uniswap V2 uses a formula called "x * y = k" to keep prices stable. This formula ensures that the product of token reserves stays the same despite trades happening. So, even if you make a big trade, the price won't change too much.
 
> Here's an illustration using a simple example:  
  Let's say we have a liquidity pool on Uniswap V2 with tokens A and B. The initial reserves are:
Token A: 100  
Token B: 200    
According to the "x * y = k" formula, the initial product is:
100 * 200 = 20,000

> Now, suppose someone wants to swap 10 tokens of A for tokens of B. Before the swap, they calculate the expected price based on the current reserves and the formula. However, due to the trade, the reserves will change, leading to slippage.
After the swap, let's say the new reserves become:

> Token A: 90  
Token B: 223.53   
(calculated using the "x * y = k" formula: 90 * 223.53 ≈ 20,000)

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> In the UniswapV2Pair contract, the mint function is responsible for minting liquidity tokens when liquidity is added to the pair. During the initial liquidity minting, a minimum liquidity is subtracted from the liquidity being added. The rationale behind this design is to prevent front-running and ensure that liquidity providers receive a fair amount of liquidity tokens relative to their contribution.  
> ![image](https://github.com/csie-zhou/Homework-2/assets/148289135/cdd0d413-4471-4fd5-9f65-e7fd35240993)


## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> The intention behind the specific formula used to obtain liquidity when depositing tokens in the UniswapV2Pair contract is to ensure that liquidity providers receive an appropriate amount of liquidity tokens relative to the tokens they contribute to the pool.  

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> A sandwich attack happens in decentralized finance when someone watches for a big trade about to happen, then quickly makes two trades before and after it. By doing this, they manipulate the price and make a profit at the trader's expense. So, when you're swapping assets, if someone pulls off a sandwich attack, you might end up getting a worse deal than you expected.  
![alt text](https://miro.medium.com/v2/resize:fit:720/format:webp/1*rHlyRxl4DEIOhHr63Zqubw.png)

