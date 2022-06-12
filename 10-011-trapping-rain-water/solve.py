# https://leetcode.com/problems/trapping-rain-water/
# Step 1: Find the maximum height and corresponding index
# Step 2: Start from the left side and approach upto max-height-index 
# Step 3 : Start from the right side and reach upto max-height-index

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
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


print(f"Water-volume: {water_vol}")