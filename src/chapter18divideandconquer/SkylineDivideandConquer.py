class SkyLinesDivideandConquer:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkylines(self, buildings):
        result = []
        if len(buildings) == 0:
            return result
        if len(buildings) == 1:
            result.append([buildings[0][0], buildings[0][2]])
            result.append([buildings[0][1], 0])
            return result
            
        mid = (len(buildings) - 1) / 2
        leftSkyline = self.getSkyline(0, mid, buildings)
        rightSkyline = self.getSkyline(mid + 1, len(buildings)-1, buildings)
        result = self.mergeSkylines(leftSkyline, rightSkyline)
        return result

    def getSkyline(self, start, end, buildings):
        result = []
        if start == end:
            result.append([buildings[start][0], buildings[start][2]])
            result.append([buildings[start][1], 0])
            return result
        mid = (start + end) / 2
        leftSkyline = self.getSkyline(start, mid, buildings)
        rightSkyline = self.getSkyline(mid+1, end, buildings)
        result = self.mergeSkylines(leftSkyline, rightSkyline)
        return result
        
    def mergeSkylines(self, leftSkyline, rightSkyline):
        result = []
        i, j, h1, h2, maxH = 0, 0, 0, 0, 0
        while i < len(leftSkyline) and j < len(rightSkyline):
            if leftSkyline[i][0] < rightSkyline[j][0]:
                h1 = leftSkyline[i][1]
                if maxH != max(h1, h2):
                    result.append([leftSkyline[i][0], max(h1, h2)])
                maxH = max(h1, h2)
                i += 1
            elif leftSkyline[i][0] > rightSkyline[j][0]:
                h2 = rightSkyline[j][1]
                if maxH != max(h1, h2):
                    result.append([rightSkyline[j][0], max(h1, h2)])
                maxH = max(h1, h2)
                j += 1
            else:
                h1 = leftSkyline[i][1]
                h2 = rightSkyline[j][1]
                if maxH != max(h1, h2):
                    result.append([rightSkyline[j][0], max(h1, h2)])
                maxH = max(h1, h2)
                i += 1
                j += 1
        while i < len(leftSkyline):
            result.append(leftSkyline[i])
            i += 1
        while j < len(rightSkyline):
            result.append(rightSkyline[j])
            j += 1
        return result
