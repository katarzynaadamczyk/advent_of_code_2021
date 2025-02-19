'''
Advent of Code 
2015 day 11
my solution to task 1
task 1 - yes, it can work faster - I did not add constraints with equality and straight non-increasing numbers, 
but added oil constraint to adding and it works fast enough
idea is to add to last ord(char) 1, if it exceeds 25 -> move one backwards until there is nothing to add
check if no oil is in numbers
check other constraints
if all good change ints to chars and return


'''
import time

# decorator to measure time execution
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time:.4f} seconds to execute")
        return result
    return wrapper

class Solution:
    pass_len = 8
    a_ord = ord('a')
    max_val = ord('z') - ord('a') + 1
    oil_set = {ord('i') - ord('a'), ord('o') - ord('a'), ord('l') - ord('a')}
    
    def __init__(self, line) -> None:
        self.data = [ord(x) - Solution.a_ord for x in line.strip()]
        self.get_differences()
    

    def get_differences(self):
        self.differences = [y - x for y, x in zip(self.data[1:], self.data[:-1])]


    def constraint_not_oil(self):
        return len(set(self.data).intersection(Solution.oil_set)) == 0
    
    def constraint_two_same_letters(self):
        if self.differences.count(0) > 1 and len(self.differences) - 1 - self.differences[::-1].index(0) - self.differences.index(0) > 1:
            return True
        return False
    
    def constraint_increasing_straight(self):
        if self.differences.count(1) > 1:
            indexes_of_ones = [i for i, val in enumerate(self.differences) if val == 1]
            if 1 in [y - x for y, x in zip(indexes_of_ones[1:], indexes_of_ones[:-1])]:
                return True
        return False


    def add(self):
        act_index = Solution.pass_len - 1
        added = False
        while act_index >= 0 and not added:
            self.data[act_index] += 1
            if self.data[act_index] // Solution.max_val == 1:
                self.data[act_index] %= Solution.max_val
                act_index -= 1
            else:
                act_index = min(Solution.pass_len - 1, act_index + 1)
                added = True
        self.get_differences()

    def replace_oil(self):
        for char in Solution.oil_set:
            if char in self.data:
                act_index = self.data.index(char)
                self.data[act_index] = char + 1
                for i in range(act_index + 1, Solution.pass_len):
                    self.data[i] = 0
        self.get_differences()

    @measure_execution_time
    def solution_1(self):
        self.add()
        while not (self.constraint_increasing_straight() and self.constraint_two_same_letters() and self.constraint_not_oil()):
            self.add()
            self.replace_oil()
        return ''.join([chr(Solution.a_ord + x) for x in self.data])

    def add_2(self):
        act_index = Solution.pass_len - 1
        while act_index >= 0:
            if act_index == Solution.pass_len - 1:
                if self.data[act_index - 1] > self.data[act_index]:
                    self.data[act_index] = self.data[act_index - 1]
                    break
                elif self.data[act_index] == self.data[act_index - 1]:
                    self.data[act_index] += 1
                    if self.data[act_index] // Solution.max_val > 0:
                        self.data[act_index] = 0
                        act_index -= 1
                        continue
                    else:
                        break
                else:
                    self.data[act_index] = 0
                    act_index -= 1
                    continue
            elif act_index > 0:
                # TODO
                self.data[act_index] += 1
                if self.data[act_index] // Solution.max_val > 0:
                    self.data[act_index] = 0
                    act_index -= 1
                    continue
                else:
                    break
            else:
                self.data[act_index] += 1
                self.data[act_index] %= Solution.max_val
                break
        self.get_differences()

    @measure_execution_time
    def solution_2(self):
        self.add_2()
        while not (self.constraint_increasing_straight() and self.constraint_two_same_letters() and self.constraint_not_oil()):
            self.add_2()
            self.replace_oil()
        return ''.join([chr(Solution.a_ord + x) for x in self.data])
    


def main():
    print('TASK 1')
    sol = Solution('abcdefgh')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    
    sol = Solution('abcdefgh')
    print('test 1:', sol.solution_2())
    sol = Solution('ghijklmn')
    print('TEST 2')
    print('test 2:', sol.solution_1(), 'should equal: ghjaabcc')
    sol = Solution('ghijklmn')
    print('test 2:', sol.solution_2())
    sol = Solution('hxbxwxba')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    sol = Solution('hxbxwxba')
    print('Solution 1:', sol.solution_2())
    sol = Solution('hxbxxyzz')
    print('Solution 2:', sol.solution_1(), 'should equal hxcaabcc')
    sol = Solution('hxbxxyzz')
    print('Solution 2:', sol.solution_2(), 'should equal hxcaabcc')


if __name__ == '__main__':
    main()
