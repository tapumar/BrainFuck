# BrainFuck
A Brainfuck interpreter written in Python

### What is brainfuck?

Brainfuck is a programming language whose operation is very similar to a Turing machine.
This machine has as its components a vector of 30000 bytes, indexed from 0 to 29999, and a pointer, which holds a position od that vector.
At each step, the machine performs an instruction according to the byte stored in the position of the vector indicated by the pointer.
When this byte is zero, execution is terminated.

### Instructions

Brainfuck has 8 commands:

Instruction | Description
------------|-------------
"<" | Increment the data pointer (go to the next cell).
">" | Decrement the data pointer (go to the previous cell).
"+" | Increment the value in current cell.
"–" | Decrement the value in current cell.
"," | Read a character from stdin, and write it to the current cell.
"." | Print the character in the current cell.
"[" | Open loop. If the value in the current cell is greater than 0, go read the next instruction else jump to the closing “]”.
"]" | Jump to the opening loop.

Brainfuck ignores all characters except the eith above. For this reason, everything else is considered commentary.
