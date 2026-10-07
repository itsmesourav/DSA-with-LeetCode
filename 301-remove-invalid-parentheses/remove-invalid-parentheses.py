class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        
        def isValid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1

                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = [s]
        visited = {s}

        while queue:
            result = []

            for string in queue:

                # If valid, minimum removals have been found
                if isValid(string):
                    result.append(string)

            if result:
                return result

            # Generate next level by removing one parenthesis
            next_queue = []

            for string in queue:
                for i in range(len(string)):

                    if string[i] != '(' and string[i] != ')':
                        continue

                    new_string = string[:i] + string[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_queue.append(new_string)

            queue = next_queue

        return [""]