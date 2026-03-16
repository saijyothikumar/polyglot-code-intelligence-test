// Legacy C helper placed under shared to test C parsing
#include <stdio.h>

int legacy_add(int a, int b) {
    return a + b;
}

void legacy_log(const char* msg) {
    printf("legacy: %s\n", msg);
}
