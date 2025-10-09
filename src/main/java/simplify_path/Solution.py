class Solution:
    def simplifyPath(self, path: str) -> str:
        
        parts = path.split("/")
        simplified_list = []

        for part in parts:
            if part =="" or part == ".":
                continue
            elif part == "..":
                if simplified_list:
                    simplified_list.pop()
            else:
                simplified_list.append(part)
                
        return "/" + "/".join(simplified_list)
