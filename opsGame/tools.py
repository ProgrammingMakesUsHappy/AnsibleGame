#  -*- endcoding=UTF-8 -*-


class tool:
    def percent2int(jsonPercentData):
        toList = list(jsonPercentData)
        del toList[-1]
        # length = len(toList)
        intStr = ''
        for num in toList:
            intStr = intStr + num
        result = int(intStr)
        return result