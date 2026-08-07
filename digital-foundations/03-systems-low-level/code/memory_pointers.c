#include <stdio.h>
#include <stdlib.h>

int main() {
    // 1. Stack Allocation
    int stack_var = 42;
    int *stack_ptr = &stack_var;

    printf("--- Stack Allocation ---\n");
    printf("Value of stack_var: %d\n", stack_var);
    printf("Address of stack_var (&stack_var): %p\n", (void*)&stack_var);
    printf("Pointer stack_ptr points to: %p\n", (void*)stack_ptr);
    printf("Dereferenced *stack_ptr: %d\n\n", *stack_ptr);

    // 2. Heap Allocation (Dynamic Memory)
    printf("--- Heap Allocation ---\n");
    int *heap_ptr = (int*)malloc(sizeof(int));
    if (heap_ptr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    *heap_ptr = 99;
    printf("Heap Value (*heap_ptr): %d\n", *heap_ptr);
    printf("Heap Memory Address (heap_ptr): %p\n", (void*)heap_ptr);

    // Clean up heap allocation
    free(heap_ptr);
    heap_ptr = NULL;
    printf("Heap memory freed successfully.\n");

    return 0;
}
