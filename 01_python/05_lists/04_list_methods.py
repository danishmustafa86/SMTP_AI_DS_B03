# 04_list_methods.py - All list methods reference

nums = [3, 1, 4, 1, 5]

# --- Adding ---
nums.append(9)          # [3, 1, 4, 1, 5, 9] - add to end
nums.insert(0, 0)       # [0, 3, 1, 4, 1, 5, 9] - insert at index
nums.extend([2, 6])     # [..., 2, 6] - add multiple items

# --- Removing ---
nums.remove(1)          # removes first occurrence of 1
nums.pop()              # removes & returns last item
nums.pop(0)             # removes & returns item at index
nums.clear()            # removes all items
# --- Finding ---
nums = [3, 1, 4, 1, 5]
print(nums.index(4))    # 2 - position of value
print(nums.count(1))    # 2 - how many times

# --- Sorting ---
nums.sort()             # [1, 1, 3, 4, 5] - ascending
nums.sort(reverse=True) # [5, 4, 3, 1, 1] - descending
nums.reverse()          # reverses current order

# --- Copying ---
copy = nums.copy()      # creates a copy

# --- Built-in functions ---
nums = [3, 1, 4, 1, 5]
print(len(nums))        # 5 - length
print(min(nums))        # 1 - smallest
print(max(nums))        # 5 - largest
print(sum(nums))        # 14 - total
print(sorted(nums))     # [1, 1, 3, 4, 5] - new sorted list

# --- Check membership ---
print(4 in nums)        # True
print(9 in nums)        # False

