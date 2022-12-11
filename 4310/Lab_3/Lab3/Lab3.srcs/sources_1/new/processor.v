`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11/24/2022 09:18:47 PM
// Design Name: 
// Module Name: processor
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


module processor (
    input clk,
    rst,
    input [31:0] instruction,
    input [31:0] MRead_data,
    input MWrite_done,
    input MRead_ready,
    input MRead_request,
    input MWrite_request,
    input immGen,
    input branchSig,
    input RegRead,
    input RegWrite,
    input [2:0] op,
    output reg [31:0] PC,
    output reg [31:0] MWrite_data,
    output reg [31:0] MAddress,
    output reg [31:0] result
);

  reg [31:0] regFile[15:0];  // Register File
  reg [3:0] opcode;  // ALU OPCode
  reg [3:0] rD;  // Support for up to 16 registers in regFile
  reg [3:0] r1;  // Support for up to 16 registers in regFile
  reg [3:0] r2;  // Support for up to 16 registers in regFile
  reg [19:0] immD;
  reg [32:0] temp;

  // Module setup and connections

  // Control Unit 
  control control_unit (
      .clk(clk),
      .rst(rst),
      .instruction(opcode),
      .MemRead(MRead_request),
      .MemWrite(MWrite_request),
      .RegRead(RegRead),
      .RegWrite(RegWrite),
      .branch(branchSig),
      .immD(immGen),
      .aluop(op)
  );

  // Main Memory
  mem main_mem (
      .clk(clk),
      .rst(rst),
      .MRead_ready(MRead_ready),
      .MRead_request(MRead_request),
      .MWrite_request(MWrite_request),
      .MAddress(MAddress),
      .MWrite_data(MWrite_data),
      .MWrite_done(MWrite_done),
      .MRead_data(MRead_data)
  );

  // Initialize variables
  initial begin
    // Load first half of Register file with default initial vals
    regFile[0] = 31'h5f35_5fcc;
    regFile[1] = 31'd6;
    regFile[2] = 31'h54f8_ac66;
    regFile[3] = 31'd8;
    regFile[4] = 31'h0c34_fdaf;
    regFile[5] = 31'h813d_e87d;
    regFile[6] = 31'h0400_7b5e;
    regFile[7] = 31'd2;

    // Load defaults into reg variables and PC
    rD = 4'b0;
    r1 = 4'b0;
    r2 = 4'b0;
    PC = 32'h0;
    result = 32'h0;

    // Load output initials as 0
    MWrite_data = 32'h0;
    MAddress = 32'h0;
  end

  // ALU definition
  // Supported operations: 
  // Nop: No operation/stall cycle: 0000 
  // Add: addition: 0001
  // Sub: subtraction: 0010
  // And: logical and: 0011
  // Sal: shift to the left: 0100
  // Sar: shift to the right: 0101
  // Or: logical or: 0110
  // Lw: load: 0111
  // Sw: store: 1000
  // Bleq: branch if equal: 1001
  // J: jump: 1010
  // Addi: Add with immediate: 1011

  // ALU operation
  always @(posedge clk) begin
    if (rst == 1) begin
      opcode = 4'h0;
      rD = 4'h0;
      r1 = 4'h0;
      immD = 20'h0;
      r2 = 4'h0;
      PC = 32'h0;
      result = 32'h0;
      MWrite_data = 32'h0;
      MAddress = 32'h0;
    end else begin
      opcode = instruction[31:28];
      rD = instruction[27:24];
      r1 = instruction[23:20];
      if (opcode == 4'b1011) begin
        immD = instruction[19:0];
      end else begin
        r2 = instruction[19:16];
      end

      case (opcode)
        4'h0: ;  // nop
        4'h1: begin
          regFile[rD] = regFile[r1] + regFile[r2];
          PC = PC + 1;
          result = regFile[rD];
        end  // Add
        4'h2: begin
          regFile[rD] = regFile[r1] - regFile[r2];
          PC = PC + 1;
          result = regFile[rD];
        end  // Sub
        4'h3: begin
          regFile[rD] = regFile[r1] & regFile[r2];
          PC = PC + 1;
          result = regFile[rD];
        end  // And
        4'h4: begin
          regFile[rD] = regFile[r1] << regFile[r2];
          PC = PC + 1;
          result = regFile[rD];
        end  // Shift Left
        4'h5: begin
          regFile[rD] = regFile[r1] >> regFile[r2];
          PC = PC + 1;
          result = regFile[rD];
        end  // Shift Right
        4'h6: begin
          regFile[rD] = regFile[r1] | regFile[r2];
          PC = PC + 1;
          result = regFile[rD];
        end  // Or 
        4'h7: begin  // Load
          MAddress = regFile[r1];
          wait (MRead_ready);
          regFile[rD] = MRead_data;
          PC = PC + 1;
          result = regFile[rD];
        end
        4'h8: begin  // Store
          MAddress = regFile[r1];
          MWrite_data = regFile[rD];
          wait (MWrite_done);
          PC = PC + 1;
          result = regFile[rD];
        end
        4'h9: begin
          PC = (regFile[r1] == regFile[r2]) ? regFile[rD] : PC + 1;
          result = PC;
        end  // Branch if equal
        4'ha: begin
          PC = regFile[rD];
          result = PC;
        end  // Jump 
        4'hb: begin
          regFile[rD] = regFile[r1] + {{12{immD[0]}}, immD};
          PC = PC + 1;
          result = regFile[rD];
        end  // Add extended immediate
      endcase
    end
  end


endmodule
