#include <assert.h>
#include <stdio.h>
#include <stdint.h>

uint64_t not(uint64_t x);
uint64_t get_n_bit(uint64_t x, uint64_t n);
uint64_t set_n_bit(uint64_t y, uint64_t n, uint64_t value);
uint64_t f(uint64_t x);
uint64_t f_reciproque(uint64_t y);

#define GOOD_VALUE 454088092903LL

int main(void) {
    //test everything works
    assert(f(19LL) == 581889079277LL);
    assert(f_reciproque(581889079277LL) == 19LL);

    //get flag
    printf("FCSC{%ld}\n", f_reciproque(GOOD_VALUE));
    return 0;
}

uint64_t not(uint64_t x) {
    assert(x == 0LL || x == 1LL);
    if (x == 1LL) {
        return 0LL;
    }
    return 1LL;
}

uint64_t get_n_bit(uint64_t x, uint64_t n) {
    assert(n < 64LL);
    return (x >> n) & 1LL;
}

uint64_t set_n_bit(uint64_t y, uint64_t n, uint64_t value) {
    assert(n < 64LL);
    assert(value == 1LL || value == 0LL);
    return y | (value << n);
}

uint64_t f_reciproque(uint64_t y) {
    uint64_t x = 0LL;

    x = set_n_bit(x, 0, get_n_bit(y, 0));
    x = set_n_bit(x, 1, get_n_bit(y, 2));
    x = set_n_bit(x, 2, get_n_bit(y, 1));
    x = set_n_bit(x, 3, get_n_bit(y, 4));
    x = set_n_bit(x, 4, get_n_bit(y, 3));
    x = set_n_bit(x, 5, not(get_n_bit(y, 6)));
    x = set_n_bit(x, 6, not(get_n_bit(y, 5)));
    x = set_n_bit(x, 7, not(get_n_bit(y, 8)));
    x = set_n_bit(x, 8, not(get_n_bit(y, 7)));
    x = set_n_bit(x, 9, not(get_n_bit(y, 10)));
    x = set_n_bit(x, 10, not(get_n_bit(y, 9)));
    x = set_n_bit(x, 11, not(get_n_bit(y, 12)));
    x = set_n_bit(x, 12, get_n_bit(y, 11));
    x = set_n_bit(x, 13, get_n_bit(y, 14));
    x = set_n_bit(x, 14, not(get_n_bit(y, 13)));
    x = set_n_bit(x, 15, get_n_bit(y, 16));
    x = set_n_bit(x, 16, not(get_n_bit(y, 15)));
    x = set_n_bit(x, 17, get_n_bit(y, 18));
    x = set_n_bit(x, 18, not(get_n_bit(y, 17)));
    x = set_n_bit(x, 19, get_n_bit(y, 20));
    x = set_n_bit(x, 20, not(get_n_bit(y, 19)));
    x = set_n_bit(x, 21, not(get_n_bit(y, 22)));
    x = set_n_bit(x, 22, get_n_bit(y, 21));
    x = set_n_bit(x, 23, not(get_n_bit(y, 24)));
    x = set_n_bit(x, 24, get_n_bit(y, 23));
    x = set_n_bit(x, 25, get_n_bit(y, 26));
    x = set_n_bit(x, 26, not(get_n_bit(y, 25)));
    x = set_n_bit(x, 27, not(get_n_bit(y, 28)));
    x = set_n_bit(x, 28, not(get_n_bit(y, 27)));
    x = set_n_bit(x, 29, not(get_n_bit(y, 30)));
    x = set_n_bit(x, 30, not(get_n_bit(y, 29)));
    x = set_n_bit(x, 31, not(get_n_bit(y, 32)));
    x = set_n_bit(x, 32, get_n_bit(y, 31));
    x = set_n_bit(x, 33, not(get_n_bit(y, 34)));
    x = set_n_bit(x, 34, not(get_n_bit(y, 33)));
    x = set_n_bit(x, 35, get_n_bit(y, 36));
    x = set_n_bit(x, 36, get_n_bit(y, 35));
    x = set_n_bit(x, 37, get_n_bit(y, 38));
    x = set_n_bit(x, 38, get_n_bit(y, 37));
    x = set_n_bit(x, 39, not(get_n_bit(y, 39)));

    return x;
}

uint64_t f(uint64_t x) {
    uint64_t y = 0LL;

    y = set_n_bit(y, 0, get_n_bit(x, 0));
    y = set_n_bit(y, 1, get_n_bit(x, 2));
    y = set_n_bit(y, 2, get_n_bit(x, 1));
    y = set_n_bit(y, 3, get_n_bit(x, 4));
    y = set_n_bit(y, 4, get_n_bit(x, 3));
    y = set_n_bit(y, 5, not(get_n_bit(x, 6)));
    y = set_n_bit(y, 6, not(get_n_bit(x, 5)));
    y = set_n_bit(y, 7, not(get_n_bit(x, 8)));
    y = set_n_bit(y, 8, not(get_n_bit(x, 7)));
    y = set_n_bit(y, 9, not(get_n_bit(x, 10)));
    y = set_n_bit(y, 10, not(get_n_bit(x, 9)));
    y = set_n_bit(y, 11, get_n_bit(x, 12));
    y = set_n_bit(y, 12, not(get_n_bit(x, 11)));
    y = set_n_bit(y, 13, not(get_n_bit(x, 14)));
    y = set_n_bit(y, 14, get_n_bit(x, 13));
    y = set_n_bit(y, 15, not(get_n_bit(x, 16)));
    y = set_n_bit(y, 16, get_n_bit(x, 15));
    y = set_n_bit(y, 17, not(get_n_bit(x, 18)));
    y = set_n_bit(y, 18, get_n_bit(x, 17));
    y = set_n_bit(y, 19, not(get_n_bit(x, 20)));
    y = set_n_bit(y, 20, get_n_bit(x, 19));
    y = set_n_bit(y, 21, get_n_bit(x, 22));
    y = set_n_bit(y, 22, not(get_n_bit(x, 21)));
    y = set_n_bit(y, 23, get_n_bit(x, 24));
    y = set_n_bit(y, 24, not(get_n_bit(x, 23)));
    y = set_n_bit(y, 25, not(get_n_bit(x, 26)));
    y = set_n_bit(y, 26, get_n_bit(x, 25));
    y = set_n_bit(y, 27, not(get_n_bit(x, 28)));
    y = set_n_bit(y, 28, not(get_n_bit(x, 27)));
    y = set_n_bit(y, 29, not(get_n_bit(x, 30)));
    y = set_n_bit(y, 30, not(get_n_bit(x, 29)));
    y = set_n_bit(y, 31, get_n_bit(x, 32));
    y = set_n_bit(y, 32, not(get_n_bit(x, 31)));
    y = set_n_bit(y, 33, not(get_n_bit(x, 34)));
    y = set_n_bit(y, 34, not(get_n_bit(x, 33)));
    y = set_n_bit(y, 35, get_n_bit(x, 36));
    y = set_n_bit(y, 36, get_n_bit(x, 35));
    y = set_n_bit(y, 37, get_n_bit(x, 38));
    y = set_n_bit(y, 38, get_n_bit(x, 37));
    y = set_n_bit(y, 39, not(get_n_bit(x, 39)));

    return y;
}
