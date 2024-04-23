import re

R_format = {'add': '000000', 'sub': '000000', 'slt': '000000'}
I_format = {'addi': '001000', 'lw': '100011', 'sw': '101011', 'beq': '000100','subi':'000000'}
J_format = {'j': '000010', 'jal': '000011'}

register_numbers = {
    "$zero": "00000",
    "$at": "00001",
    "$v0": "00010",
    "$v1": "00011",
    "$a0": "00100",
    "$a1": "00101",
    "$a2": "00110",
    "$a3": "00111",
    "$t0": "01000",
    "$t1": "01001",
    "$t2": "01010",
    "$t3": "01011",
    "$t4": "01100",
    "$t5": "01101",
    "$t6": "01110",
    "$t7": "01111",
    "$s0": "10000",
    "$s1": "10001",
    "$s2": "10010",
    "$s3": "10011",
    "$s4": "10100",
    "$s5": "10101",
    "$s6": "10110",
    "$s7": "10111",
    "$t8": "11000",
    "$t9": "11001",
    "$k0": "11010",
    "$k1": "11011",
    "$gp": "11100",
    "$sp": "11101",
    "$fp": "11110",
    "$ra": "11111",
    "exitloop2":"0000000000000110",
    "loop2":"00000100000000000000000011",
    "endouterloop":"0000000000011101",
    "endinnerloop":"0000000000001000",
    "enter1":"0000000000000010",
    "innerloop":"00000100000000000000010111",
    "endcycle":"0000000000000011",
    "cycleloop":"00000100000000000000100001",
    "enter2":"0000000000000011",
    "outerloop":"00000100000000000000001111",
}

def decimal_to_binary(number, num_bits):
    binary_str = bin(number)[2:]
    return binary_str.zfill(num_bits)

f = open('mipassembler.asm', 'r')
machine_code = []

for line in f.readlines():
    if line.strip():  # Skip empty lines
        
        line = line.strip()  # Remove leading tab and trailing newline
        
        #line = line.strip()  # Remove trailing newline

        parts = re.split(r'[,\s()]+', line) 
         # Split using spaces, commas, and parentheses
        instruction = parts[0]
        if(parts[0]=="addi"):
            print(I_format[parts[0]]+register_numbers[parts[2]]+register_numbers[parts[1]]+str(bin(int(parts[3]))[2:].zfill(16))) 
        elif(parts[0]=="lw"):
            print(I_format[parts[0]]+register_numbers[parts[3]]+register_numbers[parts[1]]+str(bin(int(parts[2]))[2:].zfill(16)))
        elif(parts[0]=="sw"):
            print(I_format[parts[0]]+register_numbers[parts[1]]+register_numbers[parts[3]]+str(bin(int(parts[2]))[2:].zfill(16)))
        elif(parts[0]=="subi"):    
            print(I_format[parts[0]]+register_numbers[parts[2]]+register_numbers[parts[1]]+str(bin(int(parts[3]))[2:].zfill(16)))

        elif(parts[0]=="loop2:" or parts[0]=="outerloop:" or parts[0]=="innerloop:" or parts[0]=="cycleloop:" ):
            print(I_format[parts[1]]+register_numbers[parts[2]]+register_numbers[parts[3]]+register_numbers[parts[4]])   
        elif(parts[0]=="add"):
            print(R_format[parts[0]]+register_numbers[parts[2]]+register_numbers[parts[3]]+register_numbers[parts[1]]+'00000'+'100000')
        elif(parts[0]=="sub"):
            print(R_format[parts[0]]+register_numbers[parts[2]]+register_numbers[parts[3]]+register_numbers[parts[1]]+'00000'+'100010')
        elif(parts[0]=="j"):
            print(J_format[parts[0]]+register_numbers[parts[1]])  
        elif(parts[0]=="slt"):
            print(R_format[parts[0]]+register_numbers[parts[2]]+register_numbers[parts[3]]+'10010'+'00000'+'101010')
        elif(parts[0]=="jal"):
            print(J_format[parts[0]]+register_numbers[parts[1]]) 
        elif(parts[0]=="beq"):
            print(I_format[parts[0]]+register_numbers[parts[1]]+register_numbers[parts[2]]+register_numbers[parts[3]])             


        
f.close()

# Print the machine code instructions
for i, binary_instruction in enumerate(machine_code):
    print(f"Instruction {i+1}: {binary_instruction}")
