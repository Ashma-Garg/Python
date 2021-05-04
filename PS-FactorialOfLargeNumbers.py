#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)


#Solutio in python was too easy so always try C/c++ solution for this problem Because they are much more tricky.

# #include <bits/stdc++.h>
#
# using namespace std;
#
# string ltrim(const string &);
# string rtrim(const string &);
#
# /*
#  * Complete the 'extraLongFactorials' function below.
#  *
#  * The function accepts INTEGER n as parameter.
#  */
# #define MAX 1000
# void extraLongFactorials(int n) {
#     int i,carry=0;
#     int a[MAX];
#     a[0]=1;
#     int rev=1;
#     for(int i=2;i<=n;i++){
#     for(int j=0;j<rev;j++){
#         int prod=(a[j]*i)+carry;
#         a[j]=prod%10;
#         carry=prod/10;
#     }
#     while(carry){
#         a[rev]=carry%10;
#         carry=carry/10;
#         rev++;
#     }
#     }
#     for(int i=rev-1;i>=0;i--){
#         cout<<a[i];
#     }
# }
#
# int main()
# {
#     string n_temp;
#     getline(cin, n_temp);
#
#     int n = stoi(ltrim(rtrim(n_temp)));
#
#     extraLongFactorials(n);
#
#     return 0;
# }
#
# string ltrim(const string &str) {
#     string s(str);
#
#     s.erase(
#         s.begin(),
#         find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
#     );
#
#     return s;
# }
#
# string rtrim(const string &str) {
#     string s(str);
#
#     s.erase(
#         find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
#         s.end()
#     );
#
#     return s;
# }
