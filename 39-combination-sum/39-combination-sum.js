/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
const combinationSum = (candidates, target) => {
  let result = [];
    
  const helper = (comb, t, i) => {
    if (t === 0) return result.push(comb);

    for (let j = i; j < candidates.length; j++) {
      const num = candidates[j] 
      
      if (num <= t) helper([...comb, num], t - num, j);
    }
  };
    
  helper([], target, 0);
    
  return result;
};