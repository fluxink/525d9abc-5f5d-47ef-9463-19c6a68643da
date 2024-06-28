def equilibriumIndex(nums):
        for i in range(len(nums)):
            first_half = sum(nums[:i])
            second_half = sum(nums[i+1:])
            if first_half == second_half:
                return i
        return None

if __name__ == '__main__':
    assert equilibriumIndex([1, 7, 3, 6, 5, 6]) == 3
    assert equilibriumIndex([1, 2, 3, 4, 5, 6]) == None
    assert equilibriumIndex([1, 100, 0, 0, 1]) == 1
    assert equilibriumIndex([0, 1]) == 1