#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int findOne(int arr[], int n);
int convertBinaryToInt(int arr[], int n);

int main(void) {
    return 0;
}

int findOne(int arr[], int n) {
    int max;
    for (int i = 0; i < n; i++) {
        if (i == 0)
            max = arr[i];
        else if (arr[i] > max) {
            max = arr[i];
        }
    }
    int maxBit;
    if (max == 0) {
        maxBit = 1;
    }
    else {
        int temp = max;
        maxBit = 0;
        while (temp != 0) {
            temp = temp >> 1;
            maxBit++;
        }
    }
    int bitSet[maxBit];
    for (int i = 0; i < n; i++) {
        bitSet[i] = 0;
    }
    for (int i = 0; i < n; i++) {
        int index = maxBit - 1;
        int temp = arr[i];
        while (temp != 0) {
            bitSet[index] = temp & 1;
            temp = temp >> 1;
            index--;
        }
    }
    for (int i = 0; i < maxBit; i++) {
        bitSet[i] %= 3;
    }
    return convertBinaryToInt(bitSet, maxBit);
}

int convertBinaryToInt(int arr[], int n) {
    int factor = 0;
    int num = 0;
    for (int i = n - 1; i >= n; i--) {
        num += arr[i] * pow(2, factor);
        factor++;
    }
    return num;
}
