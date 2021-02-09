def main():
    file = open(r"NYSE.txt",'r')
    file1 = open(r"NASDAQ.txt",'r') 
    file2 = open(r"Merged.txt", 'w')
    NYSE_list = []
    NASDAQ_list = []
    COMP_list = []
       
    
    for line in file:
        
        if 'Symbol' in line:
            
            continue
                
        this_line = line
        
        ticker = this_line.rsplit('\t',1)[0]
        
        description = this_line.rsplit('\t',1)[1]
        
        #gets a list of stock tickers
        NYSE_list.append(this_line)    
    
    
    for line in NYSE_list:
        
        #lazy way of fixing text file problems
        
        
        
        ticker = line.rsplit('\t',1)[0]     
        
        description = line.rsplit('\t',1)[1]
        
        tickers = ticker.rsplit(',')
        
        ticker = tickers[0]
        
        
        #print(ticker)
        
        COMP_list.append((ticker,description))
        
        #print(ticker,price)
        
    
    
    for line in file1:
        
        if 'Symbol' in line:
            
            continue
                
        this_line = line
        
        ticker = this_line.rsplit('\t',2)[0]
        
        #gets a list of stock tickers
        NASDAQ_list.append(this_line)    
    
    
    for line in NASDAQ_list:
        
        
        
        #lazy way of fixing text file problems
        
        ticker = line.rsplit('\t')[0]     
        
        tickers = ticker.rsplit(',')
        
        description = line.rsplit('\t',1)[1]
        
        #print(ticker)
        
        
                
        if ticker not in COMP_list:
        
            COMP_list.append((ticker,description))
    
    #changes what it is sorted by x[0] for by ticker, x[1] for price, x[2] for sector, x[3] for industry
    #print(COMP_list)
    COMP_list.sort(key = lambda x: x[0])
    file2.write('Symbol\tDescription\n')
    for line in COMP_list:
        
        this_line = line[0] + '\t' +line[1]
        
        file2.write(this_line)




    file.close()
    file1.close()
    file2.close()    
main()
