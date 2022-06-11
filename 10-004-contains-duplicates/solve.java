// This solution is taken from https://leetcode.com/problems/contains-duplicate/discuss/2138644/simple-solution-java
// After I solved this in python
class Solution {
    public boolean containsDuplicate(int[] nums) {
        
        HashSet<Integer> h = new HashSet<Integer>();
        for(int i:nums){
            if(h.contains(i)){
                return true;
            }else{
                h.add(i);
            }
        }
        return false;
    }
}