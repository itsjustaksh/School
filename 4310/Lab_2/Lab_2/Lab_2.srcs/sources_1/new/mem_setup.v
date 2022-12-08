`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/11/2022 03:02:06 PM
// Design Name: 
// Module Name: mem_setup
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
    input MRead_request, MWrite_request, clk, rst,      // Mem request signals
    input [7:0] MAddress, [7:0] MWrite_data,            // Mem write + address bus
    output reg MRead_ready, reg MWrite_done,            // Mem ready signals
    output reg [31:0] MRead_data                        // Mem read bus

    );
    
    reg [31:0]main_mem_data [9:0];
    reg [1:0] offset;
    reg [5:0] addr;
    
    initial begin
        main_mem_data[0] = 32'h240E_00D0;
        main_mem_data[1] = 32'h87AB_CDEC;
        main_mem_data[2] = 32'h88AB_CDBF;
        main_mem_data[3] = 32'h89CB_CDEA;
        main_mem_data[4] = 32'h892B_CDBF;
        main_mem_data[5] = 32'h89AB_4DEF;
        main_mem_data[6] = 32'h45A3_389E;
        main_mem_data[7] = 32'h89AB_EDEF;
        main_mem_data[8] = 32'h89AB_3CDE;
        main_mem_data[9] = 32'h89AB_6CDF;
    end
    
    // always@(posedge clk) begin
    //     $display(main_mem_data[3]);
    // end
    
    always@(clk, rst) begin
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
            MRead_ready = 1;                    // Set read flag
            MRead_data = main_mem_data[MAddress];  // Write data to bus
            // $display("MAddress:  %h", MAddress);
            // $display("MRead_data:  %h", MRead_data);
        end

        // Write request handling 
        // This assumes that memory addresses are set up as 6 bit address and 2 bit offset,
        // to access the 8 bit words in the 32 bit block.
        if (MWrite_request == 1) begin
            offset = MAddress[1:0];
            addr  = MAddress[7:2];
            case (offset)
                2'b00: main_mem_data[addr][ 7:0]  = MWrite_data;
                2'b01: main_mem_data[addr][15:8]  = MWrite_data;
                2'b10: main_mem_data[addr][23:16] = MWrite_data;
                2'b11: main_mem_data[addr][31:24] = MWrite_data;
            endcase
        end
    end
    
    
endmodule
