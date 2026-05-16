def two_sums(nums,target):
    num_map={}

    for i in range(len(nums)):
        complement=target-nums[i]

        if complement in num_map:
            return num_map[complement],i

        num_map[nums[i]]=i

n=int(input())
nums=list(map(int,input().split()))
target=int(input())

i,j=two_sum(nums,target)
print(i,j)
