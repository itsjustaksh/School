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
    input PRead_request,PWrite_request,          // Processor Request signals
    input [7:0] PAddress, [7:0] PWrite_data,     // Processor write bus
    output reg PRead_ready, PWrite_done,         // Processor ready signals
    output reg [7:0] PRead_data,                 // Processor read bus

    //Memory Signals
    output reg MRead_request, reg MWrite_request,           // Mem request signals
    output reg [7:0] MAddress, reg [7:0] MWrite_data,       // Mem write bus
    input MRead_ready, MWrite_done,                         // Mem ready signals
    input [31:0] MRead_data,                                // Mem read bus

    //General Signals
    input clk, rst
    );
    
    reg [31:0] cache_data [7:0]; // 8 block array with 32 bit entries
    reg [2:0] tag [7:0];         // 8 block array with 3 bit entries
    reg valid [7:0];             // 8 block array with 1 bit entries
    
    reg [7:0]local_addr;        // Local address register in case input address changes before completion
    reg [7:0]local_data_8 ;     // Local data register - 8 bit
    reg [2:0]block_comp;        // Block to read/write
    reg [2:0]tag_temp;          // Tag to read/write
    reg [1:0]offset;            // Section to read/write
    
    /*
     * State register to track current state
     *
     * State List
     *
     * 000 - Initial/Idle 
     * 001 - Decode
     * 010 - Read from cache and pass data
     * 011 - Read from mem
     * 100 - Write to mem
     * 101 - Write to cache (and Mem)
     * 110
     * 111
     */
    reg [3:0]state = 3'b000; // Default state 0
    
    // Initialize outputs to low
    initial begin
        PRead_ready = 0;
        PWrite_done = 0;
        PRead_data = 0;
        MRead_request = 0;
        MWrite_request = 0;
        MAddress = 0;
        MWrite_data = 0;
    end
    
    // Initialize memory block
    mem mem1(.clk(clk), .rst(rst), .MRead_ready(MRead_ready), .MRead_request(MRead_request), .MWrite_request(MWrite_request), 
            .MAddress(MAddress), .MWrite_data(MWrite_data), .MWrite_done(MWrite_done), .MRead_data(MRead_data));
    
    
    always@(posedge clk) begin
    
        // Reset logiC
        if (rst) begin
            state = 3'b000;
            block_comp = 3'b000;
            tag_temp = 3'b000;
            offset = 2'b00;
            PRead_ready = 'b0;
            PWrite_done = 'b0;
            PRead_data = 0;
        end
    
        //Reset flags if necessary
        if(~PRead_request && PRead_ready) begin
            PRead_ready = 0;
        end
        
        if(~PWrite_request && PWrite_done) begin
            PWrite_done = 0;
        end
        
        // First singal always comes from processor - only act if idle
        else if ((PRead_request || PWrite_request) && (state == 3'b000)) begin
            //Read and store inputs
            local_addr = PAddress;
            
            // Set next state
            state = 3'b001;
        end
        
        // Decode
        else if (state == 3'b001) begin
            block_comp = local_addr[4:2];
            tag_temp = local_addr[7:5];
            offset = local_addr[1:0];
            
            // Handle Read request
            if (PRead_request) begin
                // Set state based on whether block is valid or not 
                // Cache Hit
                if ( (tag_temp == tag[block_comp]) && valid [block_comp] ) begin
                    state = 3'b010; // Need to pull from cache and pass data
                // Cache miss
                end else begin
                    state = 3'b011; // Need to pull from mem and allocate to cache
                end
            end 
            
            // Handle Write request
            else if (PWrite_request) begin
                local_data_8 = PWrite_data;
                // Cache Hit
                if ( (tag_temp == tag[block_comp]) && (valid [block_comp] == 1'b1) ) begin
                    state = 3'b101; // Need to write to both mem and cache
                // Cache Miss
                end else begin
                    state = 3'b100; // Need to write to mem
                end
            end
        end        
        
        // Retrieve cache data
        else if (state == 3'b010) begin
            // Find data in block and write to PRead_data
            case (offset)
                // block_comp will be valid as we cannot get here without
                // going through previous state code
                2'b00: PRead_data = cache_data[block_comp][7:0];
                2'b01: PRead_data = cache_data[block_comp][15:8];
                2'b10: PRead_data = cache_data[block_comp][23:16];
                2'b11: PRead_data = cache_data[block_comp][31:24];
            endcase
            
            // Set Read ready signal
            PRead_ready = 1;
            state = 3'b000; // back to idle as read is complete
        end
        
        // Read from mem
        else if (state == 3'b011) begin
            // Set Mem read signals
            MRead_request = 1;
            MAddress = local_addr;
            // Will happen on next clock cycle, but state has not changed so 
            // this block will be executed again
            if (MRead_ready == 1) begin
                cache_data[block_comp] = MRead_data; // Write into memory
                tag[block_comp] = local_addr[7:5];
                valid[block_comp] = 1; // set valid bit
                MRead_request = 0; // Reset read request once read is complete
                state = 3'b010; // rest of the work is the same as cache read state, so go back to there
            end
        end
        
        // Processor Write to mem (no cache) state
        else if (state == 3'b100) begin 
            // Set Mem signals
            MWrite_request = 1'b1;
            MWrite_data = PWrite_data;
            MAddress = PAddress;
            
            // Will happen on next clock cycle, will still run as state is unchanged
            if (MWrite_done == 1'b1) begin 
                state = 3'b000;
                MWrite_request = 1'b0;
                PWrite_done = 1'b1;
                
                // no allocate on miss
                if (tag_temp == tag[block_comp]) begin 
                    valid[block_comp] = 1'b0; // clear valid bit
                end
            end
        end
        
        // Processor update cache and write to mem
        else if (state == 3'b101) begin 
            // Write to cache
            cache_data[block_comp] = local_data_8; // Write data
            tag[block_comp] = tag_temp; // Update tag
            valid[block_comp] = 1'b1; // Update valid bit

            // Mem write
            // Set Mem signals
            MWrite_request = 1'b1;
            MWrite_data = local_data_8;
            MAddress = PAddress;
            
            // Will happen on next clock cycle, will still run as state is unchanged
            if (MWrite_done == 1'b1) begin 
                state = 3'b000;
                MWrite_request = 1'b0;
                PWrite_done = 1'b1;
                // no allocate on miss
                if (tag_temp == tag[block_comp]) begin 
                    valid[block_comp] = 1'b0; // clear valid bit
                end
            end
        end
    end
    
     
endmodule