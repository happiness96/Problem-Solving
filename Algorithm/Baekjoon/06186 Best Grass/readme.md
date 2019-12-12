https://www.acmicpc.net/problem/6186

## 문제
Bessie is planning her day of munching tender spring grass and is gazing out upon the pasture which Farmer John has so lovingly partitioned into a grid with R (1 <= R <= 100) rows and C (1 <= C <= 100) columns. She wishes to count the number of grass clumps in the pasture.

Each grass clump is shown on a map as either a single '#' symbol or perhaps two '#' symbols side-by-side (but not on a diagonal). Given a map of the pasture, tell Bessie how many grass clumps there are.

By way of example, consider this pasture map where R=5 and C=6:

.#....

..#...

..#..#

...##.

.#....

This pasture has a total of 5 clumps: one on the first row, one that spans the second and third row in column 2, one by itself on the third row, one that spans columns 4 and 5 in row 4, and one more in row 5.

## 입력
Line 1: Two space-separated integers: R and C

Lines 2..R+1: Line i+1 describes row i of the field with C characters, each of which is a '#' or a '.'

## 출력
Line 1: A single integer that is the number of grass clumps Bessie can munch
