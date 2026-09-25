class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        def combine(a, b):
            result = set()

            for x in a:
                for y in b:
                    result.add(x + y)

            return result

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    part, i = parse(i + 1)
                    current = combine(current, part)

                elif expression[i] == ',':
                    result.update(current)
                    current = {""}
                    i += 1

                else:
                    current = combine(current, {expression[i]})
                    i += 1

            result.update(current)

            return result, i + 1

        result, _ = parse(0)

        return sorted(result)