`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11/24/2022 09:18:47 PM
// Design Name: 
// Module Name: control
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////

module control(
    input clk,
    input rst,
    input [3:0]instruction,           // instruction from proc
    output reg MemRead, reg MemWrite, // Mem signals
    output reg RegRead, reg RegWrite, // Reg file Signals
    output reg branch,  reg immD,     // Other signals
    output reg [2:0]aluop
    );
    
    
    /*
        Set signals based on instruction
        Nop: No operation/stall cycle: 0000 
        Add: addition: 0001
        Sub: subtraction: 0010
        And: logical and: 0011
        Sal: shift to the left: 0100
        Sar: shift to the right: 0101
        Or: logical or: 0110
        Lw: load: 0111
        Sw: store: 1000
        Bleq: branch if equal: 1001
        J: jump: 1010
        Addi: Add immediate 1011
    */

    initial begin
        RegRead <= 0;
        RegWrite <= 0;
        MemRead <= 0;
        MemWrite <= 0;
        immD <= 0;
        branch <= 0;
        aluop <= 0;
    end

    
    always @(instruction) begin
        if (rst) begin
            RegRead <= 0;
            RegWrite <= 0;
            MemRead <= 0;
            MemWrite <= 0;
            immD <= 0;
            branch <= 0;
            aluop <= 3'b0;
        end
        case (instruction)
            4'h0: begin // nop
                RegRead <= 0;
                RegWrite <= 0;
                MemRead <= 0;
                MemWrite <= 0;
                immD <= 0;
                branch <= 0;
                aluop <= 4'b0;
            end
            4'h1: begin // add
                RegRead <= 1;
                RegWrite <= 1;
                MemRead <= 0;
                MemWrite <= 0;
                immD <= 0;
                branch <= 0;
                aluop <= 3'd1;
            end
            4'h2: begin // sub
                RegRead <= 1;
                RegWrite <= 1;
                MemRead <= 0;
                MemWrite <= 0;
                immD <= 0;
                branch <= 0;
                aluop <= 3'd2;
            end
            4'h3: begin // and 
                RegRead <= 1;
                RegWrite <= 1;
                MemRead <= 0;
                MemWrite <= 0;
                immD <= 0;
                branch <= 0;
                aluop <= 3'd3;
            end
            4'h4: begin // sal
                RegRead <= 1;
                RegWrite <= 1;
                MemRead <= 0;
                MemWrite <= 0;
                immD <= 0;
                branch <= 0;
                aluop <= 3'd4;
            end 
            4'h5: begin // sar
                RegRead <= 1;
                RegWrite <= 1;
                MemRead <= 0;
                MemWrite <= 0;
                immD <= 0;
                branch <= 0;
                aluop <= 3'd5;
            end
            4'h6: begin // or
                RegRead <= 1;
                RegWrite <= 1;
                MemRead <= 0;
                MemWrite <= 0;
                immD <= 0;
                branch <= 0;
                aluop <= 3'd6;
            end
            4'h7: begin // lw
                RegRead <= 1;
                RegWrite <= 1;
                MemRead <= 1;
                MemWrite <= 0;
                immD <= 0;
                branch <= 0;
                aluop <= 3'd1;
            end
            4'h8: begin // sw
                RegRead <= 1;
                RegWrite <= 1;
                MemRead <= 0;
                MemWrite <= 1;
                immD <= 0;
                branch <= 0;
                aluop <= 3'd1;
            end
            4'h9: begin // bleq
                RegRead <= 1;
                RegWrite <= 0;
                MemRead <= 0;
                MemWrite <= 0;
                immD <= 0;
                branch <= 1;
                aluop <= 3'd2;
            end
            4'ha: begin // J
                RegRead <= 1;
                RegWrite <= 0;
                MemRead <= 0;
                MemWrite <= 0;
                immD <= 1;
                branch <= 1;
                aluop <= 3'd0;
            end
            4'hb: begin // Addi
                RegRead <= 1;
                RegWrite <= 1;
                MemRead <= 0;
                MemWrite <= 0;
                immD <= 1;
                branch <= 0;
                aluop <= 3'd1;
            end
        endcase
    end


endmodule
