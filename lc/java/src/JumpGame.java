/*
https://leetcode.com/problems/jump-game/


*/
public class JumpGame {
    public boolean canJump(int[] nums) {
        if (nums.length == 0) return true;

        int end = nums.length - 1;
        int reach = nums[0];
        int curr = 1;
        while (curr <= reach && reach < end) {
            reach = Math.max(reach, curr + nums[curr]);
            curr++;
        }
        return reach >= end;
    }
}
