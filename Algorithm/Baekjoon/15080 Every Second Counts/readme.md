https://www.acmicpc.net/problem/15080

## 문제
Meredith runs a taxi service called Ruber which offers rides to clients in small towns in western Pennsylvania. She wants to get every possible dime out of people who use her taxis, so her drivers charge a flat fee not per minute but per second. It’s important, therefore, to be able to determine the exact amount of elapsed time between the moment a client enters a cab until the moment they leave. Trying to write a program to do this has driven Meredith crazy (pun intended) so she’s come to you for some help.

## 입력
Input consists of two lines: the first contains the start time and the second contains the end time for a single taxi ride. Each time is of the form hh : mm : ss, giving the hour, minute and seconds. Meredith uses a 24 hour clock, with 0 : 0 : 0 representing 12 midnight and 23 : 59 : 59 representing one second before midnight. Note that the end time may have a value less than the start time value if the ride spans midnight (see the last sample test case for an example of this).

## 출력
Display the number of seconds between the two times. No cab ride will be equal to or longer than 24 hours.
