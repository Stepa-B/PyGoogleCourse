
import re
def CoveragePercent(log_line):
    regex = r" {2,}\"CoveragePercent\": +([0-9]{1,3})"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return result[1]
print(CoveragePercent('  "CoveragePercent": 7,'))
print(CoveragePercent('asdasdadawdwda  "CoveragePercent": 1, saca cascasd'))
print(CoveragePercent('asdasdadawdwda"CoveragePercent": 100, saca cascasd'))
print(CoveragePercent('asdasdadawdwda  "CofdveragePercent": 200, saca cascasd'))
print(CoveragePercent('asdasdadawdwda  "CoveragePercent": 300, saca cascasd'))
print(CoveragePercent('asdasdadawdwda "CoveragePercent": 400, saca cascasd'))
print(CoveragePercent('asdasdadawdwda  "CoveragePercent": 500, saca cascasd'))
print(CoveragePercent('asdasdadawdwda  "CoveqragePercent": 600, saca cascasd'))
print(CoveragePercent('asdasdadawdwda  "CoveqragePercent": 6666, saca cascasd'))