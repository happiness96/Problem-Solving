https://www.acmicpc.net/problem/16337

## 문제
The boss of Binary Casino wants to have control over games played in his casino. This is especially true in the case of dice games, as from time to time people try to cheat their way to the victory by manipulating dice even after a throw has already occurred. Therefore, there is a camera installed to monitor the course of every single dice game. Dice recognition, however, is not an easy task and sometimes a camera may produce a faulty image which makes the task of recognition impossible.

There are rasterized data available from a camera which took pictures of several dice. The task is to write a program which determines the value of the top side of the die in the picture or detects that the picture is corrupted. Note that the picture is transformed in such way that the sides incident to the captured top side of the die are parallel to the x and y axis. However, it is unknown which of the four possible rotations of the top side is depicted.

## 입력
The input specifies the top side of a captured die. It consists of three lines, each with three characters “o” or “:” representing a dent or a smooth surface, respectively

## 출력
Output a single line with either the number represented by the captured top side of the die or “unknown” if the image is incorrect.
