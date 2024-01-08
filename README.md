## Art using Code
Just like how a seemingly empty tiny patch of sky reveals thousands of galaxies if you capture enough light over time, there's potential to find the next wave of stars if you let the clock run long enough with public goods funding.

## What does this script do?
- Collates every single project that earned more than $10 in direct donations in 2023 on Gitcoin.
- Plots a honeycomb where each bin represents a project, and its brightness indicates the amounts raised in direct donations
- When the brightness is linear to the amount received, we hardly see more than a couple dozen projects.
  
![Darker honeycomb showcasing power law in public goods funding](https://github.com/rohitmalekar/PGF-s-Deep-Fields/blob/main/PGF_Linear.jpg)

- This is consistent with the power law distribution leading to most popular public goods getting a lion's share of funding + [long tail of public goods projects](https://gov.gitcoin.co/t/long-tail-public-goods-funding/17318)
- However, every dark bin is still a recipient of direct donations from the community holding the potential to grow brighter over time
- We simulate "long exposure" to capture the light coming from these seemingly darker spots by rendering the honeycomb on a logarithmic scale
  
![With log scale, the honeycomb lit up showing the impact of community funding for future stars](https://github.com/rohitmalekar/PGF-s-Deep-Fields/blob/main/PGF_Log.jpg)

- Now, with this renewed perspective, we can see the potential for light in every bin - a signal to the community that even if their direct donations might not be going to the most popular public goods projects, their ecosystem-wide support raises the probability of discovering newer starts of the future.

## Steps
1. Execute create_datasets.py to extract the list of projects with at least $10 of direct donations in 2023 on Gitcoin
2. hexbin_tales.py creates the animation for the two distinct honeycombs based on linear and log distribution for brightness

## Credits
The script uses [Gitcoin Grants Data Portal](https://davidgasquez.github.io/gitcoin-grants-data-portal/) by [David Gasquez](https://twitter.com/davidgasquez) as a data source.
 
