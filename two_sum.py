def two_sum(nums,target):
    idx =[]
    for i in range(len(nums)):
        counter =1
        if nums[i] + nums[i+counter] == target:
            idx.append(i,i+counter)
            break
        else:
            
            
            
    