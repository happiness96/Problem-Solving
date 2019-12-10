https://www.acmicpc.net/problem/15241

## 문제
Every afternoon, Jack runs from his house to John's. Their houses are in an open field of size N x M. Jack is trying to use a different path each day but he is not sure how many different ways to reach John's house exist.

We will represent the field using a grid of N rows and M columns like the following:

(링크 참고)

Jack lives in the top-left position and John in the bottom-right. Jack wants to use a different route every day but does not want to waste time he will only walk down and/or right. Also, some parts of the fields have obstacles such as rocks or houses and Jack cannot go through them (they are marked with an X in the grid).

In the previous field, the 4 valid routes are:

(링크 참고)

Notice that all the valid routes will always have the same length (N + M - 1).

The number of possible paths can be very large so print the result modulo 1000000007 (10^9 + 7).

## 입력
The first line will contain two integers N and M. The rows and columns of the map.

Each of the following N lines will contain M characters. If the character is a dot (.), this position is empty. If the character is an X, it means that there is an obstacle and Jack cannot use this cell.

The top-left and bottom-right cells will never have an obstacle on them.

2 <= N <= 200

2 <= M <= 200

## 출력
Print the number of possible path between the top-left and bottom-right positions. Remember to print the result modulo 1000000007.

In most languages the modulus operator is %.
