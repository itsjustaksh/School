`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/04/2022 08:31:56 PM
// Design Name: 
// Module Name: cache
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


module cache(
    //Processor Signals
    input PRead_request,PWrite_request,          // Proc Request signals
    input [7:0] PAddress, [7:0] PWrite_data,     // Proc write bus
    output PRead_ready, PWrite_done,             // Proc ready signals
    output [7:0] PRead_data,                     // Proc read bus

    //Memory Signals
    output MRead_request, MWrite_request,        // Mem request signals
    output [7:0] MAddress, [31:0] MWrite_data,   // Mem write bus
    input MRead_ready, MWrite_done,              // Mem ready signals
    input [31:0] MRead_data,                     // Mem read bus

    //General Signals
    input clk, rst
    );
    
    reg [31:0] cache_data [7:0]; // 8 block array with 32 bit entries
    reg [2:0] tag [7:0];         // 8 block array with 3 bit entries
    reg valid [7:0];             // 8 block array with 1 bit entries


    
    
    
    
endmodule
