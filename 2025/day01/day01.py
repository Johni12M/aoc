class Solution:
    def part1(self):
        with open("input.txt", "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        ans = 0
        dial = 50
        for line in lines:
            direction = line[0]
            count = int(line[1:])
            if direction == "L":
                dial -= count
            else:
                dial += count
            dial %= 100  # wrap around 0-99

            if dial == 0:
                ans += 1
        return ans

    def part2(self):
        pass


if __name__ == "__main__":
    solution = Solution()
    print(solution.part1())
