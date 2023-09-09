# O(n)
def daily_temperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures):
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return ans

# 이 문제가 왜 O(n)이지? 라고 생각할 수 있다.. for문안에 while문이 중첩되어있기 때문이다.
# 하지만 자세히 살펴보면 while문은 "조건"을 가진 채로 "총" n번만 실행된다.
# O(n^2)이 되기위해서는 반복 1회당 n번 반복해야 하는데, 이 코드는 반복 n회에 최대 총 n번 반복한다.
# 정확히 이해하자면 stack and stack[-1][1]의 조건은 stack에 temperature를 쌓아두고 pop을 n번 수행하는 것으로
# ans[]배열에 채워지는 값에 개수에 따라 결정된다.
# 만약 ans의 마지막쪽이 0으로 return된다면 len(ans)-ans의 0개수 만큼 반복했다고 생각하면 된다.

print(daily_temperatures([1,2,3,4]))