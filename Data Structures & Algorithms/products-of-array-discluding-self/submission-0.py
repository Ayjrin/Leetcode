class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res






        # biggest_prod = 1
        # for j in range(len(nums)):
        #     biggest_prod *= nums[j]

        # prod_array = [biggest_prod] * len(nums)
        # for i in range(len(nums)):
        #     # total_product = 1
        #     # print(f"\n\n\n num[i] {nums[i]} -- i {i}")
        #     # for before_i in range(i-1):
        #     #     total_product *= nums[before_i]
        #     #     print(f"before i {total_product} -- i {before_i}")

        #     # for after_i in range(i+1, len(nums)):
        #     #     total_product *= nums[after_i]
        #     #     print(f"after i  {total_product} -- i {after_i}")

        #     # print(f"total {total_product} -- i {i} \n")


        #     # prod_arr.append(total_product)
        #     if nums[i] == 0:
        #         prod_array[i] = biggest_prod // nums[i]

        #     prod_array[i] = biggest_prod // nums[i]

        # prod_array = []
        # for i in range(len(nums)):
        #     if i == 0:
        #         num = 1
        #         for j in range(1, len(nums)):
        #             num *= nums[j]
        #     else:
        #         num = prod_array[i-1] * nums[i-1]
        #         if nums[i] == 0:
        #             pass
        #         else:
        #             num /= nums[i]
            
        # return prod_array