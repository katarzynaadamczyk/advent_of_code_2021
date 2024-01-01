'''
Advent of Code 
2023 day 21
my solution to task 1 & 2

solution 1 - create a set of points that are accessible at each iteration. So, at iteration 0 it is only starting point. Then for each iteration check
accessible positions for each point and add them to new set of points. Then delete old set and replace it with a new one. At the end we get a set of 
points that are accessible at last iteration. Just get their length and it is result.

solution 2 - 

'''

from itertools import product

class Solution:

    ROCK = '#'
    GARDEN = '.'


    def __init__(self, filename, start='S') -> None:
        self.get_data(filename, start)


    def get_data(self, filename, start):
        self.data, self.nums, self.data_lens = [], [], []
        with open(filename, 'r') as myfile:
            y = 0
            for line in myfile:
                if start in line:
                    self.start_pos = (y, line.find(start))
                    line = line.replace(start, Solution.GARDEN)
                self.data.append(line.strip())
                y += 1
        self.max_y, self.min_y = y, 0
        self.max_x, self.min_x = len(self.data[0]), 0
        


    def get_map_value(self, position):
        return self.data[position[0] % self.max_y][position[1] % self.max_x]

    def get_new_positions(self, position):
        # up  
        if position[0] - 1 >= self.min_y and self.get_map_value((position[0] - 1, position[1])) == Solution.GARDEN:
            yield (position[0] - 1, position[1])

        # down  
        if position[0] + 1 < self.max_y and self.get_map_value((position[0] + 1, position[1])) == Solution.GARDEN:
            yield (position[0] + 1, position[1])

        # left  
        if position[1] - 1 >= self.min_x and self.get_map_value((position[0], position[1] - 1)) == Solution.GARDEN:
            yield (position[0], position[1] - 1)
        

        #  right 
        if position[1] + 1 < self.max_x and self.get_map_value((position[0], position[1] + 1)) == Solution.GARDEN:
            yield (position[0], position[1] + 1)

    

    def solution_1(self, start_pos=(5,5), iterations=6):
        act_gardener_positions = set()
        act_gardener_positions.add(start_pos)
        len_of_gardener_positions = [1]
        for _ in range(iterations):
            new_positions = set()
            for position in act_gardener_positions:
                for new_position in self.get_new_positions(position):
                    new_positions.add(new_position)
            len_of_gardener_positions.append(len(new_positions))
            del act_gardener_positions
            act_gardener_positions = new_positions
            if len(len_of_gardener_positions) > 2 and len_of_gardener_positions[-1] == len_of_gardener_positions[-3]:
                print(start_pos, iterations, len_of_gardener_positions)
                if len(len_of_gardener_positions) % 2 == iterations % 2:
                    return len_of_gardener_positions[-1]
                return len_of_gardener_positions[-2]
        print(start_pos, iterations, len_of_gardener_positions)
        return len_of_gardener_positions[-1]
    
    def get_parameter_A_B(self, coordinate, steps):
        result = 0
        for point in product((coordinate, self.max_x - 1 - coordinate), repeat=2):
            result += self.solution_1(start_pos=point, iterations=steps)
        return result
    
    
    def get_parameter_E_F(self, coordinate_1, coordinate_2, coordinate_3, steps):
        result = 0
        for point in [(coordinate_1, coordinate_2), (coordinate_2, coordinate_1), (coordinate_1, coordinate_3), (coordinate_3, coordinate_1)]:
            result += self.solution_1(start_pos=point, iterations=steps)
        return result
    
    def get_sum_even(self, num):
        return sum([i for i in range(0, num-1, 2)])
    
    def solution_2(self, steps=50, start_pos=(5,5)):
        N = steps // self.max_y
        print(N)
        # counts add
        add = self.solution_1(start_pos=start_pos, iterations=self.max_y * 2)
        # counts F 
        F = self.get_parameter_E_F(start_pos[0], 0, self.max_x - 1, 2 * self.max_x)
        # counts F_prim 
        F_prim = self.get_parameter_E_F(start_pos[0], 0, self.max_x - 1, self.max_x - 1)
        # counts E
        E = self.get_parameter_E_F(start_pos[0], 0, self.max_x - 1, 2 * self.max_x - 1)
        # counts A
        A = self.get_parameter_A_B(0, 2 * self.max_x)
        # counts A_prim
        A_prim = self.get_parameter_A_B(0, self.max_x + self.max_x // 2)
        # counts B
        B = self.get_parameter_A_B(0, 2 * self.max_x + 1)
        # counts B_prim
        B_prim = self.get_parameter_A_B(0, self.max_x // 2)
        print(add, F, F_prim, E, A, A_prim, B, B_prim)
        result = add + F_prim + N // 2 * E + (N // 2 - 1) * F + self.get_sum_even(N) * B + N * B_prim + (N // 2 - 1) ** 2 * A + (N - 1) * A_prim
        return result


def main():
    print('TASK 1')
    sol = Solution('2023/Day_21/test.txt')
    print('TEST 1')
    print(sol.start_pos)
    print(sol.max_x, sol.max_y)
    print('test 1 -    6:', sol.solution_1(iterations=6))
    print('test 1 -  101:', sol.solution_2(steps=101))
    sol = Solution('2023/Day_21/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1(iterations=64, start_pos=(65, 65)))
    print('Solution 2 - 327', sol.solution_2(steps=327, start_pos=(65, 65)))
    #print('Solution 2 - 26501365:', sol.solution_2(steps=26501365, start_pos=(65, 65)))
   # print('Solution 1:', sol.solution_1(iterations=200))
  #  print('Solution 1:', sol.solution_1(iterations=300))
   # print('Solution 1:', sol.solution_1(iterations=1000))



if __name__ == '__main__':
    main()
