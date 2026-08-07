#include <stdio.h>

// Unaligned struct layout (padding added by compiler)
struct PaddedStruct {
    char a;     // 1 byte
    double b;   // 8 bytes
    int c;      // 4 bytes
};

// Optimized struct layout (minimizes padding)
struct PackedStruct {
    double b;   // 8 bytes
    int c;      // 4 bytes
    char a;     // 1 byte
};

int main() {
    printf("Size of PaddedStruct: %lu bytes\n", sizeof(struct PaddedStruct));
    printf("Size of PackedStruct: %lu bytes\n", sizeof(struct PackedStruct));
    return 0;
}
