`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11/24/2022 09:18:47 PM
// Design Name: 
// Module Name: processor_tb
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


module processor_tb;
    reg clk;
    reg rst;

    reg [31:0] instruction;
    wire MRead_request;
    wire MWrite_request;
    wire MRead_ready;
    wire MWrite_done;
    wire [31:0] MWrite_data;
    wire [31:0] MRead_data;
    wire [31:0] MAddress;
    wire RegRead;
    wire RegWrite;
    wire immGen;
    wire branchSig;
    wire [31:0] PC;
    wire [31:0] res;
    wire [2:0] aluop;

    processor proc1(
        .clk(clk), 
        .rst(rst), 
        .MRead_ready(MRead_ready), 
        .MRead_request(MRead_request),
        .MWrite_request(MWrite_request), 
        .MAddress(MAddress), 
        .MWrite_data(MWrite_data),
        .MWrite_done(MWrite_done), 
        .MRead_data(MRead_data), 
        .instruction(instruction),
        .RegRead(RegRead),
        .RegWrite(RegWrite),
        .immGen(immGen),
        .branchSig(branchSig),
        .PC(PC),
        .result(res),
        .op(aluop)
    );


    initial begin
        clk = 0;
        rst = 1;
        instruction = 32'h0000_0000; 
        
        
        @(posedge clk);
        rst = 0;
        instruction = 32'h0000_0000; // Test nop

        @(posedge clk);
        instruction = 32'h7210_0000; // Test load from main mem[r1] into r2 
        wait(res);
        
        
        @(posedge clk);
        instruction = 32'h1543_0000; // Test r5 = r4 + r3
        wait(res);
        
        @(posedge clk);
        instruction = 32'h3534_0000; // Test r5 = r3 AND r4
        wait(res);
        
        @(posedge clk);
        instruction = 32'h8730_0000; // Test store into main mem[r7] from r3
        wait(res);
        
        @(posedge clk);
        instruction = 32'ha600_0000; // Test jump to PC = r6
        wait(res);

        // Test branch if r3 == r5 
        @(posedge clk);
        instruction = 32'h3564_0000; // r5 = r6 AND r4
        wait(res);
        @(posedge clk);
        instruction = 32'h3364_0000; // r3 = r6 AND r4
        wait(res);
        
        @(posedge clk);
        instruction = 32'h9135_0000; // Branch to PC = [r8] if r3 == r5   
        wait(res);
        
        // Reset all to show end of test
        @(posedge clk);
        rst = 1;
        instruction = 32'h0;
    end

    always clk = #1 ~clk;
endmodule
