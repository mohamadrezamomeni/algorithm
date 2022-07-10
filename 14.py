class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hashmap = {}
        for i, string in enumerate(strs):
            for string_index in range(1, len(string)+1):
                if i >= 1 and string[0:string_index] not in hashmap:
                    continue

                if string[0:string_index] in hashmap and hashmap[string[0:string_index]]["index"] == i:
                    continue
                if string[0:string_index] in hashmap:
                    hashmap[string[0:string_index]]["index"] = i
                    hashmap[string[0:string_index]]["val"] += 1
                if string[0:string_index] not in hashmap:
                    hashmap[string[0:string_index]] = {"index": i, "val": 1}
        strs_len = len(strs)
        results = ""
        for k, v in hashmap.items():
            if v["val"] == strs_len and len(k) > len(results):
                results = k

        return results
