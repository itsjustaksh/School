// test bench for part 1
module my_circuit_tb ;
  
    reg a ; 
	reg b; 
	reg c ; // control signal
	
	wire out ;


// instantiate your module here
    q1 testq1(.a(a), .b(b), .ctrl(c), .c(out));
//  make sure to connect the ins/outs properly
 
 initial begin
   
       a = 1'b0; b= 1'b0; c=1'b0 ;
 #100  a = 1'b0; b= 1'b1; c=1'b0 ;
 #100  a = 1'b1; b= 1'b0; c=1'b0 ;
 #100  a = 1'b1; b= 1'b1; c=1'b0 ;
   
       a = 1'b0; b= 1'b0; c=1'b1 ;
 #100  a = 1'b0; b= 1'b1; c=1'b1 ;
 #100  a = 1'b1; b= 1'b0; c=1'b1 ;
 #100  a = 1'b1; b= 1'b1; c=1'b1 ;
 
 end 
 
endmodule

//------------------------------------

// test bench template for part 2
module my_circuit_tb ;
  
    reg a ; 
	reg b; 
	reg c ;

	reg clk ;  // add clock and reset
	wire out ;

// instantiate your module here
    q2 testq2(.a(a), .b(b), .ctrl(c), .clk(clk), .c(out));
//  make sure to connect the ins/outs properly
 
 // -------------building the clock signal----------------------
 always clk  = #10 ~clk ;
 
 // to invert the clock the following code can also be used:
 initial begin 
   forever #10  clk = !clk;
  end
  //---------------------------------------------------
 
 initial begin
   clk = 1'b0 ; 
 #100  a = 1'b0; b= 1'b0; c=1'b0 ;
 #100  a = 1'b0; b= 1'b1; c=1'b0 ;
 #100  a = 1'b1; b= 1'b0; c=1'b0 ;
 #100  a = 1'b1; b= 1'b1; c=1'b0 ;
   
       a = 1'b0; b= 1'b0; c=1'b1 ;
 #100  a = 1'b0; b= 1'b1; c=1'b1 ;
 #100  a = 1'b1; b= 1'b0; c=1'b1 ;
 #100  a = 1'b1; b= 1'b1; c=1'b1 ;
 
 end 
 
endmodule
//-----------------------------------------------------
//------------------------------------
// test bench template for part 3
module my_circuit_tb ;
  
    reg a ; 
	reg b; 
	reg c; // control signal
	reg rst ;

	reg clk ;  // add clock and reset
	wire out ;

// instantiate your module here
    q3 testq3(.a(a), .b(b), .ctrl(c), .clk(clk), .c(out));
//  make sure to connect the ins/outs properly


 
 // -------------building the clock signal----------------------
 always clk  = #10 ~clk ;
 
 // to invert the clock the following code can also be used:
 initial begin 
   forever #10  clk = !clk;
  end
  //---------------------------------------------------
 
 initial begin
   clk = 1'b0 ; rst = 1'b0 ;
 #200 rst = 1'b1 ;
 #400 rst = 1'b0 ;
 
 #100  a = 1'b0; b= 1'b0; c=1'b0 ;
 #100  a = 1'b0; b= 1'b1; c=1'b0 ;
 #100  a = 1'b1; b= 1'b0; c=1'b0 ;
 #100  a = 1'b1; b= 1'b1; c=1'b0 ;
   
       a = 1'b0; b= 1'b0; c=1'b1 ;
 #100  a = 1'b0; b= 1'b1; c=1'b1 ;
 #100  a = 1'b1; b= 1'b0; c=1'b1 ;
 #100  a = 1'b1; b= 1'b1; c=1'b1 ;
 
 end 
 
endmodule
