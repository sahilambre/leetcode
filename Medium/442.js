/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function (nums) {
  let duplicates = [];
  let numCount = {};

  for (let i = 0; i < nums.length; i++) {
    if (numCount[nums[i]] === undefined) {
      numCount[nums[i]] = 1;
    } else {
      numCount[nums[i]] += 1;
    }
  }

  // console.log(numCount)

  for (let num in numCount) {
    if (numCount[num] > 1) {
      duplicates.push(parseInt(num));
    }
  }
  return duplicates;
};
