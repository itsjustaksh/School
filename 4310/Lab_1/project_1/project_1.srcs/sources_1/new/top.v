`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/13/2022 12:27:09 PM
// Design Name: 
// Module Name: Exercise 1
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


module q1(
    input a,
    input b,
    input ctrl,
    output c
    );
    
 
    assign c = (ctrl == 1) ? (a || b) : (a && b);
    
endmodule

module q2(
    input a,
    input b,
    input ctrl,
    input clk,
    output c
    );
    
    reg sto;
    assign c = sto;
    initial begin
        sto = 0; 
    end 
    always@(posedge clk) begin
        sto <= (ctrl == 1) ? (a || b) : (a && b);
    end
    
endmodule

module q3(
    input a,
    input b,
    input ctrl,
    input clk,
    output c
    );
    
    reg sto = 0;
    assign c = sto;
    always@(posedge clk) begin
        if( ctrl == 1 && a == 1 && b == 0 && sto == 0) begin
            sto = 1;
        end else if (ctrl == 1 && a == 0 && b == 1 && sto == 1) begin 
            sto = 0;
        end 
    end
    
endmodule

module testbench;
    reg a = 0, b = 0, ctrl = 0, clk = 0;
    wire c1, c2, c3;
    
    q1 testq1(.a(a), .b(b), .ctrl(ctrl), .c(c1));
    q2 testq2(.a(a), .b(b), .ctrl(ctrl), .clk(clk), .c(c2));
    q3 testq3(.a(a), .b(b), .ctrl(ctrl), .clk(clk), .c(c3));
    
    always clk = #1 ~clk;
    
    initial begin
        #5 a=0; b=0; ctrl=1;
        #5 a=0; b=1; ctrl=0;
        #5 a=0; b=1; ctrl=1;
        #5 a=1; b=0; ctrl=0;
        #5 a=1; b=0; ctrl=1;
        #5 a=1; b=1; ctrl=0;
        #5 a=1; b=1; ctrl=1;
        #5 a=0; b=1; ctrl=1;
    end
    endmodule
