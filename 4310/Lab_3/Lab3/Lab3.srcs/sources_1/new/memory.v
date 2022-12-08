`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11/24/2022 09:18:48 PM
// Design Name: 
// Module Name: memory
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


module mem(
    //Memory Signals
    input MRead_request, MWrite_request, clk, rst,        // Mem request signals
    input [31:0] MAddress, [31:0] MWrite_data,            // Mem write + address bus
    output reg MRead_ready, reg MWrite_done,              // Mem ready signals
    output reg [31:0] MRead_data                          // Mem read bus
    );
    
    reg [31:0]main_mem_data [31:0];
    
    initial begin
        main_mem_data[0] = 32'h240E_00D0;
        main_mem_data[1] = 32'h87AB_CDEC;
        main_mem_data[2] = 32'h88AB_CDBF;
        main_mem_data[3] = 32'h89CB_CDEA;
        main_mem_data[4] = 32'h892B_CDBF;
        main_mem_data[5] = 32'h89AB_4DEF;
        main_mem_data[6] = 32'd3;
        main_mem_data[7] = 32'h89AB_EDEF;
        main_mem_data[8] = 32'h89AB_3CDE;
        main_mem_data[9] = 32'h89AB_6CDF;
        
        MRead_ready = 1'b0;
        MWrite_done = 1'b0;
        MRead_data = 32'h0;
    end
    
    always@(MRead_request, MWrite_request) begin
        if (rst == 1) begin
            MRead_ready = 1'b0;
            MWrite_done = 1'b0;
            MRead_data = 31'b0;
        end

        // Reset read ready flag
        if (MRead_ready == 1 && MRead_request == 0) begin
            MRead_ready = 0;                    // Reset read flag
        end

        // Reset write done flag
        if (MWrite_done == 1 && MWrite_request == 0) begin
            MWrite_done = 0;
        end

        // Read request handling
        if (MRead_request == 1) begin
            MRead_data = main_mem_data[MAddress];   // Write data to bus
            MRead_ready = 1;                        // Set read flag
            // $display("MAddress:  %h", MAddress);
            // $display("MRead_data:  %h", MRead_data);
        end

        // Write request handling 
        else if (MWrite_request == 1) begin
            main_mem_data[MAddress] = MWrite_data;
            MWrite_done = 1;
        end
    end
    
    
endmodule
