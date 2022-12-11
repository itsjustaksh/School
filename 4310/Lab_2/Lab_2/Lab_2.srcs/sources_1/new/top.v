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
    input PRead_request,
    input PWrite_request,
    output PRead_data,
    input PWrite_data,
    output PRead_ready,
    output PWrite_done,
    input PAddress,
    output MRead_request,
    output MWrite_request,
    input MRead_data,
    output MWrite_data,
    input MRead_ready,
    input MWrite_done,
    output MAddress
    );
endmodule
