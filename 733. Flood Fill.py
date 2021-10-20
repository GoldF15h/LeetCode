class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        w = len(image[0])
        h = len(image)
        image = [[-1]*w] + image + [[-1]*w]
        h += 2
        w += 2
        for i in range(h) :
            image[i] = [-1] + image[i] + [-1]
        sr += 1
        sc += 1
        color = image[sr][sc]
        stack = [[sr,sc]]
        
        # print('test ##')
        # for i in image :
        #     print(i)
        if color != newColor :
            while stack != [] :
                print(stack)
                cur = stack[0]
                stack.pop(0)
                image[ cur[0] ][ cur[1] ] = newColor

                if image[ cur[0]-1 ][ cur[1] ] == color :
                    stack.append([ cur[0]-1 , cur[1] ])

                if image[ cur[0]+1 ][ cur[1] ] == color :
                    stack.append([ cur[0]+1 , cur[1] ])

                if image[ cur[0] ][ cur[1]+1 ] == color :
                    stack.append([ cur[0] , cur[1]+1 ])

                if image[ cur[0] ][ cur[1]-1 ] == color :
                    stack.append([ cur[0] , cur[1]-1 ])

        for i in range(h) :
            image[i] = image[i][1:w-1:]
        image = image[1:h-1:]
        
        # print('ans ##')
        # for i in image :
        #     print(i)
        
        return image