import sys
# from resource import * 
import time
import psutil
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

def seq_alignUtils(s1, s2):
    # implement basic algorithm here
    
    time_taken = 0.0  
    memory_consumed = 0.0
    
    start_algo_time = time.time()
    start_algo_memory = process_memory()
    
    m = len(s1)
    n = len(s2)
    opt = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        opt[i][0] = i * delta
    for j in range(n + 1):
        opt[0][j] = j * delta
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            alpha = cost_for_alignment[convert_to_string(s1[i - 1])][convert_to_string(s2[j - 1])]
            opt[i][j] = min(opt[i - 1][j - 1] + alpha, opt[i - 1][j] + delta, opt[i][j - 1] + delta)
  
    final_cost = opt[m][n]
    
    i = m
    j = n
    
    final_string1 = ""
    final_string2 = ""
    
    while i > 0 and j > 0:
        alpha = cost_for_alignment[convert_to_string(s1[i - 1])][convert_to_string(s2[j - 1])]
        if opt[i][j] == opt[i - 1][j - 1] + alpha:
            final_string1 = s1[i - 1] + final_string1
            final_string2 = s2[j - 1] + final_string2
            i -= 1
            j -= 1
        elif opt[i][j] == opt[i - 1][j] + delta:
            final_string1 = s1[i - 1] + final_string1
            final_string2 = "_" + final_string2
            i -= 1
            
        else:
            final_string2 = s2[j - 1] + final_string2
            final_string1 = "_" + final_string1
            j -= 1
    
    while i > 0:
        final_string1 = s1[i - 1] + final_string1
        final_string2 = "_" + final_string2
        i -= 1
    
    while j > 0:
        final_string2 = s2[j - 1] + final_string2
        final_string1 = "_" + final_string1
        j -= 1
    
    end_algo_time = time.time()
    end_algo_memory = process_memory()
    
    time_taken = (end_algo_time - start_algo_time)*1000
    memory_consumed = end_algo_memory - start_algo_memory
    
    return str(final_cost) + "\n" + final_string1 + "\n" + final_string2 + "\n" +str(time_taken) + "\n" + str(memory_consumed) 

  
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
