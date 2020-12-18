_input = [
    # ... Input Nums, separate by comma.
]

nums_viewed = []

for num in _input:
    nums_viewed.append(num)
    toFind = 2020 - num
    
    if toFind in nums_viewed:
        print(num * toFind)

for num1 in _input:
    for num2 in _input:
        for num3 in _input:
            if num1 + num2 + num3 == 2020 and num1 != num2 and num1 != num3 and num2 != num3:
                print(num1 * num2 * num3)
