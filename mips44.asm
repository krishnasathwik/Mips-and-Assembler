.data
    next_line: .asciiz "\n"
    inp_statement: .asciiz "Enter No. of integers to be taken as input: "
    inp_int_statement: .asciiz "Enter starting address of inputs (in decimal format): "
    out_int_statement: .asciiz "Enter starting address of outputs (in decimal format): "
    enter_int: .asciiz "Enter the integer: "
    .text
# Input: N = how many numbers to sort should be entered from terminal.
# It is stored in $t1
jal print_inp_statement
jal input_int
move $t1, $t4

# Input: X = The Starting address of input numbers (each 32 bits) should be entered from
# terminal in decimal format. It is stored in $t2
jal print_inp_int_statement
jal input_int
move $t2, $t4

# Input: Y = The Starting address of output numbers (each 32 bits) should be entered
# from terminal in decimal. It is stored in $t3
jal print_out_int_statement
jal input_int
move $t3, $t4

# Input: The numbers to be sorted are now entered from terminal.
# They are stored in memory array whose starting address is given by $t2
move $t8, $t2
move $s7, $zero   # i = 0
loop1:
    beq $s7, $t1, loop1end
    jal print_enter_int
    jal input_int
    sw $t4, 0($t2)
    addi $t2, $t2, 4
    addi $s7, $s7, 1
    j loop1

loop1end:
move $t2, $t8
#############################################################
# Do not change any code above this line
# Occupied registers $t1, $t2, $t3. Don't use them in your sort function.
#############################################################

# Sorting function
# Your sorting function remains unchanged from this point.
# Ensure that you don't use $t1, $t2, or $t3 in your sorting function.

addi $s1, $t1, -1   # $s1 = size - 1
move $s2, $t2
move $t5, $0

mainloop:
    beq $t5, $s1, end  # If $t5 == $s1, we are done $t5=i

    move $t6, $t5    # $t6=min-index

innerloop:
    addi $t7, $t5, 1    # $t7=j
    beq $t7, $t1, mainloop    # If $t7 == $t1(j=n), go back to the main loop

loop2:
    lw $t8, 0($t7)           # Load array[j] into $t8
    lw $t9, 0($t6)           # Load array[min-index] into $t9
    slt $s5, $t8, $t9        # $s5 = 1 if $t8 < $t9, else $s5 = 0
    addi $s5, $s5, -1        # $s5 = 0 if $t8 < $t9, else $s5 = -1
    beq $s5, $0, mo          # If $t8 >= $t9, skip the swap

mo:
    move $t6, $t7            # Update $t6 to the new minimum index

    bne $t6, $t5, swap       # If $t6 != $t5, perform the swap

swap:
    # Swap array[$t5] and array[$t6]
    lw $t8, 0($t5)           # Load array[$t5] into $t8
    lw $t9, 0($t6)           # Load array[$t6] into $t9
    sw $t8, 0($t6)           # Store $t8 in array[$t6]
    sw $t9, 0($t5)           # Store $t9 in array[$t5]

    j innerloop              # Continue with the inner loop

j mainloop

# Printing sorted numbers
move $s7, $zero   # i = 0
loop:
    beq $s7, $t1, end
    lw $t4, 0($t3)
    jal print_int
    jal print_line
    addi $t3, $t3, 4
    addi $s7, $s7, 1
    j loop

# End of program
end:
li $v0, 10
syscall

# Input from command line (takes input and stores it in $t6)
input_int:
li $v0, 5
syscall
move $t4, $v0
jr $ra

# Print integer (prints the value of $t6)
print_int:
li $v0, 1
move $a0, $t4
syscall
jr $ra

# Print next line
print_line:
li $v0, 4
la $a0, next_line
syscall
jr $ra

# Print number of inputs statement
print_inp_statement:
li $v0, 4
la $a0, inp_statement
syscall
jr $ra

# Print input address statement
print_inp_int_statement:
li $v0, 4
la $a0, inp_int_statement
syscall
jr $ra

# Print output address statement
print_out_int_statement:
li $v0, 4
la $a0, out_int_statement
syscall
jr $ra

# Print enter integer statement
print_enter_int:
li $v0, 4
la $a0, enter_int
syscall
jr $ra
