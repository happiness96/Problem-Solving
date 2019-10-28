https://www.acmicpc.net/problem/12603

## 문제
You receive a credit C at a local store and would like to buy two items. You first walk through the store and create a list L of all available items. From this list you would like to buy two items that add up to the entire value of the credit. The solution you provide will consist of the two integers indicating the positions of the items in your list (smaller number first).

## 입력
The first line of input gives the number of cases, N. N test cases follow. For each test case there will be:

One line containing the value C, the amount of credit you have at the store.

One line containing the value I, the number of items in the store.

One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.

Each test case will have exactly one solution.

Limits

5 ≤ C ≤ 1000

1 ≤ P ≤ 1000

N = 10

3 ≤ I ≤ 100

## 출력
For each test case, output one line containing "Case #x: " followed by the indices of the two items whose price adds up to the store credit. The lower index should be output first.
