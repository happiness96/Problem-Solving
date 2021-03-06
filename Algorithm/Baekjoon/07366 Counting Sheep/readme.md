https://www.acmicpc.net/problem/7366

## 문제
After a long night of coding, Charles Pearson Peterson is having trouble sleeping. This is not only because he is still thinking about the problem he is working on but also due to drinking too much java during the wee hours. This happens frequently, so Charles has developed a routine to count sheep. Not the animal, but the word. Specically, he thinks of a list of words, many of which are close in spelling to "sheep", and then counts how many actually are the word "sheep". Charles is always careful to be case-sensitive in his matching, so "Sheep" is not a match. You are to write a program that helps Charles count "sheep".

## 입력
Input will consist of multiple problem instances. The first line will consist of a single positive integer n ≤ 20, which is the number of problem instances. The input for each problem instance will be on two lines. The first line will consist of a positive integer m ≤ 10 and the second line will consist of m words, separated by a single space and each containing no more than 10 characters.

## 출력
For each problem instance, you are to produce one line of output in the format:

Case i: This list contains n sheep.

The value of i is the number of the problem instance (we assume we start numbering at 1) and n is the number of times the word "sheep" appears in the list of words for that problem instance. Output lines should be separated by a single blank line.
