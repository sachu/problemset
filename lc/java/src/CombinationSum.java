/*
https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (C) and a target number (T), find all unique
combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
*/

import java.util.List;
import java.util.ArrayList;

public class CombinationSum {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(candidates, 0, target, res, new ArrayList<>());
        return res;
    }

    private void dfs(int[] candidates, int startIdx, int target,
                     List<List<Integer>> res, List<Integer> currPath) {
        if (target < 0) {
            return;
        }
        if (target == 0) {
            res.add(currPath);
            return;
        }
        for (int i = startIdx; i < candidates.length; i++) {
            int num = candidates[i];
            List<Integer> nextPath = new ArrayList<>(currPath);
            nextPath.add(num);
            dfs(candidates, i, target - num, res, nextPath);
        }
    }
}