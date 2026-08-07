#include <stdio.h>

#define PI 3.14159

int calculate_area(int radius) {
    return PI * radius * radius;
}

int main() {
    int r = 5;
    int area = calculate_area(r);
    printf("Calculated Area: %d\n", area);
    return 0;
}
