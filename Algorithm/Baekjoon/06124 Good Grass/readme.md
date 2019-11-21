https://www.acmicpc.net/problem/6124

## 문제
Bessie believes that her favorite pasture has a patch of very special grass that is the best grass on earth. She thinks it helps cows produce more milk.

Each of the cows has returned to her assigned grazing spot, which is at some point in a fully populated rectilinear grid. Consider the example on the left below where the number of rows, NR (3 <= NR <= 100) is 6 and the number of columns, NC (3 <= NC <= 100) is 5. The spots for cows are marked with a 'C'.

Bessie actually knows the milk production P_rc (1 <= P_rc <= 100) of each of the cows in the grid; the cows are tagged with the production number in the grid on the right, below.

               COLUMN                      COLUMN
           1  2  3  4  5               1  2  3  4  5
         +--------------             +--------------
        1| C  C  C  C  C            1| 5  6  7  4  6
     R  2| C  C  C  C  C         R  2| 7  7  8  6  5
     O  3| C  C  C  C  C         O  3| 9  9  8  3  5
     W  4| C  C  C  C  C         W  4| 8  8  7  6  4
        5| C  C  C  C  C            5| 4  5  2  4  5
        6| C  C  C  C  C            6| 3  4  2  3  4
Bessie wants to find the location of the special grass. She intends to do this by finding the 3 x 3 grid of cows whose total milk production is the largest.

Find the 3 x 3 grid whose nine components sum to the greatest number and report the value of its upper left corner (first the row, then the column). In the grid above on the right, the largest sum is 71 found in the grid whose upper left corner (as depicted) is row 2, column 1.

If two 3 x 3 grids have the same sum, output the one whose row number is smallest. If more than one grid on that row has the same sum, output the one with the lowest column number.

## 입력
Line 1: Two space-separated integers: NR and NC

Lines 2..NR+1: Line r+1 contains NC space-separated integers that represent row r of the pasture's grid.

## 출력
Line 1: A single integer that is the greatest possible sum in a 3 x 3 square.

Line 2: Two space-separated integers that are respectively the row and column of the upper left corner of the 'best' 3 x 3 square grid.
