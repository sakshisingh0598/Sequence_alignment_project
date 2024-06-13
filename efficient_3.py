import sys
# from resource import * 
import time
import psutil
import math
# Initialise cost matrix for gap penalties and delta in order A, C, G, T
cost_for_alignment = [
    [0, 110, 48, 94],
    [110, 0, 118, 48],
    [48, 118, 0, 110],
    [94, 48, 110, 0]
]

delta = 30

def convert_to_string(s):
  if s == 'A':
    return 0
  elif s == 'C':
    return 1
  elif s == 'G':
    return 2
  elif s == 'T':
    return 3   
  
def process_memory():
  process = psutil.Process() 
  memory_info = process.memory_info()
  memory_consumed = int(memory_info.rss/1024) 
  return memory_consumed
  
def time_wrapper(): 
  start_time = time.time() 
  call_algorithm()
  end_time = time.time()
  time_taken = (end_time - start_time)*1000 
  return time_taken

def seq_alignGetCost(s1, s2):
    m = len(s1)
    n = len(s2)

    prev=[0]*(n+1)
    for i in range(n+1):
        prev[i]=i * delta
    
    for i in range(1, m + 1):
        curr=[0]*(n+1)
        curr[0]=i * delta
        for j in range(1, n + 1):
            alpha = cost_for_alignment[convert_to_string(s1[i - 1])][convert_to_string(s2[j - 1])]
            curr[j]=min(prev[j-1]+alpha, prev[j] + delta, curr[j-1] + delta)
            
        prev=curr
        
  
    final_cost = curr[n]
    return curr

def seq_alignDnC(x,y):
    # divide the 
    m = len(x)
    n = len(y)

    if(m==0):
        final_string1=""
        for i in range(0,n):
            final_string1+="_"
        return (n*delta,final_string1,y)
    elif(n==0):
        final_string2=""
        for i in range(0,m):
            final_string2+="_"
        return (m*delta,x,final_string2)
    elif(m==1):
        #cost of putting gaps on each character
        all_gaps=delta + n*delta

        #cost of alligning only one character and rest gaps
        align_one=math.inf
        align_idx=1
        for j in range(1, n + 1):
            alpha = cost_for_alignment[convert_to_string(x[0])][convert_to_string(y[j - 1])]
            if (align_one>alpha+(n-1)*delta):
                align_idx=j
                align_one=alpha+(n-1)*delta
        final_string1=""
        final_string2=""
        if(align_one<all_gaps):
            for i in range(0,align_idx-1):
                final_string1+="_"
            final_string1+=x[0]
            for i in range(align_idx,n):
                final_string1+="_"
            final_string2=y
            return (align_one,final_string1,final_string2)
        else:
            final_string1=x[0]
            for i in range(0,n):
                final_string1+="_"
            final_string2+=y+"_"
            return (all_gaps,final_string1,final_string2)
        
                
    elif(n==1):
        #cost of putting gaps on each character
        all_gaps=delta + m*delta

        #cost of alligning only one character and rest gaps
        align_one=math.inf
        align_idx=1
        for i in range(1, m + 1):
            alpha = cost_for_alignment[convert_to_string(x[i-1])][convert_to_string(y[0])]
            if (align_one>alpha+(m-1)*delta):
                align_idx=i
                align_one=alpha+(m-1)*delta
        final_string1=""
        final_string2=""
        if(align_one<all_gaps):
            for i in range(0,align_idx-1):
                final_string2+="_"
            final_string2+=y[0]
            for i in range(align_idx,m):
                final_string2+="_"
            final_string1=x
            return (align_one,final_string1,final_string2)
        else:
            final_string2=y[0]
            for i in range(0,m):
                final_string2+="_"
            final_string1+=x+"_"
            return (all_gaps,final_string1,final_string2)
        
    else:
        xl_cost=seq_alignGetCost(x[0:m//2],y)
        xr_cost=seq_alignGetCost(x[m//2:][::-1],y[::-1])

        min_cost=math.inf
        div_point=0
        for j in range(0,n+1):
            if min_cost > xl_cost[j]+xr_cost[n-j]:
                min_cost=xl_cost[j]+xr_cost[n-j]
                div_point=j
        if(div_point!=0):
            _,xl_seq_align,yl_seq_align=seq_alignDnC(x[0:m//2],y[0:div_point])
            _,xr_seq_align,yr_seq_align=seq_alignDnC(x[m//2:],y[div_point:])
            return (min_cost,xl_seq_align+xr_seq_align,yl_seq_align+yr_seq_align)
        elif(div_point==0):
            _,xl_seq_align,yl_seq_align=seq_alignDnC(x[0:m//2],"")
            _,xr_seq_align,yr_seq_align=seq_alignDnC(x[m//2:],y[div_point:])
            return (min_cost,xl_seq_align+xr_seq_align,yl_seq_align+yr_seq_align)
        elif(div_point==n):
            _,xl_seq_align,yl_seq_align=seq_alignDnC(x[0:m//2],y[0:div_point])
            _,xr_seq_align,yr_seq_align=seq_alignDnC(x[m//2:],"")
            return (min_cost,xl_seq_align+xr_seq_align,yl_seq_align+yr_seq_align)
        
    

def seq_alignUtils(s1, s2):
    # implement basic algorithm here
    
    time_taken = 0.0  
    memory_consumed = 0.0
    
    start_algo_time = time.time()
    start_algo_memory = process_memory()
    
    # final_cost=seq_alignGetCost(s1,s2)[len(s2)]
    final_cost,final_string1,final_string2=seq_alignDnC(s1,s2)
        

    # implement memory efficient algorithm for Sequence alignment
    
    end_algo_time = time.time()
    end_algo_memory = process_memory()
    
    time_taken = (end_algo_time - start_algo_time)*1000
    memory_consumed = end_algo_memory - start_algo_memory
    
    return str(final_cost) + "\n" + final_string1 + "\n" + final_string2 + "\n" +str(time_taken) + "\n" + str(memory_consumed) + "\n"
    # return str(final_cost)
  
def getString(s, index):
    modified_string = s[:index + 1] + s + s[index + 1:]  
    return modified_string

def seq_alignment(string_inputs, randomize1, randomize2):
    s1 = string_inputs[0]
    for index in randomize1:
        s1 = getString(s1, index)
    s2 = string_inputs[1]
    for index in randomize2:
        s2 = getString(s2, index)
    return seq_alignUtils(s1, s2)
  

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 basic.py input_file output_file")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as f:
            data = f.read()
            lines = data.splitlines()
            string_inputs = [] 
            randomize1 = []
            randomize2 = []
            for line in lines:
                if line.strip() and line[0].isalpha(): 
                    string_inputs.append(line) 
                else:
                    if len(string_inputs) == 1:
                        randomize1.append(int(line))
                    else:
                        randomize2.append(int(line))
    except FileNotFoundError:
        print("Input file not found.")
        return
    
    try:
        with open(output_file, 'w') as f:
            f.write(seq_alignment(string_inputs,randomize1,randomize2)) 
    except Exception as e:
        print("Error occurred while writing to the output file:", e)

if __name__ == "__main__":
    main()
