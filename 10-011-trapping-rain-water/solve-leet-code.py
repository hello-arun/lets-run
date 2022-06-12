# As submitted by me on https://leetcode.com/problems/trapping-rain-water/submissions/
class Solution:
    def trap(self, heights: List[int]) -> int:
        water_vol=0
        max_height = heights[0]
        max_height_index = 0
        for i,height in enumerate(heights):
            water_vol += height
            if height>max_height:
                max_height=height
                max_height_index=i
        water_vol = max_height*len(heights)-water_vol

        i,hmax_i=0,0
        while i<max_height_index:
            delta_water_vol=-(max_height-heights[i])
            if heights[i]<hmax_i:
                delta_water_vol+=hmax_i-heights[i]
            else:
                hmax_i=heights[i]
            water_vol+=delta_water_vol
            i+=1

        i,hmax_i=len(heights)-1,0
        while i>max_height_index:
            delta_water_vol=-(max_height-heights[i])
            if heights[i]<hmax_i:
                delta_water_vol+=hmax_i-heights[i]
            else:
                hmax_i=heights[i]
            water_vol+=delta_water_vol
            i-=1
        return water_vol