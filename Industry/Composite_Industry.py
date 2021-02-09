def main():
    file = open(r"NASDAQ\Sorted_Sector_$2.5.txt",'r')
    file1 = open(r"NYSE\Sorted_Sector_$2.5.txt",'r') 
    file2 = open(r"Merged.txt", 'w')
    NYSE_list = []
    NASDAQ_list = []
    COMP_list = []
       
    
    for line in file:
                
        this_line = line
        
        ticker = this_line.rsplit('\t',1)[0]
        
        #gets a list of stock tickers
        NYSE_list.append(this_line)    
    
    
    for line in NYSE_list:
        
        #lazy way of fixing text file problems
        
        line = line.strip()
        
        ticker = line.rsplit('\t',1)[0]     
        
        tickers = ticker.rsplit(',')
        
        ticker = tickers[0]
        
        price = tickers[1]
        
        sector = tickers[2]
        
        industry = tickers[3]
        
        COMP_list.append((ticker,price,sector,industry))
        
        #print(ticker,price)
        
    
    
    for line in file1:
                
        this_line = line
        
        ticker = this_line.rsplit('\t',1)[0]
        
        #gets a list of stock tickers
        NASDAQ_list.append(this_line)    
    
    
    for line in NASDAQ_list:
        
        line = line.strip()
        
        #lazy way of fixing text file problems
        
        ticker = line.rsplit('\t',1)[0]     
        
        tickers = ticker.rsplit(',')
        
        ticker = tickers[0]
        
        price = tickers[1]
        
        sector = tickers[2]
        
        industry = tickers[3]
        
        if ticker not in COMP_list:
        
            COMP_list.append((ticker,price,sector,industry))
    
    #changes what it is sorted by x[0] for by ticker, x[1] for price, x[2] for sector, x[3] for industry
    COMP_list.sort(key = lambda x: x[3])
    #print(COMP_list)
    
    for line in COMP_list:
        
        this_line = line[0]+', ' + line[1]+', ' + line[2] + ', ' + line[3] +'\n'
        
        file2.write(this_line)




    file.close()
    file1.close()
    file2.close()    
main()
