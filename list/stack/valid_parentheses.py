def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p: 
            # not stack : 처음에 스택이 비어있는 상태에서 닫는 문자가 들어온다면, false
            # 위 조건에 해당하지 않다면 stack.pop이 행해짐. (중요)
            return False
    return not stack