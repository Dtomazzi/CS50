# Questions

## What's `stdint.h`?

A library that defines data types for C/C++
## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

Thes define structs which can be used to store attributes of the file.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

8,32,32, and 16 bytes, respectively.

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."



## What's the difference between `bfSize` and `biSize`?

bfSize is the size in bytes of the bitmap file, whereas biSize is the number of bytes required by the structure.

## What does it mean if `biHeight` is negative?

If biHeight is negative, the bitmap is a top down DIB with an origin in the upper left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount specifies the BMP's color depth.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

It may return null if the input or output file does not exist.

## Why is the third argument to `fread` always `1` in our code?

The third argument specifies how many blocks to copy, and we are going byte by byte, so it is always one.

## What value does line 65 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

padding is assigned a value of 3.

## What does `fseek` do?

fseek changes the offset of the file pointer inptr.

## What is `SEEK_CUR`?

SEEK_CUR changes the location of the pointer inptr from its current position.

## Whodunit?

It was Professor Plum with the candlestick in the library
