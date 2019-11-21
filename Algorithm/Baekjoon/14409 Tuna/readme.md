https://www.acmicpc.net/problem/14409

## 문제
Fisherman Šime caught N tunas last night. With the help of a special app, he offerred them for sale to a famous Japanese company that specializes in purchasing quality fish. In what way does the app estimate the value, or the price, of a tuna?

Based on the photo of the tuna, the app returns two estimated values, P1 and P2 . If the difference between the estimates is less than or equal to X, then the higher value is taken. If the difference is strictly larger than X, the app returns a third estimate P3 and then that estimate is taken as the final value of the tuna.

Write a programme that will, based on the given estimates (sometimes two, sometimes three of them) for each of N tunas, output the total value of caught tunas.

## 입력
The first line of input contains the integer N (1 ≤ N ≤ 20), the number of tunas from the task.

The second line of input contains the integer X (1 ≤ X ≤ 10), the number from the task.

Then, N blocks follow in one of the two following forms:

In one line, two integers P1 and P2 (1 ≤ P1 , P2 ≤ 100) from the task, or

In one line, two integers P1 and P2 (1 ≤ P1 , P2 ≤ 100) from the task, and in the second line integer P3 (1 ≤ P3 ≤ 100) from the task.

## 출력
The first and only line of output must contain the total value of caught tunas.
