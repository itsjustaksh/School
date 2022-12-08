`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: Carleton
// Engineer: Aksh Ravi
// 
// Create Date: 09/24/2019 11:03:22 AM
// Design Name: 
// Module Name: cache_tb
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


module cache_tb;

    reg clk;
    reg rst;

    // Processor side
    reg PRead_request;
    reg PWrite_request;
    wire PRead_ready;
    wire PWrite_done;
    reg [7:0] PWrite_data;
    wire [7:0] PRead_data;
    reg [7:0] PAddress;

    // Memory side
    wire MRead_request;
    wire MWrite_request;
    wire MRead_ready;
    wire MWrite_done;
    wire [7:0] MWrite_data;
    wire [31:0] MRead_data;
    wire [7:0] MAddress;
    
    cache cache1(.clk(clk), .rst(rst), .PRead_request(PRead_request), .PWrite_request(PWrite_request), 
                .PRead_data(PRead_data), .PRead_ready(PRead_ready), .PWrite_data(PWrite_data), .PAddress(PAddress),
                .PWrite_done(PWrite_done), .MRead_ready(MRead_ready), .MRead_request(MRead_request),
                .MWrite_request(MWrite_request), .MAddress(MAddress), .MWrite_data(MWrite_data),
                .MWrite_done(MWrite_done), .MRead_data(MRead_data));
    

    initial
    begin
        clk = 0;
        rst = 1;
        
        PRead_request = 0;
        PAddress = 0;
        PWrite_request = 0;
        PWrite_data = 0;
        
        #5;
        @(posedge clk);
        rst = 0;
        #10;
        
        //test logic for cache miss
        @(posedge clk);
        PAddress = 6;
        PRead_request = 1;
        wait(PRead_ready);
        $display("PRead_data: %h", PRead_data);
        PRead_request = 0;
        PAddress = 0;
        #10;
        
         //test logic for cache hit
         @(posedge clk);
         PAddress = 7;
         PRead_request = 1;
         wait(PRead_ready);
         @(posedge clk);
         PRead_request = 0;
         #10;
    end

    always clk = #1 ~clk;

endmodule